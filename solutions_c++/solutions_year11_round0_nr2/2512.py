#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <list>

using namespace std;

int n, k, l, dl;
char zamien[128][128];
list <char> czysc[128];
list <char> lista;
int byl[128];
char tab[10005];

void wczytaj()
{
    memset(zamien, 0, sizeof(zamien));
    memset(byl, 0, sizeof(byl));
    for(int i=0; i<128; i++)
        czysc[i].clear();
    lista.clear();

    char slowo[5];

    scanf("%d", &k);
    for(int i=0; i<k; i++)
    {
        scanf("%s", slowo);
        zamien[slowo[0]][slowo[1]] = slowo[2];
        zamien[slowo[1]][slowo[0]] = slowo[2];
    }

    scanf("%d", &l);
    for(int i=0; i<l; i++)
    {
        scanf("%s", slowo);
        czysc[slowo[0]].push_back(slowo[1]);
        czysc[slowo[1]].push_back(slowo[0]);
    }

    scanf("%d", &dl);
    scanf("%s", tab);
}

void wyswietl()
{
    printf("[");
    if(lista.empty())
    {
        printf("]");
        return ;
    }
    list <char>::iterator it = lista.end();
    it--;
    printf("%c", *it);

    while(it != lista.begin())
    {
        it--;
        printf(", %c", *it);
    }

    printf("]");
}

void dzialaj()
{
    for(int i=0; tab[i]; i++)
    {
        if(lista.empty())
        {
            lista.push_back(tab[i]);
            byl[tab[i]]++;
        }
        else
        {
            if(zamien[*lista.begin()][tab[i]])
            {
                byl[*lista.begin()]--;
                char x = *lista.begin();
                lista.pop_front();
                lista.push_front(zamien[x][tab[i]]);
                byl[*lista.begin()]++;
            }
            else
            {
                for(list<char>::iterator it = czysc[tab[i]].begin(); it != czysc[tab[i]].end(); ++it)
                    if(byl[*it])
                    {
                        memset(byl, 0, sizeof(byl));
                        lista.clear();
                        break;
                    }
                if(!lista.empty())
                {
                    lista.push_front(tab[i]);
                    byl[tab[i]]++;
                }
            }
        }

//        printf("%2d: ", i);
//        wyswietl();
//        printf("\n");
    }
}

int main()
{
	int tests;
	scanf("%d", &tests);
	for(int i=0; i<tests; i++)
	{
	    wczytaj();
	    dzialaj();
		printf("Case #%d: ", i+1);
		wyswietl();
		printf("\n");
	}

	return 0;
}
