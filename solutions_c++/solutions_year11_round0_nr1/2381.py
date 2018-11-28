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

int n;
string R[111];
int P[111];

void solve(int testcase)
{
	cin >> n;
	for (int i = 0; i < n; ++i) cin >> R[i] >> P[i];

	vector <int> b, o;
	for (int i = 0; i < n; ++i)
		if (R[i] == "B") b.pb(P[i]); else o.pb(P[i]);

	int B = 1, O = 1, bb = 0, oo = 0, res = 0;
	for (int i = 0; i < n; )
	{
		++res;
		if (R[i] == "B" && P[i] == B)
		{
			++i;
			++bb;
			if (oo < sz(o))
			{
				if (O > o[oo]) --O;
				if (O < o[oo]) ++O;
			}
			continue;
		}
		
		if (R[i] == "O" && P[i] == O)
		{
			++i;
			++oo;
			if (bb < sz(b))
			{
				if (B > b[bb]) --B;
				if (B < b[bb]) ++B;
			}
			continue;
		}

		if (bb < sz(b))
		{
			if (B > b[bb]) --B;
			if (B < b[bb]) ++B;
		}

		if (oo < sz(o))
		{
			if (O > o[oo]) --O;
			if (O < o[oo]) ++O;
		}
	}

	printf("Case #%d: %d\n", testcase, res);
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) solve(i);
	return 0;
}
