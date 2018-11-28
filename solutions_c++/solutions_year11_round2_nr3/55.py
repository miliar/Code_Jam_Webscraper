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

const int MAXN = 8;

int bestarr[MAXN];
int bestc;

int conn[MAXN][MAXN];
int n, m;
int from[MAXN], to[MAXN];

int arr[MAXN];

bool isok(int arr[MAXN])
{
	int maxx = 0;
	bool has[MAXN] = {false};
	for (int i = 0; i < n; ++i) {
		maxx = max(maxx, arr[i]);
		has[arr[i]] = true;
	}
	for (int i = 0; i <= maxx; ++i) {
		if (!has[i]) return false;
	}
	return true;
}

int calnc(int arr[MAXN])
{
	int maxx = 0;
	for (int i = 0; i < n; ++i) {
		maxx = max(maxx, arr[i]);
	}
	return maxx + 1;
}

void gonext(int arr[MAXN])
{
	for (int i = n - 1; i >= 0; --i) {
		if (arr[i] == n - 1) {
			arr[i] = 0;
		}
		else {
			++arr[i];
			return;
		}
	}
}

void run()
{
	scanf("%d %d", &n, &m);
	for (int i = 0; i < m; ++i) {
		scanf("%d", from + i);
		--from[i];
	}
	memset(conn, 0, sizeof(conn));
	for (int i = 0; i < m; ++i) {
		scanf("%d", to + i);
		--to[i];
		conn[from[i]][to[i]] = conn[to[i]][from[i]] = 1;
	}
	for (int i = 0; i < n; ++i) {
		arr[i] = bestarr[i] = 0;
	}
	bestc = 1;
	int tot = 1;
	for (int i = 0; i < n; ++i) {
		tot *= n;
	}
	vector<int> vv;
	vv.push_back((1 << n) - 1);
	for (int i = 0 ; i < m; ++i) {
		int msk = (1 << from[i]) | (1 << to[i]);
		for (int j = 0; j < sz(vv); ++j) {
			if ((vv[j] & msk) == msk) {
				int n1 = msk, n2 = msk;
				for (int k = 0; k < n; ++k) {
					if (vv[j] & (1 << k)) {
						if (k <= from[i] || k >= to[i]) {
							n1 |= 1 << k;
						}
						else {
							n2 |= 1 << k;
						}
					}
				}
				vv.erase(vv.begin() + j);
				vv.push_back(n1);
				vv.push_back(n2);
				break;
			}
		}
	}
	while (tot--) {
		int nc = calnc(arr);
		if (isok(arr) && nc > bestc) {
			bool isisok = true;
			for (int i = 0; i < sz(vv) && isisok; ++i) {
				bool has[MAXN] = {false};
				for (int j = 0; j < n; ++j) {
					if (vv[i] & (1 << j)) {
						has[arr[j]] = true;
					}
				}
				for (int j = 0; j < nc; ++j) {
					if (!has[j]) {
						isisok = false;
						break;
					}
				}
			}
			if (isisok) {
				memcpy(bestarr, arr, sizeof(bestarr));
				bestc = nc;
			}
		}
		gonext(arr);
	}
	printf("%d\n", bestc);
	for (int i = 0; i < n; ++i) {
		printf("%d%c", bestarr[i] + 1, i == n - 1 ? '\n' : ' ');
	}
}

int main()
{
	freopen("C1.in", "r", stdin);
	freopen("C1.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: ", i);
		run();
	}
	return 0;
}