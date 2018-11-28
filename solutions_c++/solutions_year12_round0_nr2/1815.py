#include <cstdio>

int surprising[31];
int normal[31];

inline int
min(int x, int y)
{
    return x < y ? x : y;
}

void
init()
{
    for (int i = 0; i <= 30; i++)
    {
        int base = i / 3;
        int remainder = i - base * 3;
        if (remainder == 0)
        {
            if (base - 1 >= 0)
                surprising[i] = min(10, base + 1);
            else
                surprising[i] = base;
            normal[i] = base;
        }
        else if (remainder == 1)
        {
            surprising[i] = min(10, base + 1);
            normal[i] = base + 1;
        }
        else // if (remainder == 2)
        {
            surprising[i] = min(10, base + 2);
            normal[i] = base + 1;
        }
    }
}

void
print()
{
    for (int i = 0; i <= 30; i++)
        printf("%3d", i);
    printf("\n");
    for (int i = 0; i <= 30; i++)
        printf("%3d", surprising[i]);
    printf("\n");
    for (int i = 0; i <= 30; i++)
        printf("%3d", i);
    printf("\n");
    for (int i = 0; i <= 30; i++)
        printf("%3d", normal[i]);
    printf("\n");
}

int
main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    init();
//    print();

    int T;
    scanf("%d", &T);
    int score[100];
    for (int case_i = 1; case_i <= T; case_i++)
    {
        int N;
        int S;
        int P;
        scanf("%d %d %d", &N, &S, &P);
        for (int i = 0; i < N; i++)
            scanf("%d", &score[i]);

        int sur_cnt = 0;
        int nor_cnt = 0;
        for (int i = 0; i < N; i++)
        {
            if (surprising[ score[i] ] >= P)
                sur_cnt++;
            if (normal[ score[i] ] >= P)
                nor_cnt++;
        }

        int diff = sur_cnt - nor_cnt;
        int result = -1;
        if (S >= diff)
            result = sur_cnt;
        else
            result = nor_cnt + S;
        printf("Case #%d: %d\n", case_i, result);
    }

    return 0;
}
