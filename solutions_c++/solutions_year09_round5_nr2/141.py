#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

const int SIGMA = 26;
const int MOD = 10009;

int n, K;
char s[505];
char t[105][505];
int res[15];
int c1[2];
vector <int> c2[105];
vector <int> c[2][4000000];

inline int lowbit(int n)
{
    return n & -n;
}

inline void add(vector <int>& a, const vector <int>& b)
{
    for (int i = 0; i < SIGMA; i++)
        a[i] += b[i];
}

inline void add(vector <int>& a, const vector <int>& b, const vector <int>& c)
{
    for (int i = 0; i < SIGMA; i++)
        a[i] = b[i] + c[i];
}

int solve(const vector <int>& v, char* s)
{
    int len = strlen(s);
    int ret = 0;
    s[len] = '+';
    for (int i = 0, curr = 1; i <= len; i++)
    {
        if (s[i] == '+')
        {
            ret += curr;
            curr = 1;
        } else
        {
            curr = curr * v[s[i] - 'a'] % MOD;
        }
    }
    s[len] = '\0';
    ret = (ret % MOD + MOD) % MOD;
    return ret;
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        memset(res, 0, sizeof(res));
        scanf("%s%d%d", s, &K, &n);
        for (int i = 0; i < n; i++)
        {
            scanf("%s", t[i]);
            int len = strlen(t[i]);
            c[1][i] = vector <int>(SIGMA, 0);
            c2[i] = vector <int>(SIGMA, 0);
            for (int j = 0; j < len; j++)
                c[1][i][t[i][j] - 'a']++;
            for (int j = 0; j < SIGMA; j++)
                c2[i][j] = c[1][i][j];
            res[1] += solve(c[1][i], s);
        }
        c1[1] = n;
        for (int i = 1; i < K; i++)
        {
            int x = (i & 1);
            int y = 1 - x;
            c1[y] = 0;
            for (int j = 0; j < c1[x]; j++)
            {
                for (int k = 0; k < n; k++)
                {
                    c[y][c1[y]] = vector <int>(SIGMA, 0);
                    add(c[y][c1[y]], c[x][j], c2[k]);
                    int curr = solve(c[y][c1[y]], s);
                    if (i < K - 1)
                        c1[y]++;
//                    if (c1[y] > (1 << n))
//                        printf("i = %d, j = %d, k = %d\n", i, j, k);
                    res[i + 1] = (res[i + 1] + curr) % MOD;
                }
            }
        }
        printf("Case #%d:", cas);
        for (int i = 1; i <= K; i++)
            printf(" %d", res[i] % MOD);
        putchar('\n');
    }
    return 0;
}
