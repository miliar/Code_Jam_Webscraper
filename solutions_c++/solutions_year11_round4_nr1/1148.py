#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<set>
#include<map>
#include<fstream>
#define epsilon 1e-11
#define cosinusa(a, b, c) ((a * a + b * b - c * c) / (2.0 * a * b));
#define infi 1000000000
using namespace std;

int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d: ", testCounter + 1);
		double x, w, t, r;
		cin >> x >> w >> r >> t;
		int n;
		cin >> n;
		double time = 0;
		double b, e, s;
		double len = 0;
		vector<pair<double, double> > v;
		pair<double, double> p;
		double total = 0;
		for(int i = 0; i < n; i++)
		{
			cin >> b >> e >> s;
			len = e - b;
			total += len;
			p.first = s;
			p.second = e - b;
			v.push_back(p);
		}
		p.first = 0;
		p.second = x - total;
		v.push_back(p);
		sort(v.begin(), v.end());
		double cur = 0;
		double step = 1e8;
		double minm = 1e9;
		double temp;
		double left;
		while(step > epsilon)
		{
			cur += step;
			if(cur > t)
			{
				cur -= step;
				step /= 2.0;
				continue;
			}
			left = cur;
			temp = 0;
			for(int i = 0; i < v.size(); i++)
			{
				if(left + epsilon > v[i].second / ( v[i].first + r))
				{
					left -= v[i].second / ( v[i].first + r);
					temp += v[i].second / ( v[i].first + r);
				}
				else if(left > epsilon)
				{
					temp += left;
					temp += (v[i].second - left * ( v[i].first + r)) / ( v[i].first + w); 
					left = 0.0;
				}
				else 
					temp += v[i].second / ( v[i].first + w); 
			}
			if(temp < minm)
				minm = min(minm, temp);
			step /= 2.0;
		}
		printf("%.9lf\n", minm);
	}
	return 0;
}
