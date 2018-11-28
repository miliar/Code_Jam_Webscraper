#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include<fstream>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <string.h>
#define rep(x,n) for(int x=0;x<n;++x)
#define rep1(i,s) for(int i = 0; i < (int)s.size(); ++i)
#define mp(x,y) make_pair(x,y)
#define getBit(code, i) (code & (1 << i))
#define setBit(code, i) (code | (1 << i))
#define resetBit(code, i) (code & ~(1 << i))
#define PI acos(-1.0)
#define rd(x) scanf("%d", &x)
using namespace std;

struct tri
{
	int a, b, c;
	tri() {}
	tri(int a, int b, int c) : a(a), b(b), c(c) {}
};


bool cmp(pair<bool, bool> a, pair<bool, bool> b)
{
	if(a.first == b.first)
		return a.second < b.second;
	return a.first > b.first;
}

int main()
{
	freopen("input.in", "rt", stdin);
	freopen("output.in", "w", stdout);
	map<pair<int, int>, tri> mp;
	map<pair<int, int>, tri> smp;
	int arr[3];
	for(int i = 0; i <= 10; ++i)
	{
		for(int j = 0; j <= 10; ++j)
		{
			for(int k = 0; k <= 10; ++k)
			{
				arr[0] = i;
				arr[1] = j;
				arr[2] = k;
				sort(arr, arr+3);
				if(arr[2] - arr[1] < 2 && arr[1] - arr[0] < 2 && arr[2] - arr[0] < 2)
				{
					mp[make_pair(i + j + k, i)] = tri(i, j, k);
					mp[make_pair(i + j + k, j)] = tri(i, j, k);
					mp[make_pair(i + j + k, k)] = tri(i, j, k);
				}
				else if(arr[2] - arr[0] <= 2 && arr[1] - arr[0] <= 2 && arr[2] - arr[1] <= 2)
				{
					smp[make_pair(i + j + k, i)] = tri(i, j, k);
					smp[make_pair(i + j + k, j)] = tri(i, j, k);
					smp[make_pair(i + j + k, k)] = tri(i, j, k);
				}
			}
		}

	}

	int cases;
	rd(cases);
	int g[101], n, p, s, ss;
	pair<bool, bool> v[101];
	rep(c, cases)
	{
		rd(n);
		rd(s);
		rd(p);
		ss = 0;
		rep(i, n)
			v[i] = make_pair(0, 0);
		int count = 0;
		rep(i, n)
		{
			rd(g[i]);
			for(int j = p; j <= 10; ++j)
			{
				if(mp.count(make_pair(g[i], j)))
				{
					v[i].second = true;
					break;
				}
			}
			for(int j = p; j <= 10; ++j)
			{
				if(smp.count(make_pair(g[i], j)))
				{
					v[i].first = true;
					break;
				}
			}
		}
		sort(v, v + n, cmp);
		
		int counter = 0;
		ss = 0;
		rep(i, n)
			if(v[i].first && ss < s)
				ss += v[i].first;
			else
				counter += v[i].second;
		cout << "Case #" << c + 1 << ": " <<  counter + ss << endl;
	}
	return 0;
}