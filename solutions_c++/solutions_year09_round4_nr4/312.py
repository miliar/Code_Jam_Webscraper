#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define MST(a,b) (memset(a,b,sizeof(a)))
#define DB(x) (cout<<#x<<": "<<x<<endl)
#define PB push_back
#define MP make_pair
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

int t, n;
int x[16], y[16], r[16];


double Dist(int i, int j)
{
	double dist = sqrt((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]) * 1.0) + r[i] + r[j];

	return dist / 2.0;
}

int main()
{
    freopen("D_S.in","r", stdin);
	freopen("D_S.out", "w", stdout);
	scanf("%d", &t);
	int i, j, k;
	double a, b, c;
	int Case;
	for( Case = 1; Case <= t; Case++)
	{
		scanf("%d", &n);
		for(i = 0; i < n; i++)
		{
			scanf("%d%d%d", x + i, y + i, r + i);
		}
		double ret = 0;
		if(n == 1)
		{
			ret = r[0];
		}
		if(n == 2)
		{
			ret = max(r[0], r[1]);
		}
		if(n == 3)
		{
			a = max(Dist(0, 1), r[2]*1.);
			b = max(Dist(0, 2), r[1]*1.);
			c = max(Dist(1, 2), r[0]*1.);

			ret = min(a, min(b, c));
		}

		printf("Case #%d: %lf\n", Case, ret);
	}

	return 0;
}
