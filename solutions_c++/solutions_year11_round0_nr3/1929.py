#include <iostream>
#include <algorithm>

using namespace std;

int a[1005];
int s[1005];
int total;

unsigned int
add(unsigned int a, unsigned int b) {
    return (a ^ b) & ~(a & b);
}

bool isRight(int n) {
    int i, left, right;

    left = right = 0;

    for (i=0;i<n;++i) {
        if (s[i]) right = add(right, a[i]);
        else left = add(left, a[i]);
    }

    return (left == right);
}

int
solve(int n) {
    int     ans, i, j;

    sort(&a[0], &a[n]);
    ans = 0;
    for (i=1;i<n;++i) ans += a[i];
    return ans;
}

int main(void) {
    int     t, n, i, j, x, y;

    cin >> t;

    for (i=0;i<t;++i) {
        cin >> n;
        total = 0;
        for (j=0;j<n;++j) {
            cin >> a[j];
            total = add(total, a[j]);
        }
        if (total) {
            cout << "Case #" << (i+1) << ": NO" << endl;
        }
        else {
            cout << "Case #" << (i+1) << ": " << solve(n) << endl;
        }
    }

    return 0;
}
