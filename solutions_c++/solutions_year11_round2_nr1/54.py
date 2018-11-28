#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
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

#define sz(a) int((a).size())
#define all(X) (X).begin(), (X).end()
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;

const int MAXN = 128;

char matr[MAXN][MAXN];
int win[MAXN], lose[MAXN];
double wp[MAXN], owp[MAXN], oowp[MAXN];

void run()
{
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		scanf("%s", matr[i]);
		win[i] = lose[i] = 0;
	}
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			if (matr[i][j] == '1') {
				++win[i];
			}
			else if (matr[i][j] == '0') {
				++lose[i];
			}
		}
		wp[i] = double(win[i]) / (win[i] + lose[i]);
	}
	for (int i = 0; i < n; ++i) {
		double sum = 0;
		int ct = 0;
		for (int j = 0; j < n; ++j) {
			if (matr[i][j] == '1') {
				sum += double(win[j]) / (win[j] + lose[j] - 1);
				++ct;
			}
			else if (matr[i][j] == '0') {
				sum += double(win[j] - 1) / (win[j] + lose[j] - 1);
				++ct;
			}
		}
		owp[i] = sum / ct;
	}
	for (int i = 0; i < n; ++i) {
		double sum = 0;
		int ct = 0;
		for (int j = 0; j < n; ++j) {
			if (matr[i][j] == '1' || matr[i][j] == '0') {
				sum += owp[j];
				++ct;
			}
		}
		oowp[i] = sum / ct;
	}
	for (int i = 0; i < n; ++i) {
		printf("%.10f\n", wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25);
	}
}

int main()
{
	freopen("A1.in", "r", stdin);
	freopen("A1.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d:\n", i);
		run();
	}
	return 0;
}