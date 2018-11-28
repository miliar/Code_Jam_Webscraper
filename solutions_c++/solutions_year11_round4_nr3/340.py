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

vector<int> ps[1024];
vector<int> pns[1024];

void initial()
{
	for (int i = 2; i <= 1000; ++i) {
		int n = i;
		for (int j = 2; j * j <= n; ++j) {
			if (n % j == 0) {
				ps[i].push_back(j);
				int ct = 0;
				while (n % j == 0) {
					n /= j;
					++ct;
				}
				pns[i].push_back(ct);
			}
		}
		if (n != 1) {
			ps[i].push_back(n);
			pns[i].push_back(1);
		}
	}
}

int run()
{
	int minn = 0, maxx = 0;
	int n;
	int arr[1024];
	scanf("%d", &n);
	memset(arr, 0, sizeof(arr));
	maxx = 1;
	for (int i = 2; i <= n; ++i) {
		bool isok = true;
		for (int j = 0; j < sz(ps[i]); ++j) {
			int p = ps[i][j];
			int pn = pns[i][j];
			if (pn > arr[p]) {
				isok = false;
				break;
			}
		}
		if (!isok) {
			++maxx;
			for (int j = 0; j < sz(ps[i]); ++j) {
				int p = ps[i][j];
				int pn = pns[i][j];
				arr[p] = max(arr[p], pn);
			}
		}
	}
	memset(arr, 0, sizeof(arr));
	for (int i = n; i >= 2; --i) {
		bool isok = true;
		for (int j = 0; j < sz(ps[i]); ++j) {
			int p = ps[i][j];
			int pn = pns[i][j];
			if (pn > arr[p]) {
				isok = false;
				break;
			}
		}
		if (!isok) {
			++minn;
			for (int j = 0; j < sz(ps[i]); ++j) {
				int p = ps[i][j];
				int pn = pns[i][j];
				arr[p] = max(arr[p], pn);
			}
		}
	}
	minn = 0;
	for (int i = 0; i <= 1000; ++i) {
		if (arr[i] != 0) {
			++minn;
		}
	}
	if (minn == 0) minn = 1;
	return maxx - minn;
}

int main()
{
	freopen("C1.in", "r", stdin);
	freopen("C1.out", "w", stdout);
	initial();
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: %d\n", i, run());
	}
	return 0;
}