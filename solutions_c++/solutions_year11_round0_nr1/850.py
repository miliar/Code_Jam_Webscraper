#include <iostream>
#include <algorithm>
using namespace std;

void solve(int CASE)
{
    int n;
    cin >> n;

    int p[2] = { 1, 1 };
    int t[2] = { 0, 0 };

    char c;
    int which;
    int where;

    for (int i = 0; i < n; i++)
    {
        //printf("Orange: %d at %d\nBlue  : %d at %d\n", p[0], t[0], p[1], t[1]);
        cin >> c >> where;
        which = (c == 'O' ? 0 : 1);
        //printf("%d goes to %d\n", which, where);

        int m = std::max(t[0], t[1]);

        int j = abs(where - p[which]) - (m - t[which]);
        //printf(">> (%d - %d) - (%d - %d) = %d\n", where, p[which], m, t[which], j);
        if (j < 0) j = 0;
        t[which] = m + j + 1;
        p[which] = where;
    }

    printf("Case #%d: %d\n", CASE, std::max(t[0], t[1]));
}

int main()
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++)
        solve(i);

    return 0;
}
