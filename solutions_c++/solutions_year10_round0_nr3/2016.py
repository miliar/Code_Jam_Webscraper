#include <cstdio>
#include <algorithm>
typedef long long LL;
using namespace std;

int ntc;
int r,k,n;
int T[1007];
int next[40][1007];
LL cash[40][1007];



int main() {
    scanf("%d", &ntc);
    for(int c=1; c<=ntc; c++) {
                 printf("Case #%d: ", c);
               scanf("%d%d%d", &r,&k,&n);
               for(int i=0; i<n; ++i) scanf("%d", &T[i]);
               //if(n==1) printf("%d\n", r);
               int a=0; LL ac=0; 
               for(int i=0; i<n; ++i) {
                       while(ac+T[a]<=k ) { ac+=T[a]; ++a; if(a==n) a=0; if(a==i) break; }
                       cash[0][i]=ac;
                       next[0][i]=a;
                       if(ac!=0) ac-=T[i];
               }
               for(int i=1; i<=30; ++i) {
                       for(int j=0; j<n; ++j) {
                               next[i][j]=next[i-1][next[i-1][j]];
                               cash[i][j]=cash[i-1][j]+cash[i-1][next[i-1][j]];
                       }
               }
               a=0; ac=0; int p=0;
               while(r>0) {
                          if(r%2) { ac+=cash[p][a]; a=next[p][a]; }
                          r/=2; ++p;           
               }
               printf("%lld\n",ac);
                       
    }                
                       
          
}
