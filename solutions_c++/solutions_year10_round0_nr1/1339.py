// GCJ - QUAL I -- A
#include <iostream>
using namespace std;
#define fo(i,n) for(i=0; i<n; i++)
long long p,m;
int i,j,n,t;


main()
{
      freopen("input.txt","r",stdin);
      freopen("output.txt","w",stdout);
      
      scanf("%d",&t);
      fo(i,t){
         cin>>n>>m; p=1; m++;
         fo(j,n) p*=2;
         if (m%p) printf("Case #%d: OFF\n",i+1); else printf("Case #%d: ON\n",i+1);
      }
}
