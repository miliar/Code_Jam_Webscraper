#include<vector>
#include<list>
#include<map>
#include<set>
#include<queue>
#include<deque>
#include<stack>
#include<bitset>
#include<sstream>
#include<algorithm>
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
using namespace std;
#define S(n) scanf("%d",&n)
#define SL(n) scanf("%lld",&n)
#define SS(n) scanf("%s",&n)
#define FOR(i,n) for(i=0;i<n;i++)
#define REP(i,j,n) for(i=j;i<n;i++)

int main()
{
    freopen("Codejam_A_in.txt","r",stdin);
    freopen("Codejam_A_out.txt","w",stdout);
    int t,i,j,k,cas=1;
    S(t);
    while(t--)
    {
              int a=0,b=0;
              bool f=false,g=false,inco=false;
              char s[8][8];
              FOR(i,4)
              SS(s[i]);
              FOR(i,4)
              {
                      a=b=0;
                      FOR(j,4)
                      {
                              if(s[i][j]=='X' || s[i][j]=='T')
                              a++;
                              if(s[i][j]=='O' || s[i][j]=='T')
                              b++;  
                      }
                      if(a==4)
                      {
                              printf("Case #%d: X won\n",cas);
                              f=true;
                              break;
                      }
                      else if(b==4)
                      {
                              printf("Case #%d: O won\n",cas);
                              g=true;
                              break;
                      }
              }
              if(f || g)
              {
                   cas++;
                   continue;
              }
              FOR(i,4)
              {
                      a=b=0;
                      FOR(j,4)
                      {
                              if(s[j][i]=='X' || s[j][i]=='T')
                              a++;
                              if(s[j][i]=='O' || s[j][i]=='T')
                              b++;   
                      }
                      if(a==4)
                      {
                              printf("Case #%d: X won\n",cas);
                              f=true;
                              break;
                      }
                      else if(b==4)
                      {
                              printf("Case #%d: O won\n",cas);
                              g=true;
                              break;
                      }
              }
              if(f || g)
              {
                   cas++;
                   continue;
              }
              a=b=0;
              for(i=0;i<4;i++)
              {
                      if(s[i][i]=='X' || s[i][i]=='T')
                      a++;
                      if(s[i][i]=='O' || s[i][i]=='T')
                      b++;   
              }
              if(a==4)
              {
                   printf("Case #%d: X won\n",cas);
                   f=true;
              }
              else if(b==4)
              {
                   printf("Case #%d: O won\n",cas);
                   g=true;
              }
              if(f || g)
              {
                   cas++;
                   continue;
              }
              a=b=0;
              for(i=0;i<4;i++)
              {
                      if(s[3-i][i]=='X' || s[3-i][i]=='T')
                      a++;
                      if(s[3-i][i]=='O' || s[3-i][i]=='T')
                      b++;   
              }
              if(a==4)
              {
                   printf("Case #%d: X won\n",cas);
                   f=true;
              }
              else if(b==4)
              {
                   printf("Case #%d: O won\n",cas);
                   g=true;
              }
              if(f || g)
              {
                   cas++;
                   continue;
              }
              FOR(i,4)
              {
                      FOR(j,4)
                      {
                              if(s[i][j]=='.')
                              {
                                              inco=true;
                                              break;
                              }
                      }
              }
              if(inco)
              {
                      printf("Case #%d: Game has not completed\n",cas);
                      cas++;
                      continue;
              }
              else
              {
                  printf("Case #%d: Draw\n",cas);
                  cas++;
                  continue;
              }
    }
    return 0;
}
