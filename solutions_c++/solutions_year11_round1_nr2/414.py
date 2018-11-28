#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <list>

using namespace std;

int n, m;
char slowo[100005][15], s[30];
int dl[100005];
bool litery[26];
bool l[100005][26];
int ile[26];
list <char*> lista;
list <char*> :: iterator it2;

int dzialaj(int nr)
{
    memset(ile, 0, sizeof(ile));
    int d = dl[nr];

    for(int i=0; slowo[nr][i]; i++)
        ile[slowo[nr][i]-'a']++;//, printf("     doklada litere %c\n", slowo[j][i]);

    for(int j=0; j<n; j++)
    {
        if(j != nr)
            if(dl[j] == d)
            {
                lista.push_back(slowo[j]);
                for(int i=0; slowo[j][i]; i++)
                    ile[slowo[j][i]-'a']++;//, printf("     doklada litere %c\n", slowo[j][i]);
            }
    }

//    printf("teraz sprawdzamy dla %s\n", slowo[nr]);

//    for(int i=0; i<26; i++)
//        printf("liter %c jest %d\n", i+'a', ile[i]);


    if(lista.empty())   return 0;

    int wynik = 0;

    for(int i = 0; i<26; i++)
    {
        int x = s[i];
//        printf("litera: %c\n", x);

        if(ile[x-'a'] == 0)   continue;

        int f = 0;
        for(int j=0; j<d; j++)
        {
            if(slowo[nr][j] == x)   f = 1;
        }

//        printf(" nowa partia, pod litere %c\n", x);
        if(f == 0)   wynik++;//, printf("loose!\n");
        for(list<char*>::iterator it = lista.begin(); it != lista.end(); )
        {
//            printf("  sprawdzane: %s\n", *it);
            char *pom = *it;
            bool flaga = 0;
            for(int j = 0; pom[j]; j++)
            {
                if((slowo[nr][j] == x && pom[j] != x) || (slowo[nr][j] != x && pom[j] == x))
                {
                    for(int v=0; pom[v]; v++)
                        ile[pom[v]-'a']--;
                    it2 = it;
                    it++;
                    lista.erase(it2);
                    flaga = 1;
                    break;
                }
            }
            if(!flaga)  it++;
        }
        if(lista.empty())   return wynik;
    }
}

void wczytaj()
{
//    memset(litery, 0, sizeof(litery));
//    memset(l, 0, sizeof(l));

    scanf("%d %d", &n, &m);
    for(int i=0; i<n; i++)
    {
        scanf("%s", slowo[i]);
        dl[i] = strlen(slowo[i]);
/*        for(int j=0; slowo[i][j]; j++)
        {
            l[i][slowo[i][j]-'a'] = 1;
            litery[slowo[i][j]-'a'] = 1;
        }*/
//        for(int j=0; j<26; j++)
//            if(l[i][j])   printf("%c", j+'a');
//        printf("\n");
    }
//    for(int j=0; j<26; j++)
//        if(litery[j])   printf("%c", j+'a');
//    printf("\n");

    for(int i=0; i<m; i++)
    {
        int best = -1, wynik = 0, x;
        scanf("%s", s);
        lista.clear();

        for(int j=0; j<n; j++)
        {
            x = dzialaj(j);
//            printf("wynik dla %s to %d, poprzedni %d\n", slowo[j], x, best);
            if (x > best)
            {
                best = x;
                wynik = j;
            }
        }
        printf(" %s", slowo[wynik]);
    }
}

int main()
{
	int tests;
	scanf("%d", &tests);
	for(int i=0; i<tests; i++)
	{
	    printf("Case #%d:", i+1);
		wczytaj();
		printf("\n");
	}

	return 0;
}
