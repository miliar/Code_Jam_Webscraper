#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int tab[1005];
int ok[1005];

int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);

    int T, cases = 0;
    int N;
    int move;
    int temp;
    int cnt;

    scanf("%d", &T);
    while(cases++ < T)
    {
        move = 0;
        memset(tab, 0, sizeof(tab));
        memset(ok, 0, sizeof(ok));
        scanf("%d", &N);
        for (int i = 1; i <= N; i++)
        {
            scanf("%d", &tab[i]);
        }
        cnt = 0;
        for (int i = 1; i <= N; i++)
        {
            if (tab[i] == i || ok[i] != 0)
            {
                ok[i] = 1;
                continue;
            }
            else
            {
                temp = i;
                ok[i] = 1;
//                printf("%d ", i);
                cnt++;
                i = tab[i];
                while (ok[i] == 0)
                {
//                    printf("%d ", i);
                    ok[i] = 1;
                    i = tab[i];
                    cnt++;
                }
                move += cnt;
                cnt = 0;
                i = temp;
            }
        }
        printf("Case #%d: %.6f\n", cases, (double)move);
    }
    return 0;
}
