#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <list>

using namespace std;

int n, a, pos_b, pos_o;
bool czy_niebieski[100005];
list <int> o, b;

void wczytaj()
{
    char znak[5];

    o.clear();
    b.clear();
    pos_b = pos_o = 1;

    scanf("%d", &n);
    for(int i=0; i<n; i++)
    {
        scanf("%s %d", znak, &a);
        if(znak[0] == 'B')
        {
            b.push_back(a);
            czy_niebieski[i] = 1;
        }
        else
        {
            o.push_back(a);
            czy_niebieski[i] = 0;
        }
    }

    o.push_back(1);
    b.push_back(1);
}

int dzialaj()
{
    int i = 0, ruch = 0, f = 0;

    for(; i < n; ruch++)
    {
        if(pos_b != *b.begin())
        {
            if(pos_b < *b.begin())   pos_b++;
            else   pos_b--;
        }
        else
        {
            if(czy_niebieski[i])
            {
                b.pop_front();
                f = 1;
            }
        }

        if(pos_o != *o.begin())
        {
            if(pos_o < *o.begin())   pos_o++;
            else   pos_o--;
        }
        else
        {
            if(!czy_niebieski[i])
            {
                o.pop_front();
                f = 1;
            }
        }
        i += f;
        f = 0;

//        printf("ruch %d - o:%d, b:%d, i = %d\n", ruch, pos_o, pos_b, i);
    }
    return ruch;
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
