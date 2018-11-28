#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

#define mul2(x) ((x) + (x))

double solve0(const vector<int>& dis)
{
    double ans = 0;
    for (int i = 0; i < dis.size(); i++)
    {
        ans += mul2(dis[i]);
    }

    return ans;
}

double solve1(const vector<int>& dis, int T)
{
    int n = dis.size();
    double ans = DBL_MAX;
    
    for (int loc = 0; loc < n; loc++)
    {
        double val = 0;
        bool bOK = true;
        for (int i = 0; i < n; i++)
        {
            if (i == loc)
            {
                double sub = T - val;
                if (mul2(dis[i]) <= sub)
                {
                    val += mul2(dis[i]);
                }
                else if (sub <= 0)
                {
                    val += dis[i];
                }
                else
                {
                    val += sub + (dis[i] - 0.5 * sub);
                }
            }
            else
            {
                val += mul2(dis[i]);
            }

            if (val >= ans)
            {
                bOK = false;
                break;
            }
        }

        if (val < ans && bOK)
        {
            ans = val;
        }
    }

    return ans;
}

double solve2(const vector<int>& dis, int T, const vector<int>& sum)
{
    int n = dis.size();
    double ans = DBL_MAX;

    for (int pos0 = 0; pos0 < n; pos0++)
    {
        for (int pos1 = pos0 + 1; pos1 < n; pos1++)
        {
            double val = 0;

            val += mul2(sum[pos0]);
            
            double sub = T - val;
            if (sub <= 0)
            {
                val += dis[pos0];
            }
            else if (mul2(dis[pos0]) <= sub)
            {
                val += mul2(dis[pos0]);
            }
            else
            {
                val += sub + (dis[pos0] - 0.5 * sub);
            }

            val += mul2(sum[pos1] - sum[pos0 + 1]);

            sub = T - val;
            if (sub <= 0)
            {
                val += dis[pos1];
            }
            else if (mul2(dis[pos1]) <= sub)
            {
                val += mul2(dis[pos1]);
            }
            else
            {
                val += sub + (dis[pos1] - 0.5 * sub);
            }

            val += mul2(sum[n] - sum[pos1 + 1]);

            if (val < ans)
            {
                ans = val;
            }
        }
    }

    return ans;
}

void solve()
{
    int caseNum;
    scanf("%d", &caseNum);

    for (int caseId = 1; caseId <= caseNum; caseId++)
    {
        printf("Case #%d:", caseId);

        int L, T, N, C;
        scanf("%d %d %d %d", &L, &T, &N, &C);
        
        vector<int> a(C);
        for (int i = 0; i < C; i++)
        {
            scanf("%d", &a[i]);
        }

        vector<int> dis(N);
        for (int i = 0; i < N; i++)
        {
            dis[i] = a[i % C];
        }

        vector<int> sum(N + 1);
        sum[0] = 0;
        for (int i = 1; i <= N; i++)
        {
            sum[i] = sum[i - 1] + dis[i - 1];
        }

        double ans = 0;
        switch (L)
        {
        case 0:
            {
                ans = solve0(dis);
                break;
            }

        case 1:
            {
                double a0 = solve0(dis);
                double a1 = solve1(dis, T);
                ans = min(a0, a1);
                break;
            }

        case 2:
            {
                double a0 = solve0(dis);
                double a1 = solve1(dis, T);
                double a2 = solve2(dis, T, sum);
                ans = min(a0, a1);
                ans = min(ans, a2);
                break;
            }
        }

        printf(" %.0lf\n", ans);
    }
}

int main()
{
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);

    solve();

    return 0;
}