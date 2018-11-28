/*
 * =====================================================================================
 *
 * Nazwa pliku:  	C.cpp
 * Autor:		Szymon Stankiewicz (Daku)
 * Kontakt:		dakurels@gmail.com
 * Stworzony:		15.04.2012 01:35:43
 *
 * =====================================================================================
 */
#include<cstdio>

int leng(int a)
{
    int c=0;
    while(a>0)
       {
           c++;
           a/=10;
       }
    return c;
}

int rotate(int a, int b)
{
    int len=leng(a);
    int x=a, k=1, d=1;
    for(int i = 0; i<leng(a)-b; i++)
    {
        k*=10;
        x/=10;
    }
    for (int i = 0; i<b; i++)
        d*=10;
    return (a%k)*d+x;
}

int T,a,b, out;

int main()
{
    scanf("%d", &T);
    for(int i = 1; i<=T; i++)
    {
        out=0;
        scanf("%d %d", &a, &b);
        for(int j = a; j<=b; j++)
            for(int k=1; k<leng(j); k++)
                if(rotate(j,k) < j && rotate(j, k)>=a)
                {
//                    printf("%d %d\n", j, rotate(j,k));
                    out++;
                }
        printf("Case #%d: %d\n", i, out);
    }
    return 0;
}
