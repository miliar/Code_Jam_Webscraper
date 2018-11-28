#include <cmath>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

typedef long long int64;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<int64> vl;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<int64, int64> pll;

bool div(int A, int N, int M)
{
    for (int x2 = 0; x2 <= N; x2++)
    {
    for (int y3 = 0; y3 <= M; y3++)
    {
    for (int x3 = 1; x3 <= N; x3++)
    {
        int y2 = x2 * y3 + A;
        if (y2 % x3 != 0) continue;
        y2 /= x3;
        if (y2 > M || y2 < 0) continue;
        printf("%d %d %d %d %d %d\n", 0, 0, x2, y2, x3, y3);
        return true;
    }
    }
    }
    return false;
}

void main()
{
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("B-small-attempt2.out", "w", stdout);

    int C;
    scanf("%d", &C);

    for (int i = 0; i < C; i++)
    {
        int N, M, A;
        scanf("%d%d%d", &N, &M, &A);
        printf("Case #%d: ", i + 1);

        if (N * M < A || !div(A, N, M))
        {
            printf("IMPOSSIBLE\n");
            continue;
        }
    }
}
