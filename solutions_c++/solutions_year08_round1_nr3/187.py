#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <functional>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
using namespace std;

#pragma warning(disable:4996)

typedef long long int64;
typedef int64 ll;


////////////////////////////////////////start///////////////////////////////////////////

int n;

int comb[31][31];
double p1[31];
double p2[31];
const double num = sqrt(5.0);
const double num2 = 3 + num;

void process() {
	comb[0][0] = 1;
	p1[0] = 1;
	p2[0] = 1;
	for (int i=1; i<=30; ++i) {
		comb[i][0] = 1;
		for (int j=1; j<=i; ++j)
			comb[i][j] = comb[i-1][j-1] + comb[i-1][j];

		p1[i] = p1[i-1] * 3;
		p2[i] = p2[i-1] * num;
	}
}

int dp[20] = {263, 151, 855, 527, 743, 351, 135, 407, 903, 791, 135, 647};

double truncate(double a) {
	return a - floor(a / 1000.0) * 1000;
}
void solve(int id) {
	int res;
	if (n < 19) {
		double t = 1;
		for (int i=0; i<n; ++i) t *= num2;
		res = truncate(t);
	}
	else {
		res = dp[n - 19];
	}
	
	printf("Case #%d: %03d\n", id, res);
}

int main() {
	freopen("d:/input.in", "r", stdin);
	freopen("d:/output.out", "w", stdout);
	process();
	int T;
	scanf("%d", &T);
	for (int id=1; id<=T; ++id) {
		scanf("%d", &n);
		solve(id);
	}
	return 0;
}