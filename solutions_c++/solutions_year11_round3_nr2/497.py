#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int arr[100000];
int dist[100000];
int value[10000];

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);

    int T;
    int cases = 1;

    scanf("%d", &T);

    int L, t, N, C;
    int total;
    int i, j;
    while (T-- > 0)
    {
        scanf("%d %d %d %d", &L, &t, &N, &C);

        for (i = 0; i < C; i++)
        {
            scanf("%d", &value[i]);
        }

        dist[0] = 0;

        for (i = 1; i <= N; i++)
        {
            dist[i] = dist[i - 1] + value[(i - 1) % C];
        }

        total = dist[N] * 2;
        int travel = t * 0.5;
        for (i = 1; i <= N; i++)
        {
            if (dist[i] > travel)
            {
                break;
            }
        }

        if (i > N)
        {
            printf("Case #%d: %d\n", cases++, total);
            continue;
        }
        arr[0] = dist[i] - travel;
        int start = i;
        j = 1;
        for (i = start; i < N; i++)
        {
            arr[j++] = dist[i + 1] - dist[i];
        }
        sort(arr, arr + j);

        j = j - 1;
        for (i = 0; i < L; i++)
        {
            if (j < 0)
            {
                break;
            }
            else
            {
                total -= arr[j--];
            }
        }
        printf("Case #%d: %d\n", cases++, total);
    }
    return 0;
}
