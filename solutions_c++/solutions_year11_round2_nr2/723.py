#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <iomanip>

using namespace std;

    vector<long long> x_old(1000000);
    vector<long long> x_new(1000000);
    long long d;


bool is_valid(long long cur)
{
    x_new[0] = x_old[0] - cur;
    for (int i = 1; i < x_new.size(); ++i)
    {
        long long to = x_new[i-1] + d;
        long long dx = to - x_old[i];
        if (labs(dx) <= cur)
        {
            x_new[i] = to;
        }
        else
        {
            if (dx < 0)
                x_new[i] = x_old[i] - cur;
            else
                x_new[i] = x_old[i] + cur;
        }
        if (x_new[i] - x_new[i-1] < d)
            return false;
    }
    return true;
}

int main()
{
    freopen("input.txt", "r", stdin);

    freopen("output.txt", "w", stdout);
    int test_n;
    cin >> test_n;
    for (int test_i = 1; test_i <= test_n; ++test_i)
    {
        x_old.resize(0);
        x_new.resize(0);
        int c;
        int total = 0;
        cin >> c >> d;
        d *= 2;
        for (int i = 0; i < c; ++i)
        {
            long long p, v;
            cin >> p >> v;
            for (int j = 0; j < v; ++j)
            {
                x_old.push_back(2 * p);
            }
        }
        x_new.resize(x_old.size());
        long long l = 0;
        long long r = 1000000000000000ll;
        while (r - l > 1)
        {
            long long m = (l + r) / 2;
            if (is_valid(m))
                r = m;
            else
                l = m;
        }
        cout << "Case #" << test_i << ": ";
        if (is_valid(l))
        {
            cout << fixed << setprecision(6) << 0.5 * l << endl; 
        }
        else
        {
            cout << fixed << setprecision(6) << 0.5 * r << endl;
        }

    }
    return 0;
}