#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <cstring>

using namespace std;

const string wel="welcome to code jam";
string cur;

const int MOD=10000;

int dp[510][20];

int solve(int ci, int wi) {
	int& r = dp[ci][wi];
	if (r >= 0)
		return r;
	if (wi == wel.length())
		return r = 1;
	if (ci == cur.length())
		return r = 0;
	r = 0;
	if (cur[ci] == wel[wi])
		r = solve(ci+1, wi+1);
	r += solve(ci+1,wi);
	r %= MOD;
	return r;
}

int solve(const string& s) {
	memset(dp,-1,sizeof(dp));
	cur = s;
	return solve(0,0);
}

string Solve(const string& s) {
	char res[5];
	sprintf(res, "%04d", solve(s));
	return string(res);
}

int main() {
	int N;
	cin >> N;
	string s;
	getline(cin, s);
	for (size_t c=1;c<=N;c++) {
		getline(cin, s);
		cout << "Case #" << c << ": " << Solve(s) << endl;
	}

	return 0;
}
