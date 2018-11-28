#include <iostream>
#include <string>
#include <utility>
#include <vector>
#include <cstdlib>
using namespace std;

bool within_range(long long int x_, long long int y_, long long int x, long long int y, long long int d)
{
    return (x-x_)*(x-x_)+(y-y_)*(y-y_) <= d*d;
}

int sgn(int n)
{
    if (n < 0)
    {
        return -1;
    }
    if (n > 0)
    {
        return 1;
    }
    return 0;
}

bool check_valid(const vector<pair<int, int> >& all_points, int index, int x, int y)
{
    int n = all_points.size();
    int i;
    for (i = 0; i < n; i++)
    {
        if (i == index)
        {
            continue;
        }
        if (sgn(all_points[i].first-x) != sgn(all_points[index].first-x))
        {
            continue;
        }
        if (sgn(all_points[i].second-y) != sgn(all_points[index].second-y))
        {
            continue;
        }
        if (abs(all_points[i].first-x) > abs(all_points[index].first-x))
        {
            continue;
        }
        if (abs(all_points[i].second-y) > abs(all_points[index].second-y))
        {
            continue;
        }
        if (abs((all_points[i].first-x) * (all_points[index].second-y)) == abs((all_points[i].second-y) * (all_points[index].first-x)))
        {
            return false;
        }
    }
    return true;
}

int main()
{
    int t, T;
    int H, W;
    int D;
    long long int ans;
    int i, j;
    int x, y;
    int x_, y_;
    string s;
    vector<pair<int, int> > all_points;

    cin >> T;
    for (t = 1; t <= T; t++)
    {
        cin >> H >> W >> D;
        for (i = 0; i < H; i++)
        {
            cin >> s;
            for (j = 0; j < W; j++)
            {
                if (s[j] == 'X')
                {
                    x = j;
                    y = i;
                }
            }
        }
        // Re-scale
        x = 2 * (x - 1) + 1;
        y = 2 * (y - 1) + 1;
        H = 2 * (H - 2);
        W = 2 * (W - 2);
        D = 2 * D;
        ans = 0;
        all_points.clear();
        for (i = -100; i <= 100; i++)
        {
            for (j = -100; j <= 100; j++)
            {
                if (i == 0 && j == 0)
                {
                    continue;
                }
                if (i == 0 && j > 1)
                {
                    continue;
                }
                if (i == 0 && j < -1)
                {
                    continue;
                }
                if (j == 0 && i > 1)
                {
                    continue;
                }
                if (j == 0 && i < -1)
                {
                    continue;
                }
                // calculate x_, y_
                if (i % 2 == 0)
                {
                    x_ = i * W + x;
                }
                else
                {
                    x_ = i * W + (W - x);
                }
                if (j % 2 == 0)
                {
                    y_ = j * H + y;
                }
                else
                {
                    y_ = j * H + (H - y);
                }
                if (within_range(x, y, x_, y_, D))
                {
                    all_points.push_back(make_pair(x_, y_));
                }
            }
        }
        for (size_t s = 0; s < all_points.size(); s++)
        {
            ans += check_valid(all_points, s, x, y);
        }
        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}

