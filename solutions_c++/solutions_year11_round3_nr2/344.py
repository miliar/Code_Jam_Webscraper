#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
using namespace std;

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	cin >> tests;
	long long l, n, c;
	long long t;
	vector<long long> v;
	vector<long long> d;
	for(int test = 1; test <= tests; test++)
	{
		cin >> l >> t >> n >> c;
		v.clear();
		v.resize(c);
		for(int i = 0; i < c; i++)
			cin >> v[i];
		d.clear();
		d.resize(n);
		int idx = 0;
		while(idx < n)
		{
			for(int i = 0; i < v.size(); i++)
			{
				if(idx < n)
				{
					d[idx] = v[i];
					idx++;
				}
			}
		}
		long long whole = 0;
		for(int i = 0; i < n; i++)
		{
			whole += d[i];
		}
		whole *= 2;
		long long time = 0;
		idx = 0;
		for(int i = 0; i < n; i++)
		{
			time += 2 * d[i];
			if(time >= t)
			{
				idx = i;
				break;
			}
		}
		vector<long long> w;
		for(int i = idx + 1; i < n; i++)
			w.push_back(d[i]);
		
		if(time > t)
		{
			long long tt = time - t;
			if(tt % 2 == 0)
				tt /= 2;
			else
			{
				tt /= 2;
				tt++;
			}
			w.push_back(tt);
		}
		sort(w.rbegin(), w.rend());
		long long dist = 0;
		if(w.size() < l)
		{
			for(int i = 0; i < w.size(); i++)
				dist += w[i];
		}
		else
		{
			for(int i = 0; i < l; i++)
			{
				dist += w[i];
			}
		}
		long long res = whole - dist;
		cout << "Case #" << test << ": " << res << endl;
	}
	return 0;
}