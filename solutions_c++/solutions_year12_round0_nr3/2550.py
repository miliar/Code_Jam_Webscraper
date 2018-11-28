#include<stdio.h>
#include<stdlib.h>
int main () {
    int t;
    int v[20], lista[20];
    int a, b, res;
    scanf("%d", &t);
    for (int lo = 1; lo <= t; lo++) {
        res = 0;
        scanf("%d %d", &a, &b);
        for (int c = a; c <= b; c++) {
            int p = 1;
            int cnt = 1;
            int used = 0;
            while (p <= c) {
                p = p*10;
                cnt++;
            }
            p = p/10;
            cnt--;
            int help = p;
            int aux = c;
            for (int k = 1; k <= cnt; k++) {
                v[k] = aux/p;
                aux = aux-(aux/p)*p;
                p = p/10;
            }
            aux = c;
            p = 10;
            int m;
            int esq = v[1];
            for (int k = 1; k < cnt; k++) {
                aux = aux- (aux/help)*help;
                m = aux*p;
                help = help/10;
                p = p*10;
                if (v[k+1] == 0) {
                    esq = esq*10+v[k+1];
                    continue;
                }
                if (esq+m > c && esq+m <= b) {
                    bool aux = true;
                    for (int i = 1; i <= used; i++) {
                        if (lista[i] == esq+m) {
                            aux = false;
                            break;
                        }
                    }
                    if (aux) {
                        res++;
                        lista[++used] = esq+m;
                    }
                }
                esq = esq*10+v[k+1];
                
            }
        }
        printf("Case #%d: %d\n", lo, res);
    }
    return 0;
}
                    
                    
                
                
            
                
