#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
using namespace std;

#define REP(i, n) for(int i = 0; i<(n); i++)
#define abs(a) ((a) >= 0 ? (a) : -(a))
#define inf 2000000001
typedef vector<int> VI;
typedef vector<string> VS;

typedef long long i64;
typedef unsigned long long u64;

int n;
const string pat = "welcome to code jam";
int G[550][20];
string str;

int dp(int a, int b) {
	if (G[a][b] != -1) return G[a][b];
	if (b == pat.size()) return 1;
	if (a == str.size()) return 0;
	
	int ret = dp(a + 1, b);
	if (str[a] == pat[b]) ret = (ret + dp(a+1, b+1)) % 10000;
	return G[a][b] = ret;
}

int main() {
	cin>>n;
	getline(cin, str);
	REP(t, n) {
		getline(cin, str);
		memset(G, -1, sizeof(G));
		printf("Case #%d: %04d\n", t + 1, dp(0, 0));
		
	}
	return 0;
}