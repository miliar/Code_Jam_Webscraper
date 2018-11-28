#include <iostream>
#include <cstdio>
#include <set>
#include <map>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <functional>
#include <queue>
#include <bitset>
#include <sstream>
using namespace std;

#define	rep(i,N)	for((i) = 0; (i) < (N); (i)++)
#define	rab(i,a,b)	for((i) = (a); (i) <= (b); (i)++)
#define	Fi(N)		rep(i,N)
#define	Fj(N)		rep(j,N)
#define	Fk(N)		rep(k,N)
#define	sz(v)		(int)v.size()

const int debug_flag	 = 0;

#define	DBG(f,x)	if(debug_flag & f) x

typedef pair<int,int>	PII;

vector <PII>	brd,nbrd;
int		bhl,bhh,bwl, bww;

bool inrange(int a, int b, int x)
{
	return a <= x && x <= b;
}

int	possh[1000];
int	possw[1000];

int main()
{
	int	T,cs;
	int	N,M;
	int	h,w;
	int	i,j,k,l;
	char	s[1000];
	int	bhl,bwl,bhh,bwh;
	int	uhl,uwl, uhh, uwh;

	scanf("%d",&T);

	rab(cs,1,T)
	{
		scanf("%d",&N);

		brd.clear();
		nbrd.clear();

		while(N--)
		{
			scanf("%d %d %s",&h,&w,s);

			if(s[0] == 'B')
				brd.push_back(PII(h,w));
			else
				nbrd.push_back(PII(h,w));

			while(getchar() != '\n');
		}	

		bhl = bwl = bhh = bwh = -1;

		Fi(sz(brd))
		{
			if(brd[i].first < bhl || bhl == -1) bhl = brd[i].first;
			if(brd[i].first > bhh || bhh == -1) bhh = brd[i].first;
			if(brd[i].second < bwl || bwl == -1) bwl = brd[i].second;
			if(brd[i].second > bwh || bwh == -1) bwh = brd[i].second;
		}

		scanf("%d",&M);

		printf("Case #%d:\n",cs);

		while(M--)
		{
			scanf("%d %d",&h,&w);

			if(bhl <= h && h <= bhh && bwl <= w && w <= bwh)
				printf("BIRD\n");
			else
			{
				int	nhl,nhh,nwl,nwh;

				if(bhl == -1)
				{
					nhl = nhh = h;
					nwl = nwh = w;
				}
				else
				{
					nhl = min(bhl,h);
					nhh = max(bhh,h);
					nwl = min(bwl,w);
					nwh = max(bwh,w);
				}

				DBG(1,printf("w=%d; h=%d\n",w,h));

				Fi(sz(nbrd))
				{
					if(inrange(nhl,nhh,nbrd[i].first) && inrange(nwl,nwh, nbrd[i].second))
						break;
				}

				DBG(1,printf("%d %d %d %d\n",nhl,nhh,nwl,nwh));

				if(i >= sz(nbrd))
					printf("UNKNOWN\n");
				else
					printf("NOT BIRD\n");
			}

		}

	}

	return 0;
}
