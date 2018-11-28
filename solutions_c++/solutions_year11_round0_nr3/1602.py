# include <iostream>
# include <cstdio>
# include <cstdlib>
# define INF 0x3f3f3f3f
using namespace std;

int main()
{
    int t, tt, i, n, ans, temp, sum, mini, a;

    cin >> t;
    tt = 1;
    while(t--) {
        cin >> n;

        mini = INF;
        ans = 0;
        for (i = 0; i < n; i++) {
            cin >> a;

            temp = (i == 0) ? a : temp ^ a;
            ans += a;
            mini = min(mini, a);
        }

        if (temp == 0) {
            printf("Case #%d: %d\n", tt++, ans - mini);
        }
        else {
            printf("Case #%d: NO\n", tt++);
        }
    }

    return 0;
}
