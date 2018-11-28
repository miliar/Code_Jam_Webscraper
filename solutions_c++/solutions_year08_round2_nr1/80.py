#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <set>

#define VI vector <int>
#define VVI vector < vector<int> >
#define VS vector <string>
#define rep(i,n) for(int i=0;i<(n);++i)
#define repab(i,a,b) for(int i=(a);i<=(b);++i)
#define PB push_back
#define SORT(v) sort(v.begin(), v.end())

using namespace std;

int nn[3][3];

void licz(void)
{
	rep(i,3)
	rep(j,3)
	nn[i][j]=0;
	long long n, A, B, C, D, x0, y0, M;
	long long X,Y;
	scanf("%lld%lld%lld%lld%lld%lld%lld%lld", &n, &A, &B, &C, &D, &x0, &y0, &M);
	X = x0;
	Y = y0;
	nn[X%3][Y%3]++;
	rep(i,n-1)
	{
		X = (A*X+B) % M;
		Y = (C*Y+D) % M;
		nn[X%3][Y%3]++;
	}
	long long s=0,z;
	long long a,b,c;
	rep(x1,3)
	rep(y1,3)
	{
		a = nn[x1][y1];
		nn[x1][y1]--;
		rep(x2,3)
		rep(y2,3)
		{
			b = nn[x2][y2];
			nn[x2][y2]--;
			rep(x3,3)
			rep(y3,3)
			{
				c = nn[x3][y3];
				if ((x1+x2+x3)%3==0)
				if ((y1+y2+y3)%3==0)
				if (a>0 && b>0 &&c>0)
				{
					z = a*b*c;
					s += z;
				}
			}
			nn[x2][y2]++;
		}
		nn[x1][y1]++;
	}
	s /= 6;
	printf("%lld\n",s);
}

int main(void)
{
	int dd;
	scanf("%d",&dd);
	for(int yy=0;yy<dd;yy++)
	{
		printf("Case #%d: ", yy+1);
		licz();
	}
	return 0;
}
