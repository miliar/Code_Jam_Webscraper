#include <cstdio>
unsigned int Curr, Min, Sum, Xor, i, j, T, N;
int main(){
    scanf("%u", &T);
    for(i=0;i<T;i++){
        Min=1000000000;
        Xor=0;
        Sum=0;
        scanf("%u", &N);
        for(j=0;j<N;j++){
            scanf("%u", &Curr);
            Xor^=Curr;
            if(Curr<Min) Min=Curr;
            Sum+=Curr;
        }
        if(Xor!=0) printf("Case #%u: NO\n", i+1);
        else printf("Case #%u: %u\n", i+1, Sum-Min);
    }
    return 0;
}
