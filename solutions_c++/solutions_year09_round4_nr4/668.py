#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>

using namespace std;

struct Point
{
	int x;
	int y;
	int r;
};

int C;
int n;

double eps = 1e-7;
int ind1, ind2;

vector <Point> v;
vector <Point> v1;
vector <Point> v2;

double Dist(Point &p1, Point &p2)
{
	return sqrt((double)((p2.x - p1.x)*(p2.x - p1.x) + (p2.y - p1.y)*(p2.y - p1.y))) + p1.r + p2.r;
}

bool Pred1( Point &p1, Point &p2 )
{
	return Dist( v[ind1], p1 ) > Dist( v[ind1], p2 );
}

bool Pred2( Point &p1, Point &p2 )
{
	return Dist( v[ind2], p1 ) > Dist( v[ind2], p2 );
}


void Solve()
{
	int i1, i2;
	double m = -1;

	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j < n; j++)
		{
			if( i == j )
				continue;
			double ro = Dist( v[i], v[j] );
			if( ro > m + eps )
			{
				i1 = i;
				i2 = j;
				m = ro;
			}
		}
	}

	ind1 = i1;
	ind2 = i2;


	for(int i = 0; i < n; i++)
	{
		if( i == i1 || i == i2 )
			continue;

		if( Dist( v[i], v[i1] ) < Dist( v[i], v[i2] ) - eps )
			v1.push_back(v[i]);
		else
			v2.push_back(v[i]);
	}


	sort( v1.begin(), v1.end(), Pred1 );
	sort( v2.begin(), v2.end(), Pred2 );

	double ans1, ans2;

	if( v1.empty() )
		ans1 = v[i1].r;
	else
		ans1 = Dist( v[i1], v1[0] )/2;

	if( v2.empty() )
		ans2 = v[i2].r;
	else
		ans2 = Dist( v[i2], v2[0] )/2;

	if( ans1 > ans2 )
	{
		printf("%lf\n", ans1);
	}
	else
	{
		printf("%lf\n", ans2);
	}
}


int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &C);

	int x, y, r;
	Point tmp;

	for(int ii = 0; ii < C; ii++)
	{
		scanf("%d", &n);

		v.clear();
		v1.clear();
		v2.clear();

		for(int i = 0; i < n; i++)
		{
			scanf("%d%d%d", &x, &y, &r);

			tmp.x = x;
			tmp.y = y;
			tmp.r = r;

			v.push_back(tmp);
		}

		printf("Case #%d: ", ii+1);

		if( n == 1 )
			printf("%d\n", v[0].r);
		else
			Solve();
	}


	return 0;
}