#include <cstdio>
#include <cstring>
using namespace std;

int a[1000];

bool bio[6000000];
int di[6000000];

void solve (int test){
     memset(bio,0,sizeof(bio));
     memset(di,0,sizeof(di));
     int n;
     scanf ("%d",&n);
     for (int i=0;i<n;++i){
         scanf ("%d",&a[i]);
     }
     printf ("Case #%d:\n",test);
     int zbr=0;
     for (int i=0;i<(1<<n);++i){
        zbr=0;
        for (int j=0;j<n;++j){
            if ( ( (i>>j) &1) == 1 ) zbr+=a[j];
        }
        //printf ("%d %d\n",i,zbr);
        if (bio[zbr]==1){
           for (int j=0;j<n;++j){
              if ( ( (i>>j) &1) == 1 ){
                 if (j==n-1) printf ("%d",a[j]); else printf ("%d " ,a[j]);
              }
           }
           printf ("\n");
           for (int j=0;j<n;++j){
              if ( ( (di[zbr]>>j) &1) == 1 ){
                 if (j==n-1) printf ("%d",a[j]); else printf ("%d " ,a[j]);
              }
           }
           printf ("\n");
           return;
        }
        bio[zbr]=1;
        di[zbr]=i;
     }
     printf ("Impossible\n");
     return;
}

int main (){
    int t;
    scanf ("%d",&t);
    for (int i=0;i<t;++i) solve(i+1);
    return 0;
}
