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

bool Solve(int test)
{
	int N;
	scanf("%d", &N);
	vint A;
	for(int i = 0; i < N; ++i)
	{
		int a = 0;
		char buf[55];
		scanf("%s", buf);
		for(int j = 0; j < N; ++j)
			if(buf[j] == '1')
				a = j;
		A.pb(a);
	}
	int ans = 0;
	for(int i = 0; i < N; ++i)
	{
		int ix = i;
		while(A[ix] > i)
			ix++;
		for(int j = ix - 1; j >= i; --j)
		{
			ans++;
			swap(A[j], A[j + 1]);
		}
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
	int t = 0;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i)
		Solve(i);
	//*/while(Solve(++t));
	return 0;
}