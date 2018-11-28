#include <cstdio>
#include <algorithm>
typedef long long LL;
using namespace std;

int ntc,n,k,p;
bool T[40];


int main() {
scanf("%d", &ntc);
    for(int c=1; c<=ntc; c++) {
                 scanf("%d%d", &n,&k);
                 printf("Case #%d: ", c);
                 p=1; while(n--) p*=2;
                 if((k+1)%p==0) printf("ON\n");
                 else printf("OFF\n");                       
    }                
                       
          
}
