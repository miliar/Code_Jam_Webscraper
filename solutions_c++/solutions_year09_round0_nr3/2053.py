#include <iostream>
#include <stdlib.h>
#include <string>
char t[]="welcome to code jam";
std::string s;
int sl,tl;
long long w;
void go(int lvl,int pos)
{
    if(pos>=sl)return;
    for(int i=pos;i<sl;++i)
    {
        if(s[i]==t[lvl])
        {
            if(lvl==tl-1)
            {
                ++w;
            }
            else
            {
                go(lvl+1,i+1);
            }
        }
    }                
}    
int main()
{
  int n;
  tl=strlen(t);
  scanf("%d\n",&n);
  for(int i=1;i<=n;++i)  
  {
      s.clear();
      char c;
      while(true)
      {
          c=getchar();
          if(!((c>='a'&&c<='z')||c==' '))break;
          s.push_back(c);
      }    
      sl=s.length();
      w=0;
      go(0,0);
      printf("Case #%d: %04lld\n",i,w%10000);
  }
  return 0;
}
