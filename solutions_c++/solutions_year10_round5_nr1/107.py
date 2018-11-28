#include <cstdio>
using namespace std;
int t,tt,i,j,p,c,r,d,n,sk,st,x[15]; // Is long long needed?
bool a[1000100],q,qq;
long long A,B,y;
long long pow(long long a, int b) {
  if (b==0) return 1%p;
  if (b&1) return (a*pow(a,b-1))%p; else {
    long long x=pow(a,b/2);
    return (x*x)%p;
  }
}
int main() {
   freopen("Al.in","r",stdin);
   freopen("Al.out","w",stdout);
   for (i=2; i<1000100; i++) if (!a[i]) for (j=2*i; j<1000100; j+=i) a[j]=true;
   scanf("%d",&t);
   for (tt=1; tt<=t; tt++) {
     scanf("%d%d",&d,&n); r=-1; st=sk=1;
     for (i=0; i<d; i++) st*=10;
     for (i=0; i<n; i++) {
       scanf("%d",&x[i]);
       if (x[i]>sk) sk=x[i];
     }
     qq=(n>1);
     if (n==2) {
       if (x[0]==x[1]) r=x[0]; else qq=false;
     }
     if (n>2) for (p=sk+1; p<=st; p++) if (qq && !a[p]) {
       y=pow((x[1]-x[0]+p)%p,p-2);
       A=(((x[2]-x[1]+p)%p)*y)%p;
       B=(x[1]-(A*x[0])%p+p)%p;
       q=true;
       for (i=1; i<n-1; i++) if ((A*x[i]+B)%p!=x[i+1]) {
         q=false; break;
       }
       if (q) {
         c=(A*x[n-1]+B)%p;
         if (r==-1 || c==r) r=c; else { qq=false; break; }
       }
     }
     printf("Case #%d: ",tt);
     if (qq) printf("%d\n",r); else puts("I don't know.");
   }
   return 0;
}
