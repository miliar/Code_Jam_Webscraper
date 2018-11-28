/*
 * =====================================================================================
 *
 * Nazwa pliku:  	B.cpp
 * Autor:		Szymon Stankiewicz (Daku)
 * Kontakt:		dakurels@gmail.com
 * Stworzony:		15.04.2012 01:00:00
 *
 * =====================================================================================
 */
#include<cstdio>

int N, M, p, s, x, out;

int main()
{
    scanf("%d", &N);
    for (int i =1; i<=N; i++)
    {
        out=0;
        scanf("%d %d %d", &M, &s, &p);
        for (int j=0; j<M; j++)
        {
            scanf("%d", &x);
            if(x<p) continue;
            if((x-p)/2>=p-1)
                out++;
            else if((x-p)/2 == p-2 && s>0 && x<=28 && x>=2)
            {
                s--;
                out++;
            }
        }
        printf("Case #%d: %d\n", i, out);
    }
    return 0;
}
