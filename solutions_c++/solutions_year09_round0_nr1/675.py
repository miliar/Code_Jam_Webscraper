#include <cstdio>
#include <algorithm>
#include <vector>
#include <cassert>
#include <map>
#include <set>
#include <cmath>
#include <stack>
#include <queue>
#include <string>
#include <iostream>
using namespace std;
#define sz(a) (int)((a).size())
#define pb push_back
#define mp make_pair
#define all(a) (a).begin(), (a).end()
typedef pair<int, int> pii;
typedef vector<int> vint;
typedef long long lint;

int L, D, N;

char W[5005][20];

int Read()
{
	char c;
	while(1)
	{
		c = getchar();
		if(c >= 'a' && c <= 'z')
			return 1 << c - 'a';
		if(c == '(')
			break;
	}
	int ret = 0;
	while(1)
	{
		c = getchar();
		if(c == ')')
			return ret;
		ret += 1 << c - 'a';
	}
}

bool Solve(int test)
{
	scanf("%d %d %d", &L, &D, &N);
	for(int i = 0; i < D; ++i)
		scanf("%s", W[i]);
	int w[20];
	for(int k = 0; k < N; ++k)
	{
		for(int i = 0; i < L; ++i)
			w[i] = Read();
		int ans = 0;
		for(int i = 0; i < D; ++i)
		{
			bool ok = true;
			for(int j = 0; ok && j < L; ++j)
				if(!(w[j] & (1 << W[i][j] - 'a')))
					ok = false;
			if(ok)
				ans++;
		}
		printf("Case #%d: %d\n", k + 1, ans);
	}
	return false;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t = 0;
	/*scanf("%d", &t);
	for(int i = 1; i <= t; ++i)
		Solve(i);
	//*/while(Solve(++t));
	return 0;
}