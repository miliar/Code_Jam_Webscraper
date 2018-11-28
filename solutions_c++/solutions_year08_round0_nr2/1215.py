#include <cstdio>
#include <algorithm>

using namespace std;

#define READY_A 0
#define READY_B 1
#define DEPARTURE_A 2
#define DEPARTURE_B 3

#define REP(a, b) for(int a=0; a<(b); a++)

pair<int, int> tab[400];

int main() {
    int d;
    scanf("%d", &d);
    REP(z, d) {
        int need_a = 0, need_b = 0, cnt_a = 0, cnt_b = 0;
        int ile = 0;
        int T, NA, NB;
        scanf("%d %d %d", &T, &NA, &NB);
        REP(i, NA) {
            int a, b, c, d;
            scanf("%d:%d %d:%d", &a, &b, &c, &d);
            int dep = a*60+b, red = c*60+d+T;
            tab[ile++] = make_pair(dep, DEPARTURE_A);
            tab[ile++] = make_pair(red, READY_B);
        }
        REP(i, NB) {
            int a, b, c, d;
            scanf("%d:%d %d:%d", &a, &b, &c, &d);
            int dep = a*60+b, red = c*60+d+T;
            tab[ile++] = make_pair(dep, DEPARTURE_B);
            tab[ile++] = make_pair(red, READY_A);
        }
        sort(tab, tab+ile);
        REP(i, ile)
            switch(tab[i].second) {
                case READY_A:
                    cnt_a++;
                    break;
                case READY_B:
                    cnt_b++;
                    break;
                case DEPARTURE_A:
                    if (cnt_a==0)
                        need_a++;
                    else cnt_a--;
                    break;
                case DEPARTURE_B:
                    if (cnt_b==0)
                        need_b++;
                    else cnt_b--;
                    break;
            }
        printf("Case #%d: %d %d\n", z+1, need_a, need_b);
    }
    return 0;
}
