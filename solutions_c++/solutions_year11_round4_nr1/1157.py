//compiled in vc
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <complex>
// C++
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <climits>
#include <ctime>
using namespace std;


struct road
{
	int s , t;
	int speed;
};

bool cmp1( const road &l, const road &r) 
{
	return l.s < r.s;
}

bool cmp2( const road &l, const road &r) 
{
	if( l.speed != r.speed ) return l.speed < r.speed;
	return l.s < r.s;
}


int main()
{
	int cases , Case = 1;
	scanf("%d" , &cases);
	

	int x , s , r , t , n;
	while( cases-- )
	{
		printf("Case #%d: " , Case++);   

		scanf("%d%d%d%d%d" , &x, &s,&r,&t,&n);

		vector< road> roads;
		for(int i= 0;i<n;i++)
		{
			road a;
			scanf("%d%d%d" , &a.s,&a.t , &a.speed);

			a.speed +=s;
			roads.push_back(a);
		}

		sort( roads.begin() , roads.end() , cmp1);
		int start = 0;
		for(int i= 0;i<n;i++)
		{
			if( roads[i].s != start )
			{
				road a;
				a.s = start;
				a.t = roads[i].s;
				a.speed = s;
				
				roads.push_back(a);
			}
			
				start = roads[i].t;
		}

		if( start != x )
		{
			road a;
				a.s = start;
				a.t = x;
				a.speed = s;
				roads.push_back(a);
		}

		sort( roads.begin() , roads.end() , cmp2);
		
		double ans = 0;
		double reSec = t;
		for(int i = 0 ; i < roads.size(); i++)
		{
			if( reSec > 1e-8)
			{
				double useS = (double)( roads[i].t - roads[i].s )/(double)(roads[i].speed -s + r);
				if( reSec >= useS ) //!!!
				{
					reSec -= useS;
					ans += useS;
				}
				else
				{
					double canRun = (double)(roads[i].speed + r -s ) * reSec;
					ans += reSec;
					double redis = (double)( roads[i].t - roads[i].s ) - canRun;


					ans += (double)( redis )/(double)roads[i].speed;

					reSec = -1;
				}
			}
			else
			{
				ans += (double)( roads[i].t - roads[i].s )/(double)roads[i].speed;
			}

		}

		printf("%0.10lf\n" , ans);

	}

	return 0;
}
