/*
 * =====================================================================================
 *
 * Nazwa pliku:  	bot.cpp
 * Autor:		Szymon Stankiewicz (Daku)
 * Kontakt:		dakurels@gmail.com
 * Stworzony:		07.05.2011 01:05:23
 *
 * =====================================================================================
 */
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<iostream>

using namespace std;

long long int P, N, aktualne[2], czas[2], numer;
char kolor;

int main()
{
    scanf("%lld", &P);
    for (int iter=1; iter<=P; iter++)
    {
        scanf("%lld", &N);
        aktualne[1]=1;
        aktualne[0]=1;
        czas[0]=0;
        czas[1]=0;
        for(int i =0; i<N; i++)
        {
            cin.ignore();
            scanf("%c %lld", &kolor, &numer);
            if (kolor=='B')
            {
                czas[0]+=abs(numer-aktualne[0]);
                aktualne[0]=numer;
                czas[0]=max(czas[0], czas[1]);
                czas[0]++;
            }
            else
            {
                czas[1]+=abs(numer-aktualne[1]);
                aktualne[1]=numer;
                czas[1]=max(czas[0], czas[1]);
                czas[1]++;
            }
        }
        printf("Case #%d: %lld\n", iter, max(czas[0],czas[1]));
    }
    return 0;
}
