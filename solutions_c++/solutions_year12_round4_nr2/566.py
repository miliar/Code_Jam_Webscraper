#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

#include <algorithm>
#include <set>
#include <stack>
#include <vector>
#include <queue>

#define MAXN 2222
#define FOR(A, B) for(A=0; A<B; A++)

using namespace std;

int r[MAXN], x[MAXN], y[MAXN];
int perm[MAXN];
bool attempt(int w, int l, int n)
{
	int i;
	//do {
		int sum = 0, ysum = 0, ymax = 0;
		bool first = true, firstrow = true, ok = true;
		FOR(i, n) {
			if(sum + r[perm[i]] <= w) {
				if(!firstrow && ysum + r[perm[i]] > l) return false;
				x[perm[i]] = sum + r[perm[i]];
				y[perm[i]] = ysum + r[perm[i]];
				sum += 2*r[perm[i]];
				if(first) {
					first = false;
					x[perm[i]] = 0;
					sum -= r[perm[i]];
				}
				if(firstrow) {
					y[perm[i]] = 0;
					ymax = max(ymax, r[perm[i]]);
				} else ymax = max(ymax, 2*r[perm[i]]);
					
			} else {
				sum = 0; ysum += ymax;
				ymax = 0;
				firstrow = false;
				if(r[perm[i]] > w) { return false; }
				i--; continue;
			}
		}
		if(ok) return true;
	//} while(next_permutation(perm, perm+n) != NULL);
	return false;
}

int main(int argc, char* argv[])
{
	int i,j,k,m,o,a,b,z,t,T;
	FOR(i, 2222) perm[i] = i;
	freopen("C:\\B-large.in", "r", stdin);
	scanf("%d", &T);
	FOR(t, T) {
		int n,w,l;
		scanf("%d %d %d", &n, &w, &l);
		FOR(i, n) scanf("%d", r+i);
		if(attempt(w, l, n)) {
			printf("Case #%d: ", t+1);
			FOR(i, n) printf("%d %d ", x[i], y[i]);
			printf("\n");
		}
		else if(attempt(l, w, n)) {
			printf("Case #%d: ", t+1);
			FOR(i, n) printf("%d %d ", y[i], x[i]);
			printf("\n");
		}
	}
	return 0;
}