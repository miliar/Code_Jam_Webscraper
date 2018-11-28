#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>
using namespace std;

struct level
{
    bool small_done;
    bool big_done;
    int small;
    int big;
    level(int s, int b)
    {
        small = s;
        big = b;
        small_done = false;
        big_done = false;
    }
};

bool by_2stars(const level& a, const level& b)
{
    return a.big < b.big;
}

int main()
{
    int t, T;
    int N;
    int i;
    vector<level> levels;
    int a, b;
    int stars;
    int ans;
    int stars_before;

    cin >> T;
    for (t = 1; t <= T; t++)
    {
        cin >> N;
        stars = 0;
        ans = 0;
        levels.clear();
        for (i = 0; i < N; i++)
        {
            cin >> a >> b;
            levels.push_back(level(a, b));
        }

        // sort by the 2stars requirement
        sort(levels.begin(), levels.end(), by_2stars);

        while (true)
        {
            stars_before = stars;
            for (i = 0; i < N; i++)
            {
                if (stars >= levels[i].big)
                {
                    ans += (!levels[i].small_done || !levels[i].big_done);
                    stars += !levels[i].small_done + !levels[i].big_done;
                    levels[i].small_done = true;
                    levels[i].big_done = true;
                }
            }
            for (i = N - 1; i >= 0; i--)
            {
                if (!levels[i].small_done && stars >= levels[i].small)
                {
                    ans++;
                    levels[i].small_done = true;
                    stars++;
                    break;
                }
            }
            if (stars == 2 * N)
            {
                cout << "Case #" << t << ": " << ans << endl;
                break;
            }
            if (stars == stars_before)
            {
                cout << "Case #" << t << ": Too Bad" << endl;
                break;
            }
        }
    }

    return 0;
}

