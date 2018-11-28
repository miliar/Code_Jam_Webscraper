#include <cstdio>
using namespace std;
int t,tt,i,k,n;
int main() {
   freopen("Al.in","r",stdin);
   freopen("Al.out","w",stdout);
   scanf("%d",&t);
   for (tt=1; tt<=t; tt++) {
     scanf("%d%d",&n,&k); k++;
     for (i=1; (k&1)==0; i++) k/=2;
     printf("Case #%d: ",tt);
     if (n>=i) puts("OFF"); else puts("ON");
   }
   return 0;
}
