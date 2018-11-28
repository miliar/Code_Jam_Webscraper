#include <cstdio>

using namespace std;

int t, a1, a2, b1, b2;

void solve();
int get_n_positions();
int gcd(int, int);
bool can_win(int, int);

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}

void solve() {
    scanf("%d%d%d%d", &a1, &a2, &b1, &b2);
    printf("Case #%d: %d\n", ++t, get_n_positions());
}

int get_n_positions() {
    int cnt = 0;
    for (int i = a1; i <= a2; ++i) {
        for (int j = b1; j <= b2; ++j) {
            int g = gcd(i, j);
            if (can_win(i / g, j / g))
                ++cnt;
        }
    }
    return cnt;
}

int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

bool can_win(int a, int b) {
    if (a >= b * 2 || b >= a * 2)
        return true;
    if (a < b)
        return !can_win(a, b - a);
    if (a > b)
        return !can_win(a - b, b);
    return false;
}
