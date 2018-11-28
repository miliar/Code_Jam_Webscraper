#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int d;
vector <pair <long long ,long long > > l;
vector <long long > maxd;
int n;

bool Go()
{
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (l[j].first > l[i].first + maxd[i])
                break;

            maxd[j] = max(maxd[j], min(l[j].first - l[i].first, l[j].second));
        }
    }

    for (int i = 0; i < n; i++)
        if (l[i].first + maxd[i] >= d)
            return true;
    return false;
}

int main()
{
    freopen("inpu.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t = 0;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cout << "Case #" << i + 1 << ": ";
        cin >> n;
        l.resize(n);
        maxd.assign(n, 0);
        for (int j = 0; j < n; j++)
            cin >> l[j].first >> l[j].second;
        cin >> d;

        maxd[0] = l[0].first;
        if (Go())
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}
