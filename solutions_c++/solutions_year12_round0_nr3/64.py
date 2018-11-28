#include <cstdio>

#define MAXN 2000100
#define MAXE 20000000
struct node
{
    int value;
    int next;
} e[MAXE];
int start[MAXN];
int efree;
int pw[9];

void add(int x, int y)
{
    int t = start[x];
    while (t)
    {
        if (e[t].value == y) return;
        t = e[t].next;
    }

    efree++;
    e[efree].value = y;
    e[efree].next = start[x];
    start[x] = efree;

}

int main()
{
    int tc;
    int a, b, t, ans;

    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    pw[0] = 1;
    for(int i=1; i<9; ++i) pw[i] = pw[i - 1] * 10;

    for(int i=1; i<MAXN; ++i)
    {
        //if (i % 1000 == 0) printf("%i %i\n", i, efree);
        int len = 0;
        t = i;
        while (t)
        {
            len++;
            t /= 10;
        }

        for(int j=1; j<len; ++j)
        {
            t = (i / pw[j]) + (i % pw[j]) * pw[len - j];
            //if (i < 50) printf("i=%i j=%i t=%i\n", i, j, t);
            if (t > i) add(i, t);
        }
    }
    //printf("efree = %i\n", efree);

    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt)
    {
        scanf("%i %i", &a, &b);
        ans = 0;
        for(int i=a; i<b; ++i)
        {
            t = start[i];
            while (t)
            {
                if (e[t].value <= b) 
                {
                    //printf("%i %i\n", i, e[t].value);
                    ans++;
                }
                t = e[t].next;
            }
        }
        printf("Case #%i: %i\n", tt, ans);       
    }
    return 0;
}