#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T, n, s, p, a;
    cin >> T;

    for (int cs = 1; cs <= T; ++cs)
    {
        int result = 0, potential = 0;
        cin >> n >> s >> p;

        for (int i = 0; i < n; ++i)
        {
            cin >> a;
            switch (a % 3)
            {
            case 0:
                if (a / 3 >= p)
                    ++result;
                else if (a / 3 + 1 >= p)
                    if (a >= 2 && a <= 28)
                        ++potential;
                break;
            case 1:
                if (a / 3 + 1 >= p)
                    ++result;
                break;
            case 2:
                if (a / 3 + 1 >= p)
                    ++result;
                else if (a / 3 + 2 >= p)
                    if (a >= 2 && a <= 28)
                        ++potential;
            }
        }

        cout << "Case #" << cs << ": "
             << result + min(s, potential) << endl;
    }

    return 0;
}
