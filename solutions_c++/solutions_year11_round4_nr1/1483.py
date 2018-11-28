#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <cstring>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
using namespace std;

struct ww
{
	int b, e, s;
	bool operator<(const ww &w) const
	{
		return b < w.b;
	}
};

struct interval
{
	int start, end;
	int speed;
	int f;
	bool operator<(const interval &i) const
	{
		return speed < i.speed;
	}
};

vector<ww> v;
vector<interval> d;

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int numTests;
	cin >> numTests;
	int x, s, r, n;
	double t;
	ww temp;
	for(int test = 1; test <= numTests; test++)
	{
		v.clear();
		d.clear();
		cin >> x >> s >> r >> t >> n;
		for(int i = 0; i < n; i++)
		{
			scanf("%d%d%d", &temp.b, &temp.e, &temp.s);
			//cin >> temp.b >> temp.e >> temp.s;
			v.push_back(temp);
		}
		sort(v.begin(), v.end());
		int cur = 0;
		interval tmp;
		for(int i = 0; i < (int)v.size(); i++)
		{
			if(cur < v[i].b)
			{
				tmp.start = cur;
				tmp.end = v[i].b;
				tmp.speed = s;
				tmp.f = 0;
				d.push_back(tmp);
			}
			tmp.start = v[i].b;
			tmp.end = v[i].e;
			tmp.speed = v[i].s + s;
			tmp.f = 1;
			d.push_back(tmp);
			cur = v[i].e;
		}
		if(cur < x)
		{
			tmp.start = cur;
			tmp.end = x;
			tmp.speed = s;
			tmp.f = 0;
			d.push_back(tmp);
		}
		sort(d.begin(), d.end());
		double time = 0;
		int dist = 0;
		double curt;
		double left;
		double curd;
		for(int i = 0; i < (int)d.size(); i++)
		{
			dist = d[i].end - d[i].start;
			left = dist;
			if(t * (r + d[i].speed - s) >= dist)
			{
				curt = (double)dist / (r + d[i].speed - s);
				time += curt;
				t -= curt;
				left = 0;
			}
			else if(t > 0)
			{
				curd = t * (r + d[i].speed - s);
				time += t;
				t = 0;
				left = (double)dist - curd;
			}
			if(left > 0)
			{
				curt = left / d[i].speed;
				time += curt;
			}
		}
		cout << "Case #" << test << ": ";
		printf("%.9lf\n", time);
	}
	return 0;
}