#include <iostream>
#include <ctime>
#include <cstdlib>
#include <algorithm>
#include <cmath>
using namespace std;

#define MAXN 1024
#define SQ(x) ( (x)*(x) )
#define MAX 1000000

typedef unsigned long long tint;

tint getnum(tint MOD) {
    return (((tint)rand())^(((tint)rand())<<15))%MOD;
}

struct circle {
    int pos;
    tint r, x, y;
} n[MAXN];

bool compare(const circle &a, const circle &b) {
    return a.r > b.r;
}

bool compare2(const circle &a, const circle &b) {
    return a.pos < b.pos;
}

tint N, X, Y;

bool position() {
    int i, j, COUNT;

    for (i=0; i<N; i++) {
        COUNT  = 0;
        while (COUNT++ < MAX) {
            n[i].x = getnum(X);
            n[i].y = getnum(Y);
            for (j=0; j<i; j++) {
                if (SQ(n[i].x-n[j].x) + SQ(n[i].y-n[j].y) < SQ(n[i].r+n[j].r)) break;
            }
            if (j == i) break;
        }
        if (COUNT == MAX) return false;
    }
    return true;
}

int main() {
    int i, t, T;
    srand(time(0));

    cin >> T;
    for (t=1; t<=T; t++) {
        cin >> N;
        cin >> X;
        cin >> Y;
        for (i=0; i<N; i++) {
            n[i].pos = i;
            cin >> n[i].r;
        }

        sort(n, n+N, compare);
        while (!position());
        sort(n, n+N, compare2);
//        cout << "Graphics[{Line[{{0, 0}, {0, " << Y << "}, {" << X << ", " << Y << "}, {" << X << ", 0}, {0, 0}}], ";
//        for (i=0; i<N; i++) cout << "Circle[{" << n[i].x << ", " << n[i].y << "}, " << n[i].r << "], "; cout << "}]" << endl << endl;
        cout << "Case #" << t << ":";
        for (i=0; i<N; i++) cout << ' ' << n[i].x << ' ' << n[i].y; cout << endl;
    }

    return 0;
}
