#include <iostream>
#include <cmath>
int Case,n,Min,sum,p,a;
void display()
{
     scanf("%d",&Case);
     for (int ca=1;ca<=Case;ca++) {
         scanf("%d",&n);
         p=sum=0;
         Min=0x7fffffff;
         while (n--) {
               scanf("%d",&a);
               p^=a;
               sum+=a;
               Min=(Min>a)?a:Min;
               }
         if (p) printf("Case #%d: NO\n",ca);
         else printf("Case #%d: %d\n",ca,sum-Min);
         }
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    display();
    return 0;
}
