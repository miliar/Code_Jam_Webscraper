#include <vector>
#include <list>

#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;

#define FOR(i,n) for (int i = 0; i < n; i++) 
#define FOR1(i,n) for (int i = 1; i <= n; i++) 
#define SZ(x) ((int)x.size()) 
#define MEM(a,b) memset(a,b,sizeof(a))

int n;
struct c
{
	int x, y;
	double r;
	void read() { scanf("%d%d%lf", &x, &y, &r); }
	double d(c o)
	{
		return (sqrt((x-o.x)*(x-o.x)+(y-o.y)*(y-o.y)) + r + o.r)/2.;
	}
};
c w[3];
int main()
{
	scanf("%d", &n);
	FOR(t, n)
	{
		int nc;
		double rep;
		scanf("%d", &nc);
		FOR(i, nc) w[i].read();
		if(nc == 1) rep = w[0].r;
		if(nc == 2) rep = max(w[1].r, w[0].r);
		if(nc == 3)
		{
			rep = min(max(w[0].r, w[1].d(w[2])),
								max(w[2].r, w[1].d(w[0])));
			rep = min(rep,
								max(w[1].r, w[0].d(w[2])));
		}
		printf("Case #%d: %lf\n", t+1, rep);
	}
}
/*
int n;

struct cc
{
	int i, adj;
	bool operator<(const cc& o) const
	{
		return adj<o.adj;
	}
};
vector<cc> vecto;

vector<int> v[101];
bool m[101][101];
int taken[101];
int main()
{
	scanf("%d\n", &n);
	FOR(i, n)
	{
		int nbN, nbP;
		scanf("%d%d", &nbN, &nbP);
		FOR(j, nbN)
		{
			v[j].clear();
			FOR(k, nbP)
			{
				int a; scanf("%d", &a); v[j].push_back(a);
			}	
		}
		MEM(taken, -1);
		vecto.clear();
		FOR(j, nbN)
		{
			cc cur;
			cur.i = j; cur.adj = 0;
			FOR(k, nbN)
			{
				
				m[j][k] = true;
				for(int l = 1; l < nbP; l++)
				{
					//printf("(%d, %d) : (%d - %d) * (%d - %d) = %d\n", j, k, v[j][l], v[k][l], v[j][l-1], v[k][l-1], (v[j][l] - v[k][l]) * (v[j][l-1] - v[k][l-1]));
					if((v[j][l] - v[k][l]) * (v[j][l-1] - v[k][l-1]) <= 0)
					{
						m[j][k] = false;
					}
				}
				if(k==j) m[j][k] = true;
				if(m[j][k]) cur.adj++;
				
				//printf("%d ", m[j][k]);
			}
			vecto.push_back(cur);
			//printf("\n");
		}
		sort(vecto.begin(), vecto.end());
	//	FOR(j, nbN)
		//	printf("%d : %d\n", vecto[j].i, vecto[j].adj);
		
		int rep = 0;
		FOR(j, nbN)
		{
			if(taken[vecto[j].i] != -1) continue;
			taken[vecto[j].i] = rep++;
			FOR(k, nbN)
				if(taken[vecto[k].i] == -1)
				{
					bool ok = true;
					FOR(l, nbN)
						if(taken[vecto[l].i] == taken[vecto[j].i] && !m[vecto[k].i][vecto[l].i])
							ok = false;
					if(ok) { taken[vecto[k].i] = taken[vecto[j].i]; //printf("%d with %d\n", vecto[k].i, vecto[j].i);
					}		
				}
			FOR(k, nbN)
			{
				if(taken[vecto[k].i] == taken[vecto[j].i])
				{
					FOR(l, nbN)
					{
						if(m[vecto[k].i][vecto[l].i] && taken[vecto[k].i] == -1)
							vecto[k].adj--;
					}
					vecto[k].adj = -1;
				}
			}
			sort(vecto.begin(), vecto.end());
		}
		printf("Case #%d: %d\n", i+1, rep);
	}
}*/
