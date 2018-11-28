#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long lol;

#define sz(c) ((int) (c).size())
#define pb push_back
#define mp make_pair
#define fi first
#define se second

int N;
int C[1111];

void solve(int testcase)
{
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) scanf("%d", &C[i]);
	int x = 0, s = 0;
	sort(C, C + N);
	for (int i = 0; i < N; ++i) 
	{
		x ^= C[i];
		s += C[i];
	}
	printf("Case #%d: ", testcase);
	if (x == 0) printf("%d\n", s - C[0]); else puts("NO");
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) solve(i);
	return 0;
}
