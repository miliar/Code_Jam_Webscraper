#include <stdio.h>
#include <string>
#include <algorithm>
using namespace std;

int T, c = 1;
int L, t, N, C;
int ai[1000010];
int dist[1000010];

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    for(scanf("%d", &T); T; --T)
    {
        int i, j;

        scanf("%d%d%d%d", &L, &t, &N, &C);
        for(i = 0; i < C; ++i)
            scanf("%d", ai + i);

        for(i = 0; i < N; ++i)
            dist[i] = ai[i % C];

        int noboost = t >> 1;
        int sum = 0;

        for(i = 0; i < N; ++i)
        {
            sum += dist[i];
            if(sum > noboost)
            {
                break;
            }
        }

        int ans = t;

        if(i == N)
            ans = sum << 1;
        else 
        {
            dist[i] = sum - noboost;
            sort(dist + i, dist + N);

            for(j = 0; j < L && (N - 1 - j) >= i; ++j)
                ans += dist[N - 1 - j];
            for(j = N - 1 - j; j >= i; --j)
                ans += dist[j] << 1;
        }

        printf("Case #%d: %d\n", c++, ans);
    }
}