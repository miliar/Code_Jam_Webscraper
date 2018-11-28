#include <cstdio>

int S;

void troca(int * x, int * y)
{
    int aux = *x;
    *x = *y;
    *y = aux;
}

int verifica(int x1, int x2, int x3)
{
    if (x1-x2 >2) return false;
    if (x1-x3 >2) return false;
    if (x2 < 0) return false;
    return true;
}

bool solve(int n, int s)
{
    int x1 = s/3;
    int x2 = (s-x1)/2;
    int x3 = s-x1-x2;
    //printf("s: %d\nys: %d %d %d\n", s, x1, x2, x3);
    if (x1 >= n || x2 >= n || x3 >= n)
        return true;
    if (x1 < x2) troca(&x1, &x2);
    if (x1 < x3) troca(&x1, &x3);
    if (x2 < x3) troca(&x3, &x2);
    x1++;
    x2--;
    //printf("ns: %d %d %d\n", x1, x2, x3);
    if (x1 >= n && verifica(x1, x2, x3) && S)
    {
        S--;
        return true;
    }
    return false;
}

/*
bool try2(int n, int s)
{
    int x1 = s/3;
    int x2 = (s-x1)/2;
    int x3 = s-x1-x2;

    x2
}*/

int main()
{
    int T;
    scanf("%d", &T);
    for (int c = 0; c < T; c++)
    {
        int N, p, s, res = 0;
        scanf("%d %d %d", &N, &S, &p);
        //printf("p: %d s: %d\n", p, S);
        for (int i = 0; i < N; i++)
        {
            scanf("%d", &s);
            if (solve(p, s)) res++;
        }
        printf("Case #%d: %d\n", c+1, res);
    }
    return 0;
}   