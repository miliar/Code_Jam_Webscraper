#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <map>
#include <iostream>
#include <sstream>
#include <queue>
#include <cstring>
#include <ctime>
#include <cfloat>

using namespace std;

#define SZ 1005

typedef pair<int, int> PII;

vector<PII> orange;
vector<PII> blue;

int main()
{
	//freopen("A-small-attempt0.in", "rt", stdin);
	//freopen("A-small.out", "wt", stdout);

	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	int inp, tmp, r, kase, n, k, i, j;
	char ch;
	scanf("%d", &inp);
	
	for(kase = 1; kase <= inp; kase++)
	{
		scanf("%d", &n);
		orange.clear();
		blue.clear();
		for(i = 0; i < n; i++)
		{
			scanf(" %c %d", &ch, &tmp);
			if(ch == 'B')
			{
				blue.push_back(make_pair(i, tmp));
			}
			else
			{
				orange.push_back(make_pair(i, tmp));
			}
		}
		
		blue.push_back(make_pair(n + 1, -1));
		orange.push_back(make_pair(n + 1, -1));
		
		sort(blue.begin(), blue.end());
		sort(orange.begin(), orange.end());

		int bi, oi, tm;
		bi = oi = tm = 0;
		int cb, co;
		int ct = 0;
		cb = co = 1;

		while(blue[bi].first < n || orange[oi].first < n)
		{
			if(ct == blue[bi].first)
			{
				if(blue[bi].second == cb)
				{
					ct++;
					bi++;
				}
				else if(blue[bi].second > cb)
				{
					cb++;
				}
				else
				{
					cb--;
				}
				if(orange[oi].second > co)
				{
					co++;
				}
				else if(orange[oi].second < co)
				{
					co--;
				}
			}
			else
			{
				if(orange[oi].second == co)
				{
					ct++;
					oi++;
				}
				else if(orange[oi].second > co)
				{
					co++;
				}
				else
				{
					co--;
				}
				if(blue[bi].second > cb)
				{
					cb++;
				}
				else if(blue[bi].second < cb)
				{
					cb--;
				}
			}
			tm++;
		}

		printf("Case #%d: %d\n", kase, tm);
	}
	return 0;
}

