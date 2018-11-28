#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int gcd(long long a, long long b)
{
   return a % b ? gcd(b, a%b) : b;
}

struct W
{
	int b, e, w;
};

double Time(double x, double w, double s, double r, double& t)
{
	double time = x / (w + r);
	if(time > t)
	{
		time = t + (x-t*(r+w)) / (w + s);
		t = 0;
	}
	else
		t -= time;
	return time;
}

struct Pr
{
	bool operator()(W w1, W w2)
	{
		return w1.w < w2.w;
	}
};

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("answer.txt", "w", stdout);
	int tc;
	cin>>tc;
	for(int Case = 0; Case < tc; Case++)
	{
		int x, s, r, T, n;
		cin >> x >> s >> r >> T >> n;
		double t = T;
		vector<W> v(n);
		double ans = 0;
		double pos = 0;
		double len = 0;
		for(int i = 0; i < n; ++i)
		{
			cin >> v[i].b >> v[i].e >> v[i].w;
			len += v[i].e - v[i].b;
		}
		sort(v.begin(), v.end(), Pr());
		ans += Time(x - len, 0, s, r, t);
		for(int i = 0; i < n; ++i)
		{
			ans += Time(v[i].e - v[i].b, v[i].w, s, r, t);
		}

		
		cout << "Case #" << Case + 1 <<": ";
		printf("%0.7lf\n", ans);
	}

	return 0;
}
