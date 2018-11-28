#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int n, l, h, tab[100005];

void wczytaj()
{
    scanf("%d %d %d", &n, &l, &h);
    for(int i=0; i<n; i++)
        scanf("%d", &tab[i]);
}

int dzialaj()
{
    bool flaga;

    for(int i=l; i<=h; i++)
    {
        flaga = 1;
        for(int j=0; j<n; j++)
            if(i % tab[j] != 0 && tab[j] % i != 0)
            {
                flaga = 0;
                break;
            }
        if(flaga == 1)   return i;
    }
    return -1;
}

int main()
{
	int tests;
	scanf("%d", &tests);
	for(int i=0; i<tests; i++)
	{
	    wczytaj();
		printf("Case #%d: ", i+1);
		int x = dzialaj();

        if(x == -1)   printf("NO\n");
        else   printf("%d\n", x);
	}

	return 0;
}
