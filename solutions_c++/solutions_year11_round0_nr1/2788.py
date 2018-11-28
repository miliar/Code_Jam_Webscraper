#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int main (void)
{
    int teste, n;
    vector<pair<int,int> > ora, blu;

    scanf ("%d", &teste);

    for (int t = 1; t <= teste; ++t)
    {
        int tempo = 0;
        scanf ("%d", &n);
        ora.clear();
        blu.clear();

        for (int i = 0; i < n; i++)
        {
            int x;
            char c;
            scanf (" %c %d", &c, &x);

            if (c == 'O')
                ora.push_back(make_pair(i, x));
            else
                blu.push_back(make_pair(i, x));
        }
        
        int b = 1, o = 1;
        for (unsigned int i1 = 0, i2 = 0, i = 0; i1 < ora.size() || i2 < blu.size(); )
        {
        	++tempo;
        	bool apertou = false;
        	if (i1 < ora.size())
        	{
        		if (ora[i1].first == (int) i && o == ora[i1].second)
        		{
        			++i;
        			++i1;
        			apertou = true;
        		}
        		else if (ora[i1].second > o) ++o;
        		else if (ora[i1].second < o) --o;
        	}
        	
        	if (i2 < blu.size())
        	{
        		if (blu[i2].first == (int) i && b == blu[i2].second && !apertou)
        		{
        			++i;
        			++i2;
        		}
        		else if (blu[i2].second > b) ++b;
        		else if (blu[i2].second < b) --b;
        	}
        }

        printf ("Case #%d: %d\n", t, tempo);
    }

    return 0;
}
