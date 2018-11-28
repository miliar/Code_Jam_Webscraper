#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <cmath>
#include <set>
using namespace std ;
int cs,T,N,B,K ;
const int maxx = 1000000000 ;
int f[100][100] ;
bool mark[100] ;
int x[100],v[100] ;
int main()
{
    freopen("2.txt","w",stdout) ;
    int cs ;
    cin>>cs ;
    int cc ;
    cc = 0 ;
    while (cs--)
    {
          cc++ ;
          cin>>N>>K>>B>>T ;
          for (int i=1;i<=N;i++)
              scanf("%d",&x[i]) ;
          for (int i=1;i<=N;i++)
              scanf("%d",&v[i]) ;
          for (int i=0;i<100;i++)
              for (int j=0;j<100;j++)
                  f[i][j] = maxx ;
          memset(mark,0,sizeof(mark)) ;
          for (int i=1;i<=N;i++)
          {
              if (v[i]*T+x[i]>=B) 
              {
                 mark[i] = true ;
                 f[i][1] = 0 ;
              }
              f[i][0] = 0 ;
          }
          for (int i=1;i<=N;i++)
          {
              if (mark[i])
              {
                 for (int j=0;j<i;j++)
                     f[i][j+1] = min(f[i][j+1],f[i-1][j]) ;
              }
              else
              {
                  for (int j=0;j<i;j++)
                      f[i][j] = min(f[i][j],f[i-1][j] + j) ;
              }
            //  for (int j=0;j<=i;j++)
            //      cout<<i<<" "<<j<<" "<<f[i][j]<<endl ;
          }  
          int res = maxx ;
          for (int i=K;i<=N;i++)
              res = min(f[N][i],res) ;
          if (res!=maxx)
             printf("Case #%d: %d\n",cc,res) ;  
          else
              printf("Case #%d: IMPOSSIBLE\n",cc) ;    
    }
    system("pause") ;
}
