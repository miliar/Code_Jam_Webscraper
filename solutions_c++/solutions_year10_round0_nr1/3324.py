#include <cstdio>

#define max 32

long long pot[max];
int n,k,t,i;

void imprimeon()
{
    printf("Case #");
    printf("%d",i);
    printf(": ON\n");
}

void imprimeoff()
{
    printf("Case #");
    printf("%d",i);
    printf(": OFF\n");
}

void potencias()
{
    pot[0]=1;
    for (int j=1; j<=30; j++)
    {
        pot[j]=pot[j-1]*2;
    }

}

void prueba()
{
    int aux;
    aux=pot[n];
    k++;
    if ((k%aux)==0)
    {
        imprimeon();
    }
    else
       imprimeoff();
}
int main()
{
    scanf("%d",&t);
    potencias();
    for (i=1; i<=t; i++)
    {
        scanf("%d %d",&n,&k);
        if (n>k || (k%2)==0)
        {
           imprimeoff();
        }
        else
        {
            prueba();
        }
    }
}
