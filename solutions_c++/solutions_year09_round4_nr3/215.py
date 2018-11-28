#include <cstdio>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <cstdlib>
#include <cstring>
#include <map>
#include <set>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

int n, m;
int price[128][32];
int rel[128][128];
int deg[256];
int adj[256][256];
int match[256];
int used[256];

bool search(int idx)
{
    for (int i = 0; i < deg[idx]; i++)
    {
        int candidate = adj[idx][i];
        if (match[candidate] == -1)
        {
            match[candidate] = idx;
            return true;
        }
        if (used[candidate])
        {
            continue;
        }
        used[candidate] = 1;
        if (search(match[candidate]))
        {
            match[candidate] = idx;
            return true;
        }
    }
    return false;
}

int main()
{
    int tc;
    scanf("%d", &tc);
    for (int nc = 1; nc <= tc; nc++)
    {
        printf("Case #%d: ", nc);
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                scanf("%d", &price[i][j]);
            }
        }
        memset(rel, 0, sizeof(rel));
        for (int i = 0; i < n; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                char large = 1, small = 1;
                for (int k = 0; k < m; k++)
                {
                    if (price[i][k] <= price[j][k])
                    {
                        large = 0;
                    }
                    if (price[i][k] >= price[j][k])
                    {
                        small = 0;
                    }
                }
                if (large)
                {
                    rel[i][j] = 1;
                }
                if (small)
                {
                    rel[j][i] = 1;
                }
            }
        }
        memset(deg, 0, sizeof(deg));
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (rel[i][j])
                {
                    adj[i][deg[i]++] = j + n;
                }
            }
        }
        memset(match, -1, sizeof(match));
        int mm = 0;
        for (int i = 0; i < n; i++)
        {
            memset(used, 0, sizeof(used));
            if (search(i))
            {
                mm++;
            }
        }
        printf("%d\n", n - mm);
    }
    return 0;
}
