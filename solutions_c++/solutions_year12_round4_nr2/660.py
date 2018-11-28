#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <cstdlib>

using namespace std;

const double eps = 0.000000001;
const int magic_const = 4;

const int dx[8] = {0, 0, 1, -1, 1, -1, 1, -1};
const int dy[8] = {1, -1, 0, 0, 1, -1, -1, 1};


int n, w, l;
vector <int> a;
vector <pair <long long , long long > > ans;

double Dist(pair <long long , long long > a, pair<long long, long long> b)
{
    return sqrt((a.first - b.first) * (a.first - b.first) + (a.second - b.second) * (a.second - b.second));
}

bool check(pair<long long, long long> point )
{
    return point.first >= 0 && point.first <= w && point.second >=0 && point.second <= l;
}

bool F(int r, pair<long long, long long> point, int size)
{
    if (!check(point))
        return false;
    for (int i = 0; i < size; i++)
    {
        double dist = Dist(point, ans[i]);
        if (dist + eps < a[i] + r)
            return false;
    }
    return true;
}

bool Go(int num)
{
    if (num >= n)
        return true;

    for (int i = 0; i < num; i++)
    {
        int R = a[i] + a[num];
        for (int j = 0; j < 8; j++)
            if (F(a[num], make_pair(ans[i].first + dx[j] * R,
                                    ans[i].second + dy[j] * R), num))
            {
                ans[num] = make_pair(ans[i].first + dx[j] * R,
                                    ans[i].second + dy[j] * R);
                if (Go(num + 1)) return true;
            }
    }
    return false;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t = 0;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cout << "Case #" << i + 1 << ": ";
        cin >> n >> w >> l;
        a.resize(n);
        ans.resize(n);
        for (int j = 0; j < n; j++)
            cin >> a[j];

        ans[0] = make_pair(0, 0);
        while(!Go(1));

        for (int j = 0; j < ans.size(); j++)
            cout << ans[j].first << ' ' << ans[j].second << ' ';
        cout << endl;
    }
    return 0;
}
