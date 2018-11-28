#include <cstdio>
#include <iostream>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#include <climits>
#include <sstream>
using namespace std;

string p = "welcome to code jam";
int memo[25][600];
string x;

int calc(int pi, int xi)
{
	if (memo[pi][xi] >= 0) return memo[pi][xi];
	int ret = 0;
	
	if (pi == p.size() ) return 1;
	if (xi == x.size() ) return 0;
	
	if (p[pi] == x[xi]) ret += calc(pi + 1, xi + 1);
	ret += calc(pi, xi + 1);
	
	memo[pi][xi] = ret % 10000;
	
	return memo[pi][xi];
}

void solve(int pno)
{
	int i, j, k;
	
	memset(memo, 0xFF, sizeof(memo) );
	
	getline(cin, x);
	
	int ans = 0;
	
	ans = calc(0, 0);
	
	printf("Case #%d: %04d\n", pno, ans);
	
	return;
}

int main()
{
	int T;
	string s;
	
	getline(cin, s);
	istringstream iss(s);
	iss >> T;
	
	for (int i = 0; i < T; ++i) solve(i + 1);
	
	return 0;
}

