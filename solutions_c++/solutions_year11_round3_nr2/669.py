#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int n, l, t, c, tab[1000005], wynik[1000005], suma = 0, s2 = 0;

struct para
{
    int odl;
    int ile_razy;
};
para p[1000005];

int comp(const void *f, const void *s)
{
    para F = *(para*)f;
    para S = *(para*)s;
    return S.odl - F.odl;
}

void wczytaj()
{
    suma = 0;
    s2 = 0;
    scanf("%d %d %d %d", &l, &t, &n, &c);
    for(int i=0; i<c; i++)
    {
        scanf("%d", &tab[i]);
        tab[i] *= 2;
        suma += tab[i] * (n/c + (n%c > i));
        s2 += tab[i];
//        printf("%d -> %d razy\n", tab[i], (n/c + (n%c > i)));
        p[i].odl = tab[i]/2;
        p[i].ile_razy = (n/c + (n%c > i));
    }
//    printf("suma: %d\n", suma);

    p[c].odl = 0;
    p[c].ile_razy = 0;

    int akt_suma = 0;
    for(int i=0; i<c; i++)
    {
        p[i].ile_razy -= t/s2;
        if(t % s2 > akt_suma)
        {
            p[i].ile_razy--;

            if(t % s2 < akt_suma + tab[i])
            {
                p[c].odl = (akt_suma + tab[i] - t % s2)/2;
                p[c].ile_razy = 1;
//                printf("+ %d -> %d razy na speedzie\n", p[c].odl, p[c].ile_razy);
            }
        }
        p[i].ile_razy = max(p[i].ile_razy, 0);

        akt_suma += tab[i];

//        printf("  %d -> %d razy na speedzie\n", tab[i], p[i].ile_razy);
    }
}

int dzialaj()
{
    int wynik = suma;

    qsort(p, c+1, sizeof(p[0]), comp);
/*
    for(int i=0; i <= c; i++)
    {
        printf("%d jest %d razy\n", p[i].odl, p[i].ile_razy);
    }
*/
    for(int i=0; i <= c; i++)
    {
        if(p[i].ile_razy <= l)
        {
            wynik -= p[i].ile_razy * p[i].odl;
            l -= p[i].ile_razy;
//            printf("zabieramy %d razy %d\n", p[i].odl, p[i].ile_razy);
        }
        else
        {
            if(l > 0)
            {
                wynik -= l * p[i].odl;
                l = 0;
//                printf("zabieramy %d razy %d\n", p[i].odl, l);
            }
            break;
        }
    }

    return wynik;
}

int main()
{
	int tests;
	scanf("%d", &tests);
	for(int i=0; i<tests; i++)
	{
	    wczytaj();
		printf("Case #%d: %d\n", i+1, dzialaj());
	}

	return 0;
}
