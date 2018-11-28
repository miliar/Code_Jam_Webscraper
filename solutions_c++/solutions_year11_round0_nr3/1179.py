#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int candy[1006];

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    int T, cases = 0;
    int N;
    int temp;
    int value;
    int sean;

    scanf("%d", &T);
    while(cases++ < T)
    {
        value = 0; sean = 0;
        memset(candy, 0, sizeof(candy));
        scanf("%d", &N);
        for (int i = 0; i < N; i++)
        {
            scanf("%d", &temp);
            value ^= temp;
            candy[i] = temp;
        }
        if (value != 0)
        {
            printf("Case #%d: NO\n", cases);
        }
        else
        {
            sort(candy, candy + N);
            for (int i = 1; i < N; i++)
            {
                sean += candy[i];
            }
            printf("Case #%d: %d\n", cases, sean);
        }
    }
}
