//darkstallion's template

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<string>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define popb pop_back
#define del erase
#define sz size
#define ins insert
#define FOR(a,b,c) for(int a = b; a < c; a++)
#define FORS(a,b,c) for(int a = b; a <= c; a++)
#define FORN(a,b) for(int a = 0; a < b; a++)
#define FORD(a,b,c) for (int a = b; a >= c; a--)
#define RES(a,b) memset(a,b,sizeof(a))
#define LL long long
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define PDD pair<double,double>
#define PCC pair<char,char>
#define PSS pair<string,string>
using namespace std;

int t,n,w,l,z,zz,zzz;

bool cf(PII a, PII b)
{
	return a.fi > b.fi;
}

int main()
{
	scanf("%d",&t);
	FORN(i,t)
	{
		scanf("%d%d%d",&n,&w,&l);
		vector<PII> data;
		FORN(j,n)
		{
			scanf("%d",&z);
			data.pb(mp(z,j));
		}
		printf("Case #%d:",i+1);
		double x[n],y[n];
		sort(data.begin(),data.end(),cf);
		z = 0;
		zz = 0;
		zzz = 0;
		FORN(j,data.sz())
		{
			if (z == 0)
			{
				x[data[j].se] = 0;
				zz = zzz;
				if (zz == 0)
					y[data[j].se] = 0;
				else
					y[data[j].se] = zz+data[j].fi;
				zzz = y[data[j].se]+data[j].fi;
				z = x[data[j].se]+data[j].fi;
				if (z >= w)
					z = 0;
			}
			else
			{
				if (z+data[j].fi > w)
				{
					z = 0;
					x[data[j].se] = 0;
					zz = zzz;
					if (zz == 0)
						y[data[j].se] = 0;
					else
						y[data[j].se] = zz+data[j].fi;
					zzz = y[data[j].se]+data[j].fi;
					z = x[data[j].se]+data[j].fi;
					if (z >= w)
						z = 0;
				}
				else
				{
					x[data[j].se] = z+data[j].fi;
					if (zz == 0)
						y[data[j].se] = 0;
					else
						y[data[j].se] = zz+data[j].fi;
					z = x[data[j].se]+data[j].fi;
					if (z >= w)
						z = 0;
				}
			}
		}
		FORN(j,n)
			printf(" %lf %lf",x[j],y[j]);
		printf("\n");
	}
}
