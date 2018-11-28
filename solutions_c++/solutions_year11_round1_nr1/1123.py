#include <cstdio>
using namespace std;

long long gcd (long a, long b){
     long long tmp;
     while (b!=0){
         tmp=a;
         a=b;
         b=tmp%b;
     }
     return a;
}

void solve (int test){
     long long n,pd,pg;
     scanf ("%I64lld%I64lld%I64lld",&n,&pd,&pg);
     long long a2=100/gcd(100,pd),a1=pd/gcd(100,pd),b2=100/gcd(100,pg),b1=pg/gcd(100,pg);
     long long usp,fail,ost;
     int kraj=0;
     int prvi=0;
     if (a2>n){
        printf ("Case #%d: Broken\n",test);
        return;
     }
     while (b2<a2){
           b1*=2;
           b2*=2;
     }
     int br=0;
     for (int i=a2;br<9;i+=a2){
         ++br;
         if (prvi==1){
            b1*=2;
            b2*=2;
         }
         if (prvi==0) prvi=1;
         usp=a1; fail=a2-a1;
         if (b1<usp || b2-b1<fail) continue;
         ost=b2-a2;
         if (b1>usp) ost-=b1-usp;
         if (ost<0) continue;
         if (b2-b1>fail) ost-=(b2-b1)-fail;
         if (ost<0) continue;
         if (ost==0){
            kraj=1;
            break;
         }
     }
     if (kraj==1) printf ("Case #%d: Possible\n",test); else printf ("Case #%d: Broken\n",test);
}

int main (){
    int t;
    scanf ("%d",&t);
    for (int i=0;i<t;++i){
          solve (i+1);
    }
    return 0;
}
