#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int w, k;
char tab[1005][1005];

void wczytaj()
{
    scanf("%d %d", &w, &k);
    for(int i=0; i<w; i++)
        scanf("%s", tab[i]);
    for(int i=0; i<=k+1; i++)
        tab[w][i] = '.';
}

bool dzialaj()
{
    for(int i=0; i<w; i++)
        for(int j=0; j<k; j++)
        {
            if(tab[i][j] == '#')
            {
                if(tab[i+1][j] != '#' || tab[i][j+1] != '#' || tab[i+1][j+1] != '#')   return 0;
                tab[i][j] = '/';
                tab[i+1][j] = '\\';
                tab[i][j+1] = '\\';
                tab[i+1][j+1] = '/';
            }
        }
}

void wyswietl()
{
    for(int i=0; i<w; i++)
        printf("%s\n", tab[i]);
}

int main()
{
	int tests;
	scanf("%d", &tests);
	for(int i=0; i<tests; i++)
	{
		wczytaj();
		printf("Case #%d:\n", i+1);
		if(!dzialaj())
            printf("Impossible\n");
        else   wyswietl();
	}

	return 0;
}
