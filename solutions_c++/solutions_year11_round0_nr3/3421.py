/*
 * =====================================================================================
 *
 * Nazwa pliku:  	candy.cpp
 * Autor:		Szymon Stankiewicz (Daku)
 * Kontakt:		dakurels@gmail.com
 * Stworzony:		07.05.2011 01:43:08
 *
 * =====================================================================================
 */
#include<cstdio>

long long int xory, suma, minimum, t,n,z;

int main()
{
    scanf("%lld", &t);
    for (int it =1; it<=t; it++)
    {
        scanf("%lld", &n);
        minimum=2000007;
        xory=0;
        suma=0;
        for (int i =0; i<n; i++)
        {
            scanf("%lld", &z);
            xory^=z;
            suma+=z;
            if(z<minimum)
                minimum=z;
        }
        printf("Case #%d: ", it);
        if (xory!=0)
            printf("NO\n");
        else
            printf("%lld\n", suma-minimum);
    }
    return 0;
}
