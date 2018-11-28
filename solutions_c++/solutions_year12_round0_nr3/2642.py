#include <cstdio>

int p10[8];
int A, B;

int g(int n, int l)
{
    int x, z = l-1;
    while((x = n%p10[z]) < p10[z-1])
    {
        z--;
        if(z == 0)
            return n;
    }
    return x*p10[l-z] + n/p10[z];
}

int f(int n, int l)
{
    int x = n, z = -1;
    do
    {
        x = g(x, l);
        z += n <= x && x <= B;
    }
    while(x != n);
    return z;
}

int v(int n)
{
    int i=0;
    for(; n >= p10[i]; i++);
    return i;
}

int main()
{
    for(int i=0, p=1; i<=7; i++, p*=10)
        p10[i] = p;
    int T;
    scanf("%d", &T);
    for(int t=1; t<=T; t++)
    {
        scanf("%d%d", &A, &B);
        int x=0;
        for(int i=A, j=v(A); i<B; i++, j+=i==p10[j+1])
            x+=f(i,j);
        printf("Case #%d: %d\n", t, x);
    }
    return 0;
}
