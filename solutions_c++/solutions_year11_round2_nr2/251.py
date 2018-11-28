#include <algorithm>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
#include <cstdio>
using namespace std;

int main()
{
    int T, t;
    int C, D;
    int P, V;
    int i;
    double ans;
    double hi, lo;
    int total_hotdog_stand;
    vector<pair<int, int> > hotdog_stands; // location, number
    bool ok;
    double leftmost;
    int current_hotdog_stand;
    int remaining;

    cin >> T;
    for (t = 1; t <= T; t++)
    {
        cin >> C >> D;
        hotdog_stands.clear();
        hotdog_stands.resize(C);
        total_hotdog_stand = 0;
        for (i = 0; i < C; i++)
        {
            cin >> P >> V;
            hotdog_stands[i] = make_pair(P, V);
            total_hotdog_stand += V;
        }
        lo = 0.0;
        hi = (double) D * total_hotdog_stand;
        ans = 0.0;
        hotdog_stands[0].second -= 1;
        while (hi - lo > 1e-7)
        {
            ans = (lo + hi) / 2;
            ok = true;
            leftmost = hotdog_stands[0].first - ans;
            current_hotdog_stand = 0;
            while (current_hotdog_stand < (int) hotdog_stands.size() && ok)
            {
                remaining = hotdog_stands[current_hotdog_stand].second;
                while (remaining > 0 && ok)
                {
                    if (hotdog_stands[current_hotdog_stand].first - leftmost >= D)
                    {
                        // move to left
                        leftmost = max(leftmost + D, hotdog_stands[current_hotdog_stand].first - ans);
                    }
                    else
                    {
                        // move to right
                        if (hotdog_stands[current_hotdog_stand].first + ans < leftmost + D)
                        {
                            ok = false;
                        }
                        else
                        {
                            leftmost += D;
                        }
                    }
                    remaining--;
                }
                current_hotdog_stand++;
            }
            if (ok)
            {
                hi = ans;
            }
            else
            {
                lo = ans;
            }
        }

        printf("Case #%d: %.9lf\n", t, ans);
    }

    return 0;
}

