#include <algorithm>
#include <cmath>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>

using namespace std;

#define fore(i,a) for(int i = 0; i < (a); i++)
#define fort(i,a) for(typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define x first
#define y second

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef long long ll;

#define err(...)
#define err(...) fprintf(stderr, __VA_ARGS__)

int x[44], y[44], r[44];

inline int sqr(int x)
{
	return x*x;
}

double getR(int a, int b)
{
	double dist = sqrt(sqr(x[a]-x[b]) + sqr(y[a]-y[b])) + r[a] + r[b];
	return .5 * dist;
}

void test()
{
	int n;
	r[0] = r[1] = r[2] = 0;
	scanf("%d", &n);
	fore(i,n) scanf("%d%d%d", &x[i], &y[i], &r[i]);
	if(n == 1)
	{
		printf("%d\n", r[0]);
		return;
	}
	if(n == 2)
	{
		printf("%d\n", max(r[0], r[1]));
		return;
	}
	if(n > 3)
	{
		printf("za duzo\n");
		return;
	}
	double res;
	res = max(getR(0,1), 1.*r[2]);
	res = min(res, max(getR(0,2), 1.*r[1]));
	res = min(res, max(getR(1,2), 1.*r[0]));
	printf("%lf\n", res);
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int tt = 1; tt <= T; tt++)
	{
		printf("Case #%d: ", tt);
		test();
	}
}
