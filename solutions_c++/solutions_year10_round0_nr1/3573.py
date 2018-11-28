#include <iostream>
using namespace std;

int t, n, k, tmp;

int main(){
   // freopen("A-large.in", "r", stdin);
  //  freopen("A-large.out", "w", stdout);
    scanf("%d", &t);
    for(int a=1;a<=t;++a){
        scanf("%d%d", &n, &k);
        tmp = 0;
        for(int i=0;i<n;++i) if((k&(1<<i))) ++tmp;
        if(tmp == n) printf("Case #%d: ON\n", a);
        else printf("Case #%d: OFF\n", a);
    }
  //  system("pause");
}
