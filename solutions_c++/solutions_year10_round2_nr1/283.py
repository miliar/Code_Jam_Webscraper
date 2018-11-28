#include<cassert>
#include<cstring>
#include<cstdio>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<cmath>
#include<iostream>
#include<algorithm>
#define eps 1e-12
#define sqr(a) (a)*(a)
#define forn(i,n) for(int i=0;i<(int)n;i++)
#define taskname ""
typedef long long ll;
using namespace std;
set<string> x;
void add(string s)
{
  if(!x.count(s))
  {
    for(int j=s.size()-1;j>=0;j--)
      if(s[j]=='/')
      {
        add(s.substr(0,j));
        //cerr<<s<<' '<<s.substr(0,j)<<endl;
        x.insert(s);
      }
  }  
}
int main()         
{
  //#ifdef DEBUG
  /*freopen(taskname".in","r",stdin);                         
  freopen(taskname".out","w",stdout);*/
  //#endif
  int t;
  scanf("%d",&t);
  forn(test,t)
  { 
    string s;
    int n,m;
    printf("Case #%d: ",test+1);
    x.clear();
    x.insert("");
    scanf("%d %d ",&n,&m);
    //cerr<<n<<' '<<m<<endl;
    forn(i,n)
    {                     
      cin>>s;
      x.insert(s);
    }
    forn(i,m)
    {
      cin>>s;
      //cerr<<s<<endl;
      add(s);
    }
    printf("%d\n",x.size()-n-1);
  }
  return 0;
}

