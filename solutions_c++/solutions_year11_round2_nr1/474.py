#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long lol;

#define sz(c) ((int) (c).size())
#define pb push_back
#define mp make_pair
#define fi first
#define se second

int n;
char a[111][111];
double wp[111], owp[111], oowp[111], rpi[111];
int games[111], wins[111];

void solve(int testcase)
{
	printf("Case #%d:\n", testcase);
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) scanf("%s", a[i]);
	for (int i = 0; i < n; ++i) {
		games[i] = wins[i] = 0;
		for (int j = 0; j < n; ++j) {
			if (a[i][j] != '.') ++games[i];
			if (a[i][j] == '1') ++wins[i];
		}
		wp[i] = 1.0 * wins[i] / games[i];
	}
	for (int i = 0; i < n; ++i) {
		int count = 0;
		owp[i] = 0.0;
		for (int j = 0; j < n; ++j)
			if (a[i][j] != '.') {
				owp[i] += 1.0 * (wins[j] - (a[j][i]-'0')) / (games[j]-1), ++count;
			}
		owp[i] /= count;
	}
	for (int i = 0; i < n; ++i) {
		int count = 0;
		oowp[i] = 0.0;
		for (int j = 0; j < n; ++j)
			if (a[i][j] != '.') oowp[i] += owp[j], ++count;
		oowp[i] /= count;
	}
	for (int i = 0; i < n; ++i)
		rpi[i] = 0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i];
	for (int i = 0; i < n; ++i)
		printf("%.10lf\n", rpi[i]);
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) solve(i);
	return 0;
}
