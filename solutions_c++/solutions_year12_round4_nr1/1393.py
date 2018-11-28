#include <iostream>
#include <string>
#include <cstdio>
#include <deque>
#include <cmath>
#include <algorithm>
using namespace std;

const int MAXN = 10010;

int d[MAXN];
int l[MAXN];
int lineMax[MAXN];
int D;
int n;

bool run()
{
    memset(lineMax, 0, sizeof(lineMax));
    deque<pair<int, int> > que;

    que.push_back(make_pair(d[0], d[0]));
    lineMax[0] = d[0];
    while (!que.empty())
    {
        pair<int, int> cur = que.front();
        que.pop_front();
        // cout << "Reach " << cur.first << " " << cur.second << endl;

        int left = cur.first - cur.second;
        int right = cur.first + cur.second;

        if (D >= left && D <= right)
        {
            return true;
        }

        int pLeft = lower_bound(d, d + n, left) - d;

        for (int i = pLeft; i < n; i++)
        {
            if (d[i] > right)
            {
                break;
            }

            int dif = abs(d[i] - cur.first);
            int hold = min(dif, l[i]);
            if (hold > lineMax[i])
            {
                lineMax[i] = hold;
                que.push_back(make_pair(d[i], hold));
            }
        }
    }

    return false;
}

int main()
{
    int T;
    scanf("%d", &T);

    for (int t = 0; t < T; t++)
    {
        scanf("%d", &n);

        for (int i = 0; i < n; i++)
        {
            scanf("%d%d", &d[i], &l[i]);
        }

        scanf("%d", &D);

        printf("Case #%d: ", t + 1);
        if (run())
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }
    }
}
