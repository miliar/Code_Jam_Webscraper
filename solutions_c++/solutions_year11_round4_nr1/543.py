#if 1
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <stack>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <functional>
#include <algorithm>
#include <cmath>
#include <bitset>
#include <cstdio>
#include <list>
#include <ctime>
using namespace std;

typedef long long LL;
typedef long double LD;
const LD eps = 1e-9;

typedef pair<int, int> pii;
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) cerr << #x << " = " << x << endl;
#define dbgv(x) { cerr << #x << ": {"; for(int i = 0; i < x.size(); ++i) { if(i) cerr << ", "; cerr << x[i]; } cerr << "}" << endl; }

struct swalk
{
	double len, w;
	swalk() { }
	swalk(double left, double right, double w) : len(right - len), w(w) { }
	swalk(double len, double w) : len(len), w(w) { }
};

bool cmpSpeed(const swalk &a, const swalk &b)
{
	return a.w < b.w;
}

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	int t; scanf("%d" , &t);
	for(int z = 0; z < t; ++z)
	{
		double s, r;
		double x;
		cin >> x;
		cin >> s >> r;
		double ti;
		cin >> ti;

		int n; cin >> n;
		vector<swalk> a(n);

		
		for(int i = 0; i < n; ++i)
		{
			double left, right;
			cin >> left >> right >> a[i].w;
			a[i].len = right - left;
			a[i].w += s;
			x -= a[i].len;
		}
		
		a.push_back(swalk(x, s));
		r -= s;
	
		sort(a.begin(), a.end(), cmpSpeed);

		for(int i = 0; i < a.size(); ++i)
		{
			if(ti > eps)
			{
				LD speed = a[i].w + r;
				LD time = a[i].len / speed;
				if(time < ti + eps)
				{
					a[i].w += r;
					ti -= time;
				} else
				{
					LD dist = ti * speed;
					a[i].len -= dist;
					a.pb(swalk(dist, speed));
					break;
				}
			} 
		}
		

		LD sum = 0.0;
		for(int i = 0; i < a.size(); ++i)
			sum += a[i].len / a[i].w;

		cout.precision(9);
		cout.setf(ios::fixed);
		cout << "Case #" << z + 1 << ": " << sum << endl;
		
		
	}
	return 0;
}
#endif

