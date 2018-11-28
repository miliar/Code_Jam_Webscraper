#include <iostream>
using namespace std;
int main(){
    freopen("gcj1.txt","r",stdin);
    freopen("gcj1.out","w",stdout);
    int oo,bb,ol,bl,N,n,x,ans;
    char c,lc;
    scanf("%d",&N);
    for(int I = 1;I <= N;++I){
        oo = bb = 1;
        ol = bl = 0;
        scanf("%d",&n);
        ans = 0;
        for(int i = 0;i < n;++i){
            scanf(" %c %d",&c,&x);
            if(c == 'O'){
                ol = max(bl,ol + abs(x-oo)) + 1;
                oo = x;
            }
            else{
                bl = max(ol,bl + abs(x-bb)) + 1;
                bb = x;
            }
            ans = max(bl,ol);
            lc = c;
        }
        printf("Case #%d: %d\n",I,ans);
    }
}
