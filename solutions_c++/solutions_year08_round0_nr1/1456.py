#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

#define MAXN 128
#define MAXLEN 128
#define MAXQ 1024

int s, q;

map<string, int> eng2num;

int query[MAXQ];

int dp[MAXN][MAXQ];

int calc_dp(int x, int y) {
	if(y >= q) return 0;

	int& res = dp[x][y];
	if(res != -1) return res;

	if(y == q-1) return res = ((query[y] == x) ? 1 : 0);

	if(query[y] != x) return res = calc_dp(x, y+1);
	
	res = 1000000000;

	for(int i=1; i<=s; ++i)
		if(i != x)
		{
			int curr = calc_dp(i, y+1) + ((i==x) ? 0 : 1);
			res = min(res, curr);
		}

	return res ;
}

void init() {
	string str;
	char buf[1024], ch;

	cin >> s;
	cin.getline(buf, MAXLEN); // Read all bulsheads to the end of the line.	

	eng2num.clear();

	for(int i=0; i<s; ++i)	
	{
		cin.getline(buf, MAXLEN);	
		str = buf;
		eng2num[str] = i + 1;
	}

	cin >> q;
	cin.getline(buf, MAXLEN); // Read all bulsheads to the end of the line.	
	
	for(int i=0; i<q; ++i)
	{
		cin.getline(buf, MAXLEN);
		str = buf;
		query[i] = eng2num[str];		
	}

}

int solve() {
	for(int i=0; i<MAXN; ++i)
		for(int j=0; j<MAXQ; ++j)
			dp[i][j] = -1;

	int res = 1000000000;
	for(int i=1; i<=s; ++i)
		res = min(res, calc_dp(i, 0));

	return res;
}


int main(void) {
	int t;
	freopen("A-large.in", "r", stdin);
	freopen("A-small-attempt.out", "w", stdout);

	cin >> t;
	for(int i = 1; i <= t; i++) {
		init();
		cout << "Case #" << i << ": " << solve() << endl;
	}
	return 0;
}
