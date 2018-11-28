#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

#if 0
int color[10];
void dfs(int i, int* P, int c)
{
    color[i] = c;
    int j = P[i];
    if (color[j] == -1)
    {
        dfs(j, P, c);
    }
}

vector<int> split(int* P, int n)
{
    memset(color, -1, sizeof(color[0]) * n);

    int c = 0;
    for (int i = 0; i < n; i++)
    {
        if (color[i] == -1)
        {
            dfs(i, P, c);
            c++;
        }
    }
    static int cnt[10];
    memset(cnt, 0, sizeof(cnt));
    for (int i = 0; i < n; i++)
    {
        cnt[color[i]]++;
    }

    vector<int> r;
    for (int cc = 0; cc < c; cc++)
    {
        r.push_back(cnt[cc]);
    }
    sort(r.begin(), r.end());
    return r;
}

int fact[10];
double dp[10];
bool use[10];

double Dp(int n)
{
    if (use[n])
        return dp[n];

    use[n] = true;

    int P[n];
    for (int i = 0; i < n; i++)
    {
        P[i] = i;
    }

    int self = 0;
    double other = 0;
    do
    {
        vector<int> z = split(P, n);
        if (z.size() == 1)
            self++;
        else
        {
            int cnt = z.size();
            for (int i = 0; i < cnt; i++)
            {
                other += Dp(z[i]);
            }
        }
    } while (next_permutation(P, P + n));

    other /= (double) fact[n];
    double coeff = (1.0 - (double) self / (double) fact[n]);

    return dp[n] = (1.0 + other) / coeff;
}
#endif

int N;
int a[1000];
int color[1000];
int cnt[10000];

void dfs(int i, int c)
{
    color[i] = c;
    int j = a[i];
    if (color[j] == -1)
    {
        dfs(j, c);
    }
}

int main()
{
#if 0
    fact[0] = 1;
    for (int i = 1; i < 10; i++)
        fact[i] = i * fact[i - 1];

    use[0] = use[1] = true;
    
    for (int p = 1; p <= 9; p++)
    {
        printf("%lf\n", Dp(p));
    }
    return 0;
#endif

    int T;
    scanf("%d", &T);
    for (int tc = 0; tc < T; tc++)
    {
        printf("Case #%d: ", tc + 1);

        scanf("%d", &N);
        for (int i = 0; i < N; i++)
        {
            scanf("%d", &a[i]);
            a[i]--;
        }

        memset(color, -1, N * sizeof(color[0]));
        int c = 0;
        for (int i = 0; i < N; i++)
        {
            if (color[i] == -1)
            {
                dfs(i, c);
                c++;
            }
        }

        memset(cnt, 0, c * sizeof(cnt[0]));
        for (int i = 0; i < N; i++)
        {
            cnt[color[i]]++;
        }

        int ans = 0;
        for (int cc = 0; cc < c; cc++)
        {
            int x = cnt[cc];
            if (x == 1)
            {
                x = 0;
            }
            ans += x;
        }
        printf("%d\n", ans);
    }
    return 0;
}
