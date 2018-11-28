#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <inttypes.h>
#include <ctype.h>
#include <algorithm>
#include <utility>
#include <iostream>
#include <queue>
using namespace std;
#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << "\n")
#define _inline(f...) f() __attribute__((always_inline)); f
#define _foreach(it, b, e) for (typeof(b) it = (b); it != (e); it++)
#define foreach(x...) _foreach(x)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
const int INF = 0x3F3F3F3F;
const int NULO = -1;
const double EPS = 1e-10;
_inline(int cmp)(double x, double y = 0, double tol = EPS) {
  return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

priority_queue<pair<int, int> > heap;

vector<int> clau[2010];
vector<int> resp;

int val[2010];

int main() {
  TRACE(setbuf(stdout, NULL));
	int C;
	scanf("%d", &C);
	foreach(_42, 1, C+1) {
		memset(val, 0, sizeof(val));
		foreach (i, 0, 2010) {
			clau[i].clear();
		}
		resp.clear();
		printf("Case #%d:", _42);
		int N, M;
		scanf("%d %d", &N, &M);
		foreach(i, 0, M) {
			int T;
			scanf("%d", &T);
			foreach(j, 0, T) {
				int A, B;
				scanf("%d %d", &A, &B);
				if (B == 0) {
					clau[i].push_back(A);
				} else {
					clau[i].push_back(-A);
				}
			}
		}
		int m = -1;
		while (1) {
			m = -1;
			foreach(i, 0, M) {
				if (val[i])
					continue;
				if (m > -1 && clau[i].size() >= clau[m].size())
					continue;
				if (clau[i][0] < 0)
					continue;
				m = i;
			}
			foreach(i, 0, M) {
				if (val[i])
					continue;
				if (m > -1 && clau[i].size() >= clau[m].size())
					continue;
				m = i;
			}

			if (m == -1 || val[m] || clau[m].size() != 1)
				break;
			if (clau[m][0] < 0)
				resp.push_back(-clau[m][0]-1);
			int var = clau[m][0];
			foreach(i, 0, M) {
				if (val[i])
					continue;
				foreach(j, 0, clau[i].size()) {
					if (clau[i][j] == var) {
						val[i] = 1;
						break;
					}
					if (clau[i][j] == -var) {
						clau[i][j] = clau[i][clau[i].size()-1];
						clau[i].pop_back();
						j--;
					}
				}
			}
		}
		if (m == -1) {
			sort(all(resp));
			foreach(i, 0, N) {
				if (binary_search(all(resp), i))
					printf(" 1");
				else
					printf(" 0");
			}
			printf("\n");
		}
		else if (val[m])
			printf(" IMPOSSIBLE\n");
		else if (clau[m].size() == 0)
			printf(" IMPOSSIBLE\n");
		else {
			sort(all(resp));
			foreach(i, 0, N) {
				if (binary_search(all(resp), i))
					printf(" 1");
				else
					printf(" 0");
			}
			printf("\n");
		}
			
	}

  return 0;
}
