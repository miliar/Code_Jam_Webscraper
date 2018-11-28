#include <iostream>
#include <string>

using namespace std;

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B_small.out","w",stdout);

    int t, n, s, p, sum;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        cin >> n >> s >> p;
        int ans = 0;
        int usings = 0;

        if (p == 0)
        {
            for (int j = 0; j < n; ++j)
            {
                cin >> sum;

                if (sum >= 0)
                {
                    ++ans;
                }
            }
        }
        else if (p == 1)
        {
            for (int j = 0; j < n; ++j)
            {
                cin >> sum;
                if (sum > 0)
                {
                    ++ans;
                }
            }
        }
        else
        {
            int min = (p - 1) * 3;

            for (int j = 0; j < n; ++j)
            {
                cin >> sum;
                if (sum > min)
                {
                    ++ans;
                }
                else if (sum == min || sum == min - 1)
                {
                    if (usings < s)
                    {
                        ++usings;
                        ++ans;
                    }
                }
            }
        }

        cout << "Case #" << i << ": " << ans << endl;
    }

    return 0;

}