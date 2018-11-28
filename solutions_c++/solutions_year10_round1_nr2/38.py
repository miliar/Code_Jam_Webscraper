#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

const int INF=1<<28;
int D,I,M,N;
int V[300];
int dp[300][300][2];

int cost(int cur, int prev) {
	if (prev==-1) return I;
	int diff = abs(cur-prev);
	if (M==0) return cur == prev ? I : INF;
	return max(I, I * ((diff+M-1)/M));
}

int go(int at, int prev, bool ins) {
	if (at>=N) return 0;
	int& ref = dp[at][prev+1][ins];
	if (ref!=-1) return ref;
	ref = go(at+1,prev,0) + D;
	for (int i=0;i<=255;++i) {
		if (prev == -1 || abs(i-prev) <= M) {
			ref = min(ref, go(at+1,i,0) + abs(i-V[at]));
		}
		if (!ins) {
			ref = min(ref, go(at,i,1) + cost(i,prev));
		}
	}
	return ref;
}

int main() {
	int ncases;
	cin >> ncases;
	for (int z=1;z<=ncases;++z) {
		cin >> D >> I >> M >> N;
		for (int i=0;i<N;++i) cin >> V[i];
		memset(dp,-1,sizeof dp);
		printf("Case #%d: %d\n", z, go(0,-1,0));
	}
}
