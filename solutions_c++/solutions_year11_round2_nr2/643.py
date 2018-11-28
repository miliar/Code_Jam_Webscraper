#include<stdio.h>
#include<string>
#include<queue>
#include <math.h>
#include<set>
#include<cstring>
#include<assert.h>
#include<iostream>
#include<map>
#include<algorithm>
#define sf scanf
#define pf printf
#define clr(key) memset(key,0,sizeof(key))
using namespace std;
#define ll long long

struct ft
{
	ll pos;
	int num;

}pos[300];

const double eps = 1e-9;
int n;
ll D;

bool cmp( const ft &a,const ft &b )
{
	return a.pos < b.pos;
}

int check( double t )
{
	double nowfar = pos[0].pos - t;
	for(int j=0;j<n;++j)
	{
		for(int i=0;i<pos[j].num;++i)
		{
			if( nowfar < pos[j].pos )
			{
				if( pos[j].pos - nowfar < D )
				{
					double tmp = D-( pos[j].pos - nowfar );
					if( tmp < t + eps )
					{
						nowfar = pos[j].pos + tmp;
					}
					else
						return -1;
				}
				else
				{
					double tmp = min(t,pos[j].pos - nowfar - D);
					nowfar = pos[j].pos - tmp;
				}
			}
			else
			{
				double tmp = nowfar + D - pos[j].pos;	
				if( tmp > t + eps )
				{
					return -1;
				}
				nowfar = tmp + pos[j].pos;
			}
		}
	}
	return 0;
}

int sol()
{
	sort( pos,pos+n,cmp);
	pos[0].num--;

	double l = 0, r = 1e13;
	while( fabs(l-r)>eps )
	{
		double mid = (l+r)/2.0;
		if( check( mid ) == 0 )
		{
			r = mid;
		}
		else
			l = mid;
	}
	printf("%.8lf\n",l);
}

int main()
{
	int T;
	scanf("%d",&T);
	int ca=0;
	while(T--)
	{
		scanf("%d",&n);
		scanf("%lld",&D);
		for(int i=0;i<n;++i)
		{
			scanf("%lld%d",&pos[i].pos,&pos[i].num);
		}
		printf("Case #%d: ",++ca);
		sol();
	}
}

