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
const long long int  INFL = 1000100000000100000LL;
const int N = 100000;
typedef long long int LL;
int t, n;
vector<LL> V;
LL l, ans, res, tmp;
int T[N];
void bfs(int k)
{
	int v, x;
	int w, wx;
	priority_queue<pair<int,int>, vector<pair<int,int> >, greater<pair<int,int> > > Q;
	for(int i = 0; i < k; ++i)
		T[i] = INF;
	Q.push(make_pair(0, 0));
	T[0] = 0;
	while(!Q.empty())
	{
		v = Q.top().second;
		x = Q.top().first;
		Q.pop();
		if(x != T[v])
			continue;
		for(int i = 0; i < n; ++i)
		{
			w = v + V[i];
			wx = x + 1;
			if(w >= k)
			{
				w -= k;
				wx--;
			}
			if(T[w] > wx)
			{
				Q.push(make_pair(wx, w));
				T[w] = wx;
			}
		}
	}
	return;
}
int main()
{
	int i, j, k;
	ios_base::sync_with_stdio(false);
	cin >> t;
	for(int testCase = 1; testCase <= t; ++testCase)
	{
		cin >> l >> n;
		V.resize(n);
		for(i = 0; i < n; ++i)
			cin >> V[i];
		ans = INFL;
		for(i = 0; i < n; ++i)
		{
			bfs(V[i]);
	//		cout << l % V[i] << " " << T[l % V[i]] << endl;
			if(T[l % V[i]] == INF)
				continue;
			ans = min(LL(l / V[i]) + LL(T[l % V[i]]), ans);
		}
		cout << "Case #" << testCase << ": ";
		if(ans == INFL)
			cout << "IMPOSSIBLE";
		else
			cout << ans;
		cout << endl;
	}
}
