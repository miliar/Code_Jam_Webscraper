#include <iostream>
using namespace std;
#define fo(i,n) for(i=0; i<n; i++)
#define fi(i,n) for(i=1; i<=n; i++)
int i,j,n,m,l,r,k,t;
int a[1500],b[1500];
long long ans,p,c[1500];


main()
{
      freopen("input.txt","r",stdin);
      freopen("output.txt","w",stdout);
      
      scanf("%d",&t);
      fo(i,t){
         scanf("%d%d%d",&m,&k,&n);
         memset(a,0,sizeof(a));
         memset(b,0,sizeof(b));
         memset(c,0,sizeof(c));
         fi(j,n) scanf("%d",&a[j]), a[j]+=a[j-1];
         fi(j,n){
            p=0;
            for(l=j; l<=n; l++) if (a[l]-a[j-1]>k) break;
            if (l>n) l=n;
            if (a[l]-a[j-1]<=k){
                p=a[l]-a[j-1];
                fi(l,j-1) if (p+a[l]>k) break;
                b[j]=l; c[j]=p+a[l-1];
            } else b[j]=l, c[j]=a[l-1]-a[j-1];
         }
         p=1; ans=0;
         
         fo(j,m){
              ans+=c[p]; p=b[p];
         }
         printf("Case #%d: ",i+1);
         cout<<ans<<endl;
      }
}
