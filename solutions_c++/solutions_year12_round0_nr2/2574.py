#include <iostream>

using namespace std;

int main() {

    int T, N, S, P, temp, res, NotSurp, Surp;
    scanf("%d\n",&T);
    for (int i=1; i<=T ; i++) {
        scanf("%d %d %d",&N, &S, &P);
        res = 0;
        NotSurp = P*3-2;
        Surp = NotSurp-2;
        for (int j=0 ; j<N ; j++) {
            scanf("%d", &temp);
            if (temp >= NotSurp) {
                res++;
            } else if (temp >= Surp && S>0 && Surp>0) {
                S--;
                res++;
            }
        }
        scanf("\n");
        printf("Case #%d: %d\n",i,res);
    }

    return 0;
}