#include <cstdio>
#include <cstring>
#include <climits>
#include <algorithm>

using namespace std;

const int maxN = 11000;

int d[maxN];
int l[maxN];
int N;
int low[maxN];

int main()
{
    freopen("swing.in", "r", stdin);
    freopen("swing.out", "w", stdout);
    int Tcases;
    scanf("%d", &Tcases);
    for ( int cases = 0; cases < Tcases; cases++)
    {
        scanf("%d", &N);
        for ( int i = 0 ; i < N; i++)
        {
            scanf("%d %d", d + i, l + i);
        }

        int D;
        scanf("%d", &D);
        d[N] = D;
        l[N] = INT_MAX;
        ++N;
        low[0] = d[0] << 1;

        bool ans = true;
        int j = 0;
        for ( int i = 1; i < N && ans; i++)
        {
            while ( j < i && low[j] < d[i])
            {
                ++j;
            }
            if ( j == i)
            {
                ans = false;
            }
            else
            {
                int dis = d[i] - d[j];
                dis = min( dis, l[i]);
                low[i] = dis + d[i];
            }
            //printf("%d ", low[i]);
        }

        printf("Case #%d: %s\n", cases+1, ans ? "YES" : "NO");
    }

    return 0;
}
