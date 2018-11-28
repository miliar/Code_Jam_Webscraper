#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <cstdio>
#include <cassert>
#include <vector>
#include <map>
#include <string>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <set>
using namespace std;

#define REP(i,n) for(int i = 0; i < n; i++)

void openfiles()
{
#ifndef ONLINE_JUDGE
	//string file = "test";
	string file = "C-large";
	freopen((file + ".in").c_str(),"rt",stdin);
	freopen((file + ".out").c_str(),"wt",stdout);
#endif
}

// return next person, euro
pair<int, int> ride(vector<int> groups, int start, int mx) {
	int k = groups.size();
	int cur = 0;
	for (int i = 0; i < k; i++) {
		if (cur + groups[(i+start)%k] > mx) {
			return make_pair((i+start)%k, cur);
		}
		cur += groups[(i+start)%k];
	}
	return make_pair(start, cur);
}

#define SOLVE_VOID
#ifdef SOLVE_VOID
void solve(int test)
{
	int R, k, N;
	scanf("%d %d %d ",&R, &k, &N);
	vector<int> groups(N);
	REP(i,N) scanf("%d",&groups[i]);

	set<int> been;
	int last = 0;
	long long output = 0;
	int vis[1001]; memset(vis, 0, sizeof(vis));
	long long cnt[1001]; memset(cnt, 0, sizeof(cnt));
	int r = 0;
	for (; r < R && been.find(last) == been.end(); r++) {
		been.insert(last);
		vis[last] = r;
		cnt[last] = output;
		pair<int,int> p = ride(groups, last, k);
		output += p.second;
		last = p.first;
	}
	long long cycleEuro = output - cnt[last];
	long long cycleLen = r - vis[last];
	R -= r;

	if (R > 0) {
		int cycleRepeats = R / cycleLen;
		output += cycleRepeats * cycleEuro;
		R -= cycleRepeats * cycleLen;
		for (int r = 0; r < R; r++) {
			pair<int,int> p = ride(groups, last, k);
			output += p.second;
			last = p.first;
		}
	}

	static int ntest = 0;
	printf("Case #%d: %lld\n",++ntest,output);
}
#endif

int main()
{
	openfiles();
	#ifdef SOLVE_BOOL
		while(solve());
	#endif
	#ifdef SOLVE_VOID
		int n; scanf("%d ",&n); REP(i,n) solve(i);
	#endif
	
	return 0;
}