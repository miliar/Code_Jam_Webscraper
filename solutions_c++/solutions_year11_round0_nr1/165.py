#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long int64;
#define E(c) cerr<<#c
#define Eo(x) cerr<<#x<<" = "<<(x)<<endl

inline int uabs(int a) { return (a<0 ? -a : a); }
inline int sgn(int a){ return (a==0 ? 0 : (a < 0 ? -1 : 1)); }

int n;

int ans;

struct Task {
	int x;
	int ind;
	inline Task(int _x = 0, int _i = 0) : x(_x), ind(_i) {}
};                                             
vector<Task> arr[2];

int ox, bx;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%d", &n);

		arr[0].clear();
		arr[1].clear();
		for (int i = 0; i<n; i++) {
			char c;
			int k;
			scanf(" %c %d", &c, &k);
			if (c == 'O')
				arr[0].push_back(Task(k, i));
			else
				arr[1].push_back(Task(k, i));
		}

		ans = 0;
		int i = 0;
		int j = 0;
		ox = 1;
		bx = 1;
		while (i < arr[0].size() || j < arr[1].size()) {
//			printf("%d: %d(%d) %d(%d)\n", ans, ox, i, bx, j);
			bool of = (i < arr[0].size() && ox == arr[0][i].x);
			bool bf = (j < arr[1].size() && bx == arr[1][j].x);

			if (of && (j == arr[1].size() || arr[1][j].ind > arr[0][i].ind)) {
				i++;
				of = bf = false;
			}
			else {
				if (i < arr[0].size()) ox += sgn(arr[0][i].x - ox);
			}

			if (bf && (i == arr[0].size() || arr[0][i].ind > arr[1][j].ind)) {
				j++;
				of = bf = false;
			}
			else {
				if (j < arr[1].size()) bx += sgn(arr[1][j].x - bx);
			}

			ans++;
		}

		printf("Case #%d: %d\n", tt, ans);
		fflush(stdout);
	}
	return 0;
}
