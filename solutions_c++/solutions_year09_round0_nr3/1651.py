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

const int MOD=10000;
const string msg = "welcome to code jam";
int dp[1000][25];
string text;

int go(int at, int k) {
	if (k==msg.size()) return (1 + go(at, 0))%MOD;
	if (at>=text.size()) return 0;
	int& ref = dp[at][k];
	if (ref!=-1) return ref;
	ref = 0;
	if (text[at]==msg[k]) ref = (ref + go(at+1,k+1))%MOD;
	ref = (ref + go(at+1,k))%MOD;
	return ref;
}

int solve() {
	memset(dp,-1,sizeof dp);
	getline(cin,text);
	return go(0,0);
}

int main() {
	int NCASES;
	cin >> NCASES;
	string tmp;
	getline(cin,tmp);
	for (int z=1;z<=NCASES;++z) {
		int res = solve();
		printf("Case #%d: %04d\n", z, res);
	}
}
