#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <cassert>
#include <cmath>
#include <string>
#include <set>
using namespace std;
vector<char> cnt;
char buf[70];
int len;
long long res;
void solve()
{
    int base; 
    if(len<=2) base = 2;
    else base = len;
    char c = buf[0];
    res = 0;
    int i=0;
    while( buf[i]!='\0' )
    {
           int t,num;
           for(int j=0;j<cnt.size();j++)
           {
                   if(cnt[j]==buf[i]) {t=j; break;}        
           }
           if(t==1) num = 0;
           else if(t==0) num = 1;
           else num = t;
           res = res*base + num;     
           i++;  
    }      
}
int main(int argc, char *argv[])
{
    freopen("A-large.in","r",stdin);
 //    freopen("B-large-practice (1).in","r",stdin);
    freopen("out.txt","w",stdout);
      
    int N;

    scanf("%d",&N);
    
    int CASE = 1;
    while(N--)
    {
          memset(buf,'\0',sizeof(buf));
          cnt.clear();
          scanf("%s",buf);
  //        printf("%s",buf);
          int i=0;
          while(1)
          {
                  if(buf[i]=='\0') break;
                  char t = buf[i];
                  bool flag = true;
                  for(int j=0;j<cnt.size();j++)
                  {
                         if(cnt[j]==t) {flag=false;break;}         
                  }
                  if(flag==true) cnt.push_back(t);
                  i++;        
          }
          len = cnt.size();
   //       for(int k=0;k<cnt.size();k++)
   //       {
    //              printf("%c ",cnt[k]);
    //      }
          solve();
          printf("Case #%d: %lld\n",CASE,res);
          CASE++;     
    }

    return 0;
}
