#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

const double eps = 1e-8;

bool Equal(double a, double b)
{
	return fabs(a-b) < eps;
}

bool Less(double a, double b)
{
	return a < b && (!Equal(a, b));
}

bool Great(double a, double b)
{
	return a > b && (!Equal(a, b));
}

int x, s, r, t, n;
int b[10000], e[10000], w[10000];

void Scan()
{
	scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
	for (int i = 0; i < n; i++)
		scanf("%d%d%d", &b[i], &e[i], &w[i]);
}

vector<pair<int,int>> v;

double ans;

void Solve()
{	
	int rem = x;
	while (!v.empty())
	{
		v.pop_back();
	}
	ans = 0;
	for (int i = 0; i < n; i++)
	{
		v.push_back(make_pair(w[i], e[i]-b[i]));
		rem -= v[i].second;
	}
	if (rem > 0)
		v.push_back(make_pair(0, rem));
	sort(v.begin(), v.end());
	double t1 = t;
	//for (int i = ((int)v.size())-1; i >= 0; i--)
	for (int i = 0; i < v.size(); i++)
	{
		if (!Equal(t1, 0))
		{
			double t2 = (v[i].second/(double)(v[i].first+r));
			if (Less(t1, t2))
			{
				t2 = t1;			
			}
			t1 -= t2;
			ans += t2;
			ans += ((v[i].second - t2*(v[i].first+r)) / (double)(v[i].first+s));
		}
		else
			ans += ((v[i].second) / (double)(v[i].first+s));		
	}
	printf("%.9lf\n", ans);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		Scan();
		printf("Case #%d: ", i+1);
		Solve();
	}
	return 0;
}