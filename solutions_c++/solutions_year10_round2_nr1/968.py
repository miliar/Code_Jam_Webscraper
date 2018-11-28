#include <stdio.h>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class dir{
      public:
             string s;
             dir *child[200];
             dir()
             {
               for(int i=0;i<200;i++)child[i]=NULL;
               s.clear();
             }
};

bool last;

string readDir()
{
  char ch; string out;
  scanf("%c",&ch);
  while(ch!='/' && ch!='\n')
  {
    out.push_back(ch);
    if( scanf("%c",&ch)==EOF ){ last = true; return out;  }
  }
  if( ch=='\n' )last = true; else last = false;
  return out;
}

dir *root;

long push(dir* c)
{
  string s; long i,cnt = 0;
  if(last){ last = false; return 0; }
  s = readDir();
  if(s.empty())return 0;
  bool found = false;
  for(i=0;c->child[i]!=NULL;i++)
    if( c->child[i]->s == s )
    {
      found = true;
      cnt += push(c->child[i]);
    }
  if(!found)
  {
    c->child[i] = new dir();
    c->child[i]->s = s;
    cnt += push(c->child[i]);
    cnt++;
  }
  return cnt;
}

main()
{
  freopen("A-large.in","r",stdin);
  freopen("file.out","w",stdout);
  long t,tc,ans,n,m,i;
  scanf("%d",&tc);
  for(t=1;t<=tc;t++)
  {
    root = new dir;
    ans = 0;
    scanf("%d %d\n",&n,&m);
    
    for(i=0;i<n;i++)  
    {
      readDir();
      push(root);
    }
    
    for(i=0;i<m;i++) 
    { 
      readDir();
      ans += push(root);
    }
      
    printf("Case #%d: %d\n",t,ans);
  }
}
