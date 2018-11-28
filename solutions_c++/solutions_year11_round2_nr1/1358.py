/*
 * =====================================================================================
 *
 * Nazwa pliku:  	A.cpp
 * Autor:		Szymon Stankiewicz (Daku)
 * Kontakt:		dakurels@gmail.com
 * Stworzony:		21.05.2011 18:03:41
 *
 * =====================================================================================
 */
#include<cstdio>

char tab[1000][1000];
int N, k;
double wp[1000], wp2[1000], owp[1000], oowp[1000],a,b;

int main()
{
    scanf("%d", &k);
    for (int it=1; it<=k; it++)
    {
        scanf("%d", &N);
        for (int i =0; i<N; i++)
            scanf("%s", tab[i]);
        for (int i =0; i<N; i++)
        {
            a=0.0;
            b=0.0;
            for (int j =0; j<N; j++)
            {
                if(tab[i][j]=='1')
                {
                    a+=1.0;
                    b+=1.0;
                }
                if(tab[i][j]=='0')
                {
                    b+=1.0;
                }
            }
            wp[i]=a;
            wp2[i]=b;
        }
        for (int i =0; i<N; i++)
        {
            b=0.0;
            a=0.0;
            for (int j =0; j<N; j++)
            {
                if(tab[i][j]!='.')
                {
                    b+=(wp[j]-1+(tab[i][j]-'0'))/(wp2[j]-1);
                    a+=1.0;
                }
            }
            owp[i]=b/a;
        }
        for (int i =0; i<N; i++)
        {
            b=0.0;
            a=0.0;
            for (int j=0; j<N; j++)
            {
                if(tab[i][j]!='.')
                {
                    a+=1.0;
                    b+=owp[j];
                }
            }
            oowp[i]=b/a;
        }
        printf("Case #%d:\n", it);
        for (int i =0; i<N; i++)
        {
            printf("%lf\n", 0.25*(wp[i]/wp2[i])+0.5*owp[i]+0.25*oowp[i]);
        }
    }
    return 0;
}

