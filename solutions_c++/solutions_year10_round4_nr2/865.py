#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cmath>
#include <cctype>
#define N 1024
using namespace std;

typedef pair<int, int>pii;
typedef long long I64;

int P, M, need[N];
int DFS(int l, int r);

int main()
{
    freopen("B-small.in", "r", stdin);
    freopen("B-small.out", "w", stdout);
    int C = 0, T;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d", &P);
        M = (1 << P);
        for(int i = 0; i < M; i++)
        {
            scanf("%d", &need[i]);
            need[i] = P - need[i];
        }
        for(int i = 1, j; i < M; i++)
            scanf("%d", &j);
        printf("Case #%d: %d\n", ++C, DFS(0, M));
    }
    return 0;
}

int DFS(int l, int r)
{
    if(l >= r)return 0;
    int i, res = 0;
    for(i = l; i < r; i++)
        if(need[i] > 0)break;
    if(i < r)
    {
        for(i = l; i < r; i++)
            if(need[i] > 0)need[i]--;
        res = 1 + DFS(l, (r + l) >> 1) + DFS((r + l) >> 1, r);
    }
    return res;
}
