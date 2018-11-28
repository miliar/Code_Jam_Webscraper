#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cassert>
#include <string>
#include <cstdio>
#include <cmath>
#include <stack>
#define sz(x) ((int)(x.size()))
#define all(c) (c).begin(),(c).end() 
#define pb push_back 
#define mp make_pair
using namespace std;
typedef long long lint;
typedef pair<int, int> pii;
typedef vector<int> vi;
#pragma comment(linker, "/STACK:10000000")
int A[1000], N;
int D, I, M;

map<pair<int, int>, int> dp;

int rec(int a, int b) {
	if (a == b) return 0;		
	if (a < b) swap(a, b);
	if (a % b == 0) return 1;
	pair<int, int> p = make_pair(a, b);
	if (dp.count(p)) return dp[p];

	for (int i = 1; a - i * b > 0; ++i) {
		int t = rec(b, a - i * b);
		if (!t) return dp[p] = 1;
	}
	return dp[p] = 0;
}


void solve(int numTst) {
	int A1, A2, B1, B2;
	dp.clear();
	cin >> A1 >> A2 >> B1 >> B2;
	int ans = 0;
	for (int a = A1; a <= A2; ++a) {
		for (int b = B1; b <= B2; ++b) {
			if (rec(a, b)) ++ans;
		}
	}
	//int ans = rec(0, 256);
	printf("Case #%d: %d\n", numTst, ans);


}

int main() {	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; ++i) {
		solve(i);
	}
	return 0;
}

