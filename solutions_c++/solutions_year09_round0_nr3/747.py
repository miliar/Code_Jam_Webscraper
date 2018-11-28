/*
Problem: C
Set: GCJ 2009 qualification 
*/

#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
const int mod = 10000;
const string pattern = "welcome to code jam";
string text;
int dp[512][32];

int solve(int posInText, int patPos) {
	if (patPos == (int)pattern.size()) {
		return 1;
	} else if (posInText >= (int)text.size()) {
		return 0;
	}
	if (dp[posInText][patPos] != -1) {
		return dp[posInText][patPos];
	}
	dp[posInText][patPos] = solve(posInText + 1, patPos);
	if (text[posInText] == pattern[patPos]) {
		dp[posInText][patPos] += solve(posInText + 1, patPos + 1);
		dp[posInText][patPos] %= mod;
	}
	return dp[posInText][patPos];
}

int main() {
	freopen("input.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int N;
	scanf("%d", &N);
	int t;
	getline(cin, text);
	for (t = 1 ; t <= N ; ++t) {
		memset(dp, -1, sizeof(dp));
		getline(cin, text);
		printf("Case #%d: %04d\n", t, solve(0, 0));
	}
	return 0;
}

