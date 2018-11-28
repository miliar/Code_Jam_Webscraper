#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;

struct Chick
{
	int i, x, v;
	long double t;
	bool operator<(const Chick& c) const
	{
		return x < c.x;
	}
};

int n, k, b, t;
Chick cs[50];
Chick orig[50];


int solve()
{
	sort(cs, cs+n);
	long double maxt = 0;
	for(int i = n-1; i >=0; i--)
	{
		cs[i].t = max(maxt, (b-cs[i].x) / (long double)cs[i].v);
		maxt = max(maxt, cs[i].t);
		//printf("%Lf\n", maxt);
	}
	int nb = 0, nbS = 0;
	int ahead = 0;
	for(int i = n-1; i >= 0 ; i--)
	{
		if(nb == k)	return nbS;
		if(cs[i].t <= (long double)t + 0.00000000000001)
			nb++;
		else
		{
			if((b-cs[i].x) / (long double)cs[i].v <=  (long double)t + 0.00000000000001)
			{
				nbS += ahead;
				nb++;
			}
			else
				ahead++;
		}
		
	}
	if(nb == k)	return nbS;
	return -1;
}
int main()
{
	freopen("example.in.txt", "r", stdin);
	
	int nbCases, c = 0;
	scanf("%d", &nbCases);
	while(c != nbCases)
	{
		scanf("%d%d%d%d", &n, &k, &b, &t);
		for(int i = 0;i < n; i++)
		{
			cs[i].i=i;
			scanf("%d", &cs[i].x);
		}
		for(int i = 0;i < n; i++)
		{
			scanf("%d", &cs[i].v);
			orig[i] = cs[i];
		}
		int rep = solve();
		if(rep == -1)
			printf("Case #%d: IMPOSSIBLE\n", ++c);
		else
			printf("Case #%d: %d\n", ++c, rep);
	}
	
	return 0;
}