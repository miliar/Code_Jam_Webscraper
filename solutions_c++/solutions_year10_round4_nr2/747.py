
#include <cstdio>
#include <cstring>

#define For(i, a, b) for (int i = a; i < b; i++)
#define PARENT(x) ((x)/2)
#define TEAM(x) (n + x)

int T;
int buy[1025];

static void solve(int t)
{
    int P;
    scanf("%d", &P);
    int n = 1 << P;

    memset(buy, 0, sizeof(buy));

    For(i, 0, n)
    {
        int M;
        scanf("%d", &M);
        int pos = TEAM(i);
        For(j, 0, M)
            pos = PARENT(pos);
        while (pos != 1)
        {
            pos = PARENT(pos);
            buy[pos] = 1;
        }
    }
    int unused;
    For(j, 1, n)
        scanf("%d", &unused);

    int r = 0;
    For(i, 1, n)
        r += buy[i];

    printf("Case #%d: %d\n", t, r);
}

int main()
{
    scanf("%d", &T);

    For(t, 0, T)
        solve(t+1);

    return 0;
}

