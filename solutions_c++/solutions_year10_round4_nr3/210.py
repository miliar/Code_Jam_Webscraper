#define _CRT_SECURE_NO_DEPRECATE

#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <string.h>

using namespace std;

#define pb push_back
#define pf push_front
#define mp make_pair
#define fi(a, b) for(i=a; i<=b; i++)
#define fj(a, b) for(j=a; j<=b; j++)
#define fo(a, b) for(o=a; o<=b; o++)
#define fdi(a, b) for(i=a; i>=b; i--)
#define fdj(a, b) for(j=a; j>=b; j--)
#define fdo(a, b) for(o=a; o>=b; o--)
#define ZERO(x) memset(x, 0, sizeof(x));
#define COPY(x, y) memcpy(x, y, sizeof(y));
#define SIZE(x) (int)x.size()
#define LEN(x) (int)x.length()

typedef long long int64;

int test, testq;

#define MAX 200

int n = 110;
int matr[MAX][MAX];
int matr2[MAX][MAX];
int q;

int ans;

bool Fun() {
	int i, j;
	int f;
	ZERO(matr2);
	f = 0;
	fj(1, n) {
		fi(1, n) {
			if (matr[j][i]) {f = 1;}
			if (!matr[j][i] && matr[j - 1][i] && matr[j][i - 1]) {
				matr2[j][i] = 1;
			}
			if (matr[j][i] && (matr[j - 1][i] || matr[j][i - 1])) {
				matr2[j][i] = 1;
			}
		}
	}
	if (!f) return false;
	COPY(matr, matr2);
	return true;
}

int main() {
	int i, j, o;
	int x1, y1, x2, y2;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &testq);
	for (test = 1; test <= testq; test++) {
		printf("Case #%d: ", test);
		scanf("%d", &q);
		fo(1, q) {
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			fj(y1, y2) {
				fi(x1, x2) {
					matr[j][i] = 1;
				}
			}
		}
		ans = 0;
		while (Fun()) ans++;
		printf("%d\n", ans);
	}
	return 0;
}
