#include <iostream>
#include <string>
#include <set>
#include <cstdio>
#include <cstdlib>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)

#define esta(x,c) ((c).find(x) != (c).end())

int N,D,L;

string d[6000];

set<char> pa[32];

int main()
{
	freopen("entrada.in","r",stdin);
	freopen("salida.out","w",stdout);
	cin >> L >> D >> N;
	forn(i,D)
		cin >> d[i];
	forn(tt,N)
	{
		forn(i,L)
			pa[i].clear();
		string p;
		cin >> p;
		{
			int j=0;
			forn(i,p.size())
			if (p[i] == '(')
			{
				for(i++;p[i] != ')';i++)
					pa[j].insert(p[i]);
				j++;
			}
			else
				pa[j++].insert(p[i]);
		}	
		int res = 0;
		forn(i,D)
		{
			int anda = 1;
			forn(j,L)
			if (!esta(d[i][j],pa[j]))
			{
				anda = 0;
				break;
			}
			res += anda;
		}
		printf("Case #%d: %d\n",tt+1,res);
	}
	return 0;
}
