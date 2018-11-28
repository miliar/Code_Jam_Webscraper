#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;


    int b[1001], e[1001], w[1001], order[1001];
        int x, s, r, t, n;


double f(int i)
{
    return (double)(r - s) / (w[i] + s);
}

bool cmp(int a, int b)
{
    return w[a] < w[b];
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for (int TT = 1; TT <= T; ++TT)
    {
        cin >> x >> s >> r >> t >> n;
        int walk = x;
        for (int i = 0; i < n; ++i)
        {
            order[i] = i;
            scanf("%d %d %d", &b[i], &e[i], &w[i]);
            walk -= (e[i] - b[i]);
        }
        b[n] = 0;
        e[n] = walk;
        w[n] = 0;
        order[n] = n;
        sort(order, order + n + 1, cmp);
        double left = t;
        double ans = 0;
        for (int j = 0; j < n + 1; ++j)
        {
            int i = order[j];
            if (fabs(left) < 1e-6)
            {
                ans += (double)(e[i] - b[i])/(s + w[i]);
            }
            else
            {
                double tmp = (double)(e[i] - b[i]) / (r + w[i]);
                if (left > tmp)
                {
                    ans += tmp;
                    left -= tmp;
                }
                else
                {
                    ans += left + (double)(e[i]-b[i] - left*(r + w[i])) / (s + w[i]); 
                    left = 0;
                }
            }
        }
       printf("Case #%d: %.7lf\n", TT, ans);
    }

    return 0;
}