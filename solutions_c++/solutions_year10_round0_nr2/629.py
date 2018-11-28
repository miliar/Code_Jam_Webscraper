// GCJ QUAL I - B
#include <iostream>
using namespace std;
#define fo(i,n) for(i=0; i<n; i++)
int i,j,n,m,p,t,a1,a2,a3;

int usg(int x, int y){
    int l;
    if (x<y) l=x, x=y, y=l; 
    if (y==0) return x;
    return usg(y,x%y); 
}


main()
{
      freopen("input.txt","r",stdin);
      freopen("output.txt","w",stdout);
      
      scanf("%d",&t);
      fo(i,t){
         scanf("%d",&n);
         scanf("%d%d",&a1,&a2);
         if (n==3){
            scanf("%d",&a3);
            p=usg(abs(a1-a2),abs(a1-a3));
            if (p==1) printf("Case #%d: %d\n",i+1,0); else
            printf("Case #%d: %d\n",i+1,(p-(a1%p))%p);
         } else
         {
            p=abs(a1-a2);
            printf("Case #%d: %d\n",i+1,(p-(a1%p))%p);
         }
      }
}
