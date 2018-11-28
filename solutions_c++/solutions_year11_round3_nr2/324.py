#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <numeric>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define eps 1e-10
#define inf 0x3f3f3f3f

#define console cout
#define dbg(x) console << #x << " == " << x << endl
#define print(x) console << x << endl

long long L, t, N, C;
long long tracks[1<<20];
long long acumula[1<<20];

long long dp[1<<10][4];

long long solve(int idx, int rem){
	long long &ret = dp[idx][rem];
	if(ret != -1)return ret;
	if(idx == N)return ret = 0;
	ret = 2*tracks[idx] + solve(idx+1, rem);
	if(acumula[idx] > t/2 && rem){
		int k;
		if(idx == 0)k = t;
		else k = max(t-2*acumula[idx-1], 0LL);
		ret = min(ret, (k/2 + tracks[idx]) + solve(idx+1, rem-1));
	}
	return ret;
}
void process(){
	int i;
	long long ret = 0;
	for(i = 0; i < N && ret+2*tracks[i] <= t; i++){
		ret += 2*tracks[i];
	}
	//printf("i(%d) [%lld]\n", i, tracks[i]);
	if(i == N){
		cout << ret << endl;
		return;
	}
	int k;
	if(i == 0)k = t;
	else k = max(t-2*acumula[i-1], 0LL);
	tracks[i] -= k/2;
	ret = t;
	sort(tracks+i, tracks+N, greater<int>());
	int tt;
	for(tt = 0; tt < L && i+tt < N; tt++){
		//printf("i+tt(%d) [%lld]\n", i+tt, tracks[i+tt]);
		ret += tracks[i+tt];
	}
	i += tt;
	for(; i < N; i++){
		//printf("i(%d) [%lld]\n", i, tracks[i]);
		ret += 2*tracks[i];
	}
	cout << ret << endl;
}
int read(){
	cin >> L >> t >> N >> C;
	for(int i = 0; i < C; i++)cin >> tracks[i];
	for(int i = C; i < N; i++)tracks[i] = tracks[i%C];
	acumula[0] = tracks[0];
	for(int i = 1; i < N; i++){
		acumula[i] = acumula[i-1] + tracks[i];
	}
	return 1;
}

// BEGIN CUT HERE
int main() {
//freopen("out.txt","w",stdout);
//freopen("out.txt","w",stderr);
	int casos;
	scanf("%d", &casos);
	for(int i = 1; i <= casos && read(); i++){
		fprintf(stderr, "i(%d)\n", i);
		printf("Case #%d: ", i);
		process();
	}
	return 0;
}
// END CUT HERE 
