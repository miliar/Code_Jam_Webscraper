#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int tt;
    cin >> tt;
    for (int t = 1; t <= tt; ++t)
    {
        int n, s, p;
        cin >> n >> s >> p;
        int res = 0;
        for (int i = 0; i != n; ++i)
        {
            int x;
            cin >> x;
            if (x >= p * 3 - 2)
                ++res;
            else if (p - 2 >= 0 && x >= p * 3 - 4 && s > 0)
            {
                --s;
                ++res;
            }
        }
        cout << "Case #" << t << ": " << res << endl;
    }

    return 0;
}
