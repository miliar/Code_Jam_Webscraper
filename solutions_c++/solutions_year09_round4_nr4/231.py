#include <iostream>
#include <cmath>
using namespace std;

const int MAXN = 40;
const int MAXN3 = MAXN*MAXN*MAXN;

int x[MAXN], y[MAXN], r[MAXN];
int n, n3;
bool mark[MAXN3][MAXN];
double cr[MAXN3], cx[MAXN3], cy[MAXN3];
int ind[MAXN];
bool footmark[MAXN];

void read()
{
	cin >> n;
	for(int i=0; i<n; i++)
		cin >> x[i] >> y[i] >> r[i];
}

inline double sqr(double a)
{
	return a*a;
}

double solve()
{
	double res = 2e10;
	if (n <= 2){
		res = 0;
		for(int i=0; i<n; i++)
			res = max(res, (double)r[i]);
		return res;
	}
	if (n > 3)
		return -1;
	for(int i=0; i<n; i++)
		for(int j=0; j<i; j++)
		{
			double d = sqrt(sqr(x[i]-x[j])+sqr(y[i]-y[j]));
			d += r[i]+r[j];
			res = min(res, d/2);
		}
	return res;
}

int main()
{
	int C;
	cin >> C;
	for(int ic=0; ic<C; ic++)
	{
		read();
		printf("Case #%d: %lf\n", ic+1, solve());
	}
}

