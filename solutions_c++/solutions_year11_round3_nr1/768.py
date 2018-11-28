#include <cstdio>

int R, S;
char tabla[51][51];

bool solve() {
    for (int r = 0; r < R; ++r) {
        for (int s = 0; s < S; ++s) {
            if (tabla[r][s] == '#') {
                if (r+1 >= R) return false;
                if (s+1 >= S) return false;
                if (tabla[r+1][s] != '#') return false;
                if (tabla[r][s+1] != '#') return false;
                if (tabla[r+1][s+1] != '#') return false;

                tabla[r][s] = '/';
                tabla[r][s+1] = '\\';
                tabla[r+1][s] = '\\';
                tabla[r+1][s+1] = '/';
            }
        }
    }
return true;
}

int main(void) {
 int test; scanf("%d", &test);

 for (int cs = 0; cs < test; ++cs) {
     scanf("%d%d", &R, &S);
     for (int i = 0; i < R; ++i) {
        scanf("%s", tabla[i]);
     }

     bool ok = solve();

     printf("Case #%d:\n", cs+1);
     if (!ok) puts("Impossible");
     else {
        for (int i = 0; i < R; ++i) puts(tabla[i]);
     }
 }

 return 0;
}
