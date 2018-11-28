
#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <vector>
#include <map>
#include <ctime>

using namespace std;

#define Rep(i,a,b) for(int i=a;i<b;++i)
#define Repd(i,a,b) for(int i=a,_b=b;i>_b;--i)

typedef long long ll;
const int N = 10005;

int n, xs, ys;
int r[N];
int x[N], y[N];

void print() {
    for (int i = 0; i < n; ++i) {
        if (i) putchar(' ');
        printf("%d %d", x[i], y[i]);
    }
    puts("");
}

int id[N];

bool ok() {
    int left = 0, right = ys;
    int cur = r[id[0]], maxv = r[id[0]];
    x[id[0]] = 0;
    y[id[0]] = 0;
    for (int i = 1; i < n; ++i) {
        if (cur + r[id[i]] <= xs) {
            x[id[i]] = cur + r[id[i]];
            y[id[i]] = left;
            cur += 2 * r[id[i]];
            maxv = max(maxv, r[id[i]]);
            //cout << cur << endl;
        } else {
            left += maxv;
            maxv = r[id[i]];
            left += maxv;
            x[id[i]] = 0;
            y[id[i]] = left;
            //cout << left << endl;
            cur = r[id[i]];
            if (left > right) return false;
        }
    }
}

bool ok2() { //cout <<" ~~" << endl;
    swap(xs, ys);
    for (int i = 0; i < n; ++i)
        swap(x[i], y[i]);
    swap(xs, ys);
}

bool cmp(const int a, const int b) {
    return r[a] > r[b];
}

int main() {
    int cas, tcas = 0;

    freopen("B-large.in", "r", stdin);
    freopen("out", "w", stdout);

    for (cin >> cas; cas; --cas) {
        printf("Case #%d: ", ++tcas);
        scanf("%d%d%d", &n, &xs, &ys);
        for (int i = 0; i < n; ++i) {
            scanf("%d", r + i);
            id[i] = i;
        }
        sort(id, id + n, cmp);

        if (ok() || ok2()) {
            print();
        } else {
            do {
                random_shuffle(id, id + n);
            } while (!(ok() || ok2()));
            print();
        }
    }
}