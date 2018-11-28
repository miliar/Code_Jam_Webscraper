#include <iostream>
using namespace std;
#define fo(i,n) for(i=0; i<n; i++)
#define fi(i,n) for(i=1; i<=n; i++)
int a[150][300],b[150],i,j,n,m,in,d,k,ans,t,tt,mx,p;

main()
{
      freopen("input.txt","r",stdin);
      freopen("output.txt","w",stdout);
      scanf("%d",&t);
      fo(tt,t){
         scanf("%d%d%d%d",&d,&in,&m,&n);
         mx=0;
         fi(i,n) scanf("%d",&b[i]), mx>?=b[i];
         mx++;
         
         fi(i,n){
            b[0]=b[i];
            fo(j,mx){
                a[i][j]=123456789; p=abs(j-b[i]);
                fo(k,mx){
                   if (abs(j-k)>m) a[i][j]<?=p+a[i-1][k]+abs(k-j)-m; else a[i][j]<?=p+a[i-1][k];
                   if (m && k!=j) a[i][j]<?=p+a[i-1][k]+((abs(k-j)-1)/m)*in;
                  // if (!m) if (k==j) a[i][j]<?=p+a[i-1][k];
                }
                a[i][j]<?=a[i-1][j]+d;
                a[i][j]<?=p+d*(i-1);
            }
         }
         ans=6557789;
         fo(i,mx) ans<?=a[n][i];
         
         printf("Case #%d: %d\n",tt+1,ans);
      }
}
