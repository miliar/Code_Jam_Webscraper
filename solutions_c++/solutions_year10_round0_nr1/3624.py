#include <stdio.h>
#include <math.h>

int verificar(long n, long k)
{
    int aux = 0;
    if(((k+1)%(long)(pow(2,n))) == 0) aux = 1;
    return aux;
}

int main()
{
    int T,i=0;
    long n,k;

    scanf("%d",&T);
    for(i=0; i<T; i++)
    {
        scanf("%d %d",&n,&k);
        printf("Case #%d: ",(i+1));
        (verificar(n,k)==1)?printf("ON\n"):printf("OFF\n");
    }
    return 0;
}

