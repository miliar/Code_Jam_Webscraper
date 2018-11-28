//#pragma comment(linker, "/STACK:10000000")
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <iostream>
#include <stack>
#include <queue>
#include <cmath>
using namespace std;
typedef long long lint;

vector<int> G[1001];

inline void AddEdge(int a, int b)
{
	G[a].push_back(b);
	G[b].push_back(a);
}

int Primes[1001];
int PC;
void PInit()
{
	Primes[PC++] = 2;
	for(int i = 3; i <= 1000; i += 2)
	{
		bool p = true;
		for(int j = 0; p && (j < PC); ++j)
		{
			if(i % Primes[j] == 0)
				p = false;
		}
		if(p)
			Primes[PC++] = i;
	}
}

bool Used[1001];
void DFSV(int u)
{
	Used[u] = true;
	for(int i = 0; i < G[u].size(); ++i)
	{
		int v = G[u][i];
		if(!Used[v])
			DFSV(v);
	}
}

bool Solve(int test)
{
	int A, B, P;
	scanf("%d %d %d", &A, &B, &P);
	int p = 0;
	while(p < PC && P > Primes[p])
		p++;
	for(int i = A; i <= B; ++i)
		G[i].clear();
	for(int i = A; i <= B; ++i)
		for(int j = i + 1; j <= B; ++j)
		{
			bool ok = false;
			for(int k = p; !ok && (k < PC) && Primes[k] <= B; ++k)
				if((i % Primes[k] == 0) && (j % Primes[k] == 0))
					ok = true;
			if(ok)
				AddEdge(i, j);
		}
	fill(Used + A, Used + B + 1, false);
	int ans = 0;
	for(int i = A; i <= B; ++i)
		if(!Used[i])
		{
			ans++;
			DFSV(i);
		}
	printf("Case #%d: %d\n", test, ans);
	return true;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	PInit();
	int t = 0;
	scanf("%d", &t);
	for(int i = 0; i < t; ++i)
		Solve(i + 1);
	//while(Solve(++t));
	return 0;
}