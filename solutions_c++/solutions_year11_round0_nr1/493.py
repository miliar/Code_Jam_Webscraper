#include <cstdio>
#include <utility>
#include <vector>

using namespace std;

#define ABS(x) (((x) > 0) ? (x) : -(x))

pair<char, int> buts[101];

int main()
{
	int n, b, ora, blu, p;
	scanf("%d", &n);
	
	for (int c = 1; c <= n; ++c)
	{
		vector<int> goOra, goBlu;
		scanf(" %d ", &b);
		for (int i = 0; i < b; ++i)
		{
			scanf(" %c %d ", &buts[i].first, &buts[i].second);
			if (buts[i].first == 'O')
				goOra.push_back(buts[i].second);
			else
				goBlu.push_back(buts[i].second);
		}
		ora = 1;
		blu = 1;
		p = 0;
		int t = 0;
		
		while (p < b)
		{
			int r;
			if (buts[p].first == 'O')
			{
				goOra.erase(goOra.begin());
				r = ABS(buts[p].second-ora);
				ora = buts[p].second;
				++r;
				t += r;
				//
				if (goBlu.size())
				{
					int x = goBlu[0];
					if (x < blu)
					{
						if (blu-x <= r)
							blu = x;
						else
							blu -= r;
					}
					else if (x > blu)
					{
						if (x-blu <= r)
							blu = x;
						else
							blu += r;
					}
				}
			}
			else
			{
				goBlu.erase(goBlu.begin());
				r = ABS(buts[p].second-blu);
				blu = buts[p].second;
				++r;
				t += r;
				//
				if (goOra.size())
				{
					int x = goOra[0];
					if (x < ora)
					{
						if (ora-x <= r)
							ora = x;
						else
							ora -= r;
					}
					else if (x > ora)
					{
						if (x-ora <= r)
							ora = x;
						else
							ora += r;
					}
				}
			}
			++p;
		}
		
		printf("Case #%d: %d\n", c, t);
	}

	return 0;
}

