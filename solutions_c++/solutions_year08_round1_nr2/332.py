#include <algorithm>
#include <iostream>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <cctype>
#include <queue>
#include <cmath>
#include <list>
#include <set>
#include <map>
using namespace std;

int m, n;
vector <int> res;
vector <int> f[25][2];
int cnt[200];

void dfs(int depth, int stat)
{
    if (depth > n)
    {
        for (int i=0;i<m;i++)
            if (cnt[i] == 0)
                return;
        res.push_back(stat);
        return;
    }
    for (size_t i=0;i<f[depth][0].size();i++)
        cnt[f[depth][0][i]]++;
    dfs(depth + 1, stat << 1);
    for (size_t i=0;i<f[depth][0].size();i++)
        cnt[f[depth][0][i]]--;

    for (size_t i=0;i<f[depth][1].size();i++)
        cnt[f[depth][1][i]]++;
    dfs(depth + 1, (stat << 1) + 1);
    for (size_t i=0;i<f[depth][1].size();i++)
        cnt[f[depth][1][i]]--;
}

inline int calc(int n)
{
    int ret = 0;
    while (n > 0)
    {
        ret += n & 1;
        n >>= 1;
    }
    return ret;
}

inline bool cmp1(int a, int b)
{
    return calc(a) < calc(b);
}

inline void prt(int stat, int k)
{
    if (k == n) return;
    prt(stat >> 1, k + 1);
    if (k < n - 1) printf(" ");
    printf("%d", stat & 1);
}

int main()
{
    int tt;
    cin >> tt;
    for (int i=0;i<tt;i++)
    {
        for (int i=0;i<25;i++)
        {
            f[i][0].clear();
            f[i][1].clear();
        }
        memset(cnt, 0, sizeof(cnt));
        cin >> n >> m;
        for (int i=0;i<m;i++)
        {
            int t;
            cin >> t;
            for (int j=0;j<t;j++)
            {
                int a, b;
                cin >> a >> b;
                f[a][b].push_back(i);
            }
        }
        res.clear();
        dfs(1, 0);
        sort(res.begin(), res.end(), cmp1);
        printf("Case #%d: ", i + 1);
        if (res.empty()) printf("IMPOSSIBLE\n");
        else
        {
            int stat = res[0];
            //printf("stat = %d, ", stat);
            prt(stat, 0);
            printf("\n");
        }
    }
	return 0;
}