#include<iostream>
#include<iomanip>
#include<sstream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<cassert>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<cmath>
#include<cstdlib>

#define DEBUGLEVEL
#ifdef DEBUGLEVEL
#define printf_debug(fmt, args...) fprintf(stderr, fmt, ##args)
#else
#define printf_debug(fmt, args...)
#endif

typedef long long llong;

using namespace std;

int n;
llong w, l;

#define MAXN 1200
#define EPS 1e-10


struct circle {
    llong r;
    int id;
    double x, y;
    circle(){}  
};

bool cmp(circle a, circle b) {
    return a.r > b.r;
}

bool cmp_i(circle a, circle b) {
    return a.id > b.id;
}

circle c[MAXN];

bool intersect(int a, int b) {
    return (pow(c[a].x - c[b].x, 2) + pow(c[a].y - c[b].y, 2) < pow(c[a].r + c[b].r, 2));
}

double get_rand_coord(int a, int b) {
    return a + rand() % (b - a + 1);
}

void solve() {
    cin >> n >> w >> l;
    for(int i = 0; i < n; i++) {
        cin >> c[i].r;
        c[i].id = i;
    }
    sort(c, c + n, cmp);
    c[0].x = 0, c[0].y = 0;
    if(n > 1) {
        c[1].x = 0, c[1].y = l;
    }
    if(n > 2) {
        c[2].x = w, c[2].y = l;
    }
    if(n > 3) {
        c[3].x = w, c[3].y = 0;
    }
    int mx = 4;
    while(mx < n) {
        for(int i = 4; i < n; i++) {
            mx = max(mx, i + 1); 
            int steps = 1000;
            while(steps--) {   
                c[i].x = get_rand_coord(0, w);
                c[i].y = get_rand_coord(0, l);
                bool good = true;
                for(int j = 0; j < i; j++) {
                    if(intersect(i, j)) {
                        good = false;
                        break;
                    }
                }
                if(good) break;
            }
        }
    }
    sort(c, c + n, cmp);
    for(int i = 0; i < n; i++) {
        cout << fixed << setprecision(4) << " " << c[i].x << " " << c[i].y;
    }
    cout << endl;
}

int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        cout << "Case #" << t << ":";
        solve();
    }
    return 0;
}
