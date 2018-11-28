#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>

#include <iostream>
#include <sstream>
#include <string>

#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <algorithm>
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define FORN(i,a,n) for (int i = (a); i < (a)+(n); ++i)

//#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
//#define SIZE(x) int(x.size())

typedef pair<int,int> PII;
typedef long long ll;

/////////////////////////////////////////////////////////////////////////

void Solve(int testcase)
{
	printf("Case #%d: ", testcase+1);

	int N;
	scanf(" %d", &N);

	int sum = 0, vmin = 100000000, ksor = 0;

	FOR (i, 0, N) {
		int C;
		scanf(" %d", &C);

		sum += C;
		ksor ^= C;
		vmin = min(C, vmin);
	}

	if (ksor != 0)
		printf("NO\n");
	else
		printf("%d\n", sum - vmin);
}

int main()
{
	int T;
	scanf(" %d", &T);
	FOR (t, 0, T)
		Solve(t);
	
	return 0;
}
