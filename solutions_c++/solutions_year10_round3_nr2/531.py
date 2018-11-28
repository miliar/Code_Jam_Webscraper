#include <cstdio>
#include <cstdlib>
#include <cmath>

#define MAXN 2 << 30

using namespace std;

int L, P, C, T;

int solve(){

    int l = L;

    int c = 0;

    while(l*C < P){
        c++;

        l = l*C;
    }


    if (c == 0)
        return 0;

    //printf("%d", c);
    return floor(log(c)/log(2)) + 1;

}

int main(){

    scanf("%d", &T);

    for (int i = 0; i < T; i++){
        scanf("%d %d %d", &L, &P, &C);

        int res;

        res = solve();

        printf("Case #%d: %d\n", i+1, res);
    }

    return 0;
}
