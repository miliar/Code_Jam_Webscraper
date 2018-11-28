#include<iostream>
#include<vector>
#include<map>
using namespace std ;
#define INF (int)1e9
int n,g[100][100],a[100] ;

main()
{
 int i,j,k,runs ;
 char buff[100] ;

 freopen("in.txt","r",stdin) ;
 freopen("out1.txt","w",stdout) ;
 scanf("%d",&runs) ;
 for(int t=1;t<=runs;t++)
 {
  scanf("%d",&n) ;
  for(i=0;i<n;i++)
   for(j=0;j<n;j++)
    g[i][j] = 1 ;
  for(i=0;i<n;i++)
  {
   scanf("%s",buff) ;
   for(j=n-1;j>=0;j--)
    if(buff[j] == '1')
     break ;
   j = max(j,0) ;
   a[i] = j ;
  }
  int ret = 0 ;
  for(i=0;i<n;i++) if(a[i] > i)
  {
   for(j=i+1;j<n;j++) if(a[j] <= i) break ;
   for(;j>i;j--) a[j] = a[j-1],ret ++ ;
  }
  printf("Case #%d: %d\n",t,ret) ;
 }
// while(1) ;
}
