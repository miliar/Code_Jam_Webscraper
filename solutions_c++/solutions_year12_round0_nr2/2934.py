#include <algorithm>
#include <cstdio>
#include <functional>
#include <iostream>
#include <vector>
using namespace std;
#define For(i,x) for (int i=0; i<(int)(x); i++)

typedef vector<int> vi;

bool isSuprising(int sum) {
    switch (sum) {
    case 0:
    case 1:
    case 29:
    case 30:
        return false;
    }
    return true;
}

int bestResult(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    if (n == 29) return 10;
    if (n == 30) return 10;
    return ((n-2) / 3) + 2;
}

void tri(int point, int best) {
    int c = best;
    int a = best-2;
    int b = point - (a + c);
    printf("%d %d %d = %d\n", a, b, c, point);
}

int calc(int s, int p, vi& v) {
/*
  0: 0 0 0 x
  1: 0 0 1 x
  2: 0 0 2 o
  3: 0 1 2
  4: 0 2 2
  5: 1 1 3
  6: 1 2 3
  7: 1 3 3
  8: 2 2 4

  28: 8 10 10 o
  29: 9 10 10 x
  30: 10 10 10 x
*/

    int ans = 0;
    int cnt = 0;
    sort(v.begin(), v.end());
    For(i, v.size()) {
        int best = bestResult(v[i]);
        //printf("best:%d issup:%d\n", best, isSuprising(v[i]));
        //tri(v[i], best);
        if (isSuprising(v[i])) {
            if (cnt >= s) {
                int c = best;
                int a = best - 2;
                int b = v[i] - (a + c);
                if (b != c) best--;
            }
                    
            if (best >= p) {
                ans++;
                cnt++;
            }
        }
        else {
            if (best >= p)
                ans++;
        }
    }
    return ans;
}

int main() {
    int ncases;
    scanf("%d", &ncases);

    For(cc, ncases) {
        int n, s, p;
        scanf("%d %d %d", &n, &s, &p);
        vi v(n);
        For(i, n) scanf("%d", &v[i]);

        printf("Case #%d: %d\n", cc+1, calc(s, p, v));
    }
}

