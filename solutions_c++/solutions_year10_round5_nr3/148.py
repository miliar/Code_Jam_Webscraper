#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <string.h>
#include <algorithm>
#define FOREACH(it, C) for(typeof((C).begin()) it = (C).begin(); it != (C).end(); ++it)
using namespace std;
const int INF = 1000000100;
const int N = 20000000, Z = 10000000;
typedef long long int LL;
int t, n, v, x;
vector<pair<int, int> > V;
priority_queue<pair<int,int> > Q;
int T[N];
LL ans;
int main()
{
	int i, j, k;
	ios_base::sync_with_stdio(false);
	cin >> t;
	for(int testCase = 1; testCase <= t; ++testCase)
	{
		cin >> n;
		V.resize(n);
		ans = 0;
		memset(T, 0, sizeof(T));
		for(int i = 0; i < n; ++i)
		{
			cin >> V[i].second >> V[i].first;
			V[i].second += Z;
			T[V[i].second] = V[i].first;
			if(V[i].first > 1)
				Q.push(V[i]);
		}
		while(!Q.empty())
		{
			v = Q.top().second;
			x = Q.top().first;
			Q.pop();
		//	cout << v << " " << x << " " << T[v] << endl;
			if(T[v] != x)
				continue;
			ans += (x >> 1);
			T[v - 1] += (x >> 1);
			T[v + 1] += (x >> 1);
			T[v] &= 1;
			if(T[v - 1] > 1)
				Q.push(make_pair(T[v - 1], v - 1));
			if(T[v + 1] > 1)
				Q.push(make_pair(T[v + 1], v + 1));
		}
		cout << "Case #" << testCase << ": " << ans << endl;
	}
}
