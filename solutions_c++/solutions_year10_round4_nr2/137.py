#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

#define f0(i, n) for(int i = 0; i < (n); i++)
#define f1(i, n) for(int i = 1; i <= (n); i++)

int mic[12][1100][12];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    f1(ti, tc)
    {
        printf("Case #%d: ", ti);
        int p;
        scanf("%d", &p);
        int n = (1<<p);
        for(int q = 0; q <= p; q++)
            for(int i = 0; i < n; i++)
                for(int j = 0; j <= p; j++)
                    mic[q][i][j] = 1000000000;

        f0(i, n)
        {
            int x;
            scanf("%d", &x);
            mic[0][i][x] = 0;
        }
        for(int q = 1; q <= p; q++)
        {
            n/=2;
            for(int i = 0; i < n; i++)
            {
                int c;
                scanf("%d", &c);
                for(int j = 0; j <= p; j++)
                    for(int k = 0; k <= p; k++)
                    {
                        if(mic[q][i][min(j,k)] > mic[q-1][2*i][j]+mic[q-1][2*i+1][k]+c)
                            mic[q][i][min(j,k)] = mic[q-1][2*i][j]+mic[q-1][2*i+1][k]+c;
                    }
                for(int j = 1; j <= p; j++)
                    for(int k = 1; k <= p; k++)
                    {
                        if(mic[q][i][min(j,k)-1] > mic[q-1][2*i][j]+mic[q-1][2*i+1][k])
                            mic[q][i][min(j,k)-1] = mic[q-1][2*i][j]+mic[q-1][2*i+1][k];
                    }
            }
        }
        int ans = 1000000000;
        for(int i = 0; i <= p; i++)
            if(ans > mic[p][0][i])
                ans = mic[p][0][i];
        printf("%d\n", ans);
    }
}
