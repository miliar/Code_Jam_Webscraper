# include <iostream>
# include <cstdio>
# include <cstdlib>
using namespace std;

int main()
{
    int t, i, n, a, ans, tt, p[2], w[2];
    char c;

    cin >> t;
    tt = 1;
    while(t--) {
        cin >> n;

        ans = 0;
        p[0] = p[1] = 1;
        w[0] = w[1] = 0;
        while(n--) {
            cin >> c >> a;

            i = (c == 'O') ? 0 : 1;
            ans += max(0, abs(a - p[i]) - w[i]) + 1;
            w[(i == 0) ? 1 : 0] += max(0, abs(a - p[i]) - w[i]) + 1;
            p[i] = a;
            w[i] = 0;
        }

        printf("Case #%d: %d\n", tt++, ans);
    }

    return 0;
}

