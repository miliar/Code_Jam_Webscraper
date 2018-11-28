#include <cstdio>

struct X
{
    int pos;
    int t;
};

X x[1000];

int dif(int a, int b)
{
    if (a >= b)
        return a-b;
    return b-a;
}

int MAX(int a, int b)
{
    if (a >= b)
        return a;
    return b;
}

int solve()
{
    int n;
    int l[2] = {0,1};
    
    x[0].pos = x[1].pos = 1;
    x[0].t = x[1].t = 0;
    
    scanf("%d", &n);
    int i;
    for (i = 2; i < n+2; i++)
    {
        char c;
        scanf(" %c%d", &c, &x[i].pos);
        if (c == 'O')
        {
            x[i].t = MAX(x[l[0]].t + dif(x[l[0]].pos, x[i].pos)+1, x[l[1]].t+1);
            l[0] = i;
        }
        else
        {
            x[i].t = MAX(x[l[1]].t + dif(x[l[1]].pos, x[i].pos)+1, x[l[0]].t+1);
            l[1] = i;
        }
        //printf(":%d ", x[i].t);
    }
    return x[n+1].t;
}

int main()
{
    int T;
    scanf("%d", &T);
    
    for (int t = 1; t <= T; t++)
        printf("Case #%d: %d\n", t, solve());
        
    return 0;
}

