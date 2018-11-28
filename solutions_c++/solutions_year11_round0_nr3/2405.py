#include <cstdio>
#include <cstring>

using namespace std;

#define INF 0x3f3f3f3f

int main() {
    int t;
    scanf("%d", &t);
    for (int k = 0; k < t; k++) {
        int n;
        scanf("%d", &n);
        int menor = INF;
        int x;
        int res = 0;
        int soma = 0;
        for (int i = 0; i < n; i++) {
            scanf("%d", &x);
            res = res ^ x;
            if (x < menor) menor = x;
            soma = soma + x;
        }
        if (res != 0) {
            printf("Case #%d: NO\n", k+1);
        }
        else {
            printf("Case #%d: %d\n", k+1, soma - menor);
        }
    }
    return 0;
}
