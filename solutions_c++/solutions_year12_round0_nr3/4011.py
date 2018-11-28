#include <cstdio>
using namespace std;

int a,b;

int prije[10];

int transform ( int broj ){
     int pot=10,dummy=broj/10,novi,dulj=10;
     int zbr=0;
     while ( dulj < broj ) dulj*=10;
     int poz=0,kraj;
     while (dummy>0){
         if ( ( ( broj/(pot/10) ) % 10 ) != 0){
            novi= broj/pot+ (broj%pot)*(dulj/pot);
            if (broj<novi && novi>=a && novi<=b){ 
               kraj=0;
               for (int i=0;i<poz;++i) if (novi==prije[i]) kraj=1;
               if (kraj==0){
                  ++zbr; 
                  prije[poz]=novi;
                  ++poz;
                  //printf ("%d %d\n",broj,novi);
               }
            }
            //printf ("%d %d %d\n",broj,novi,pot);
         }
         dummy/=10;
         pot*=10;
     }
     return zbr;
}

void solve ( int test ){
     scanf ("%d%d",&a,&b);
     long long zbr=0;
     for (int i=a;i<=b;++i){
         zbr+=(long long) transform(i);
     } 
     printf ("Case #%d: %I64lld\n",test,zbr);
     return;    
}

int main (){
    int t;
    scanf ("%d",&t);
    for (int i=0;i<t;++i){
        solve (i+1);
    }
    return 0;
}
