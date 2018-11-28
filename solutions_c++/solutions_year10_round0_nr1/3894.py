#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
using namespace std;

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)
#define ALL(c) (c).begin(), (c).end()



bool getState (int N, int K)
{
	REP (i, N)
	{
		int power = (int)pow(2, i);
		int quotient = K / power;
		int test = quotient % 2;
		if (test == 0) { return false; }
	}
	return true;
}

int main (int argc, char** argv)
{
	freopen("A-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int T;
	scanf("%d", &T);
	
	REP (i, T)
	{
		int N, K;
		scanf("%d%d", &N, &K);
		bool state = getState(N,K);
		if (state) { printf("Case #%d: ON\n", i+1); }
		if (!state) { printf("Case #%d: OFF\n", i+1); }
	}

	return 0;
}
