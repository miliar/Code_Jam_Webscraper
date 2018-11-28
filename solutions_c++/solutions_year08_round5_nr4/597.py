#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

int h, w, r;
int x[10], y[10];
bool mask[10];
int inv[10007];

int c(int a, int b) {
    if (b < 0 || b > a) {
        return 0;
    }
    int p = b;
    int q = a - b;
    a %= 10007;
    p %= 10007;
    q %= 10007;
    if (p + q > a) {
        return 0;
    }
    int res = 1;
    for (int i = 1; i <= a; i ++) {
        res = (res * i) % 10007;
    }
    for (int i = 1; i <= p; i ++) {
        res = (res * inv[i]) % 10007;
    }
    for (int i = 1; i <= q; i ++) {
        res = (res * inv[i]) % 10007;
    }
    return res;
}

int comb(int a, int b) {
    if ((a + b) % 3 != 0) {
        return 0;
    }
    int x = (a + b) / 3;
    if ((a - b + x) % 2 != 0) {
        return 0;
    }
    int y = (a - b + x) / 2;
    return c(x, y);
}

int calc() {
    vector<pair<int, int> > points;
    points.push_back(pair<int, int>(1, 1));
    points.push_back(pair<int, int>(h, w));
    for (int i = 0; i < r; i ++) {
        if (mask[i] == true) {
            points.push_back(pair<int, int>(x[i], y[i]));
        }
    }
    sort(points.begin(), points.end());
    int res = 1;
    for (int i = 1; i < points.size(); i ++) {
        res = (res * comb(points[i].first - points[i - 1].first, points[i].second - points[i - 1].second)) % 10007;
    }
    return res;
}

int gen(int i, int mod) {
    i -= 1;
    int res = 0;
    if (i >= 0) {
        mask[i] = false;
        res += gen(i, mod);
        mod *= -1;
        mask[i] = true;
        res += gen(i, mod);
    } else {
        res = calc();
        if (mod == -1) {
            res = 10007 - res;
        }
    }
    return res % 10007;
}

void findinv() {
    for (int i = 1; i < 10007; i ++) {
        for (int j = 1; j < 10007; j ++) {
            if ((i * j) % 10007 == 1) {
                inv[i] = j;
                break;
            }
        }
    }
}

int main() {
    findinv();
    int n;
    scanf("%d", &n);
    for (int c = 1; c <= n; c ++) {
        scanf("%d %d %d", &h, &w, &r);
        for (int i = 0; i < r; i ++) {
            scanf("%d %d", x + i, y + i);
        }
        printf("Case #%d: %d\n", c, gen(r, 1));
    }
    return 0;
}
