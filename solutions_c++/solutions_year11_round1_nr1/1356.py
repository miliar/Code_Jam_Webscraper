#include <cstdio>
#include <iostream>
using namespace std;
#define de2(a,b) cout << #a << ':' << (a) << ' ' << #b << ':' << (b) << endl
#define For(i,x) for (int i=0; i<(int)(x); i++)

void calc(int n, int pd, int pg) {
    // calc d

    for (int d = n; d > 0; d--) {
        // Pd = win/d * 100
        // Pd*d/100 = win

        if ((pd*d)%100 == 0) {
            int win = pd*d/100;
            //de2(win, d);

            int nume = pg;
            int deno = 100;

            if (win>0) {
                if (pg == 0) continue;
            }
                

            if (win<d) {
                if (pg == 100) continue;
                if (nume < deno) {
                    puts("Possible");
                    return;
                }
            }
            if (win==d) {
                puts("Possible");
                return;
            }
        }
    }

    puts("Broken");
}

int main() {
    int ncases;
    scanf("%d", &ncases);

    For(cc, ncases) {
        int n, pd, pg;
        scanf("%d %d %d", &n, &pd, &pg);

        printf("Case #%d: ", cc+1);
        calc(n, pd, pg);
    }
}
