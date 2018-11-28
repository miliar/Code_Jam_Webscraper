#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>

using namespace std;

#define Eo(x) { cerr << #x << " = " << x << endl; }

typedef long long int64;
typedef double real;

#define inf 0x3f3f3f3f

#define maxn (1 << 6)
char matr[maxn][maxn];
int r[maxn];

int main() {
	int t = 1, tc;
	for(scanf("%d", &tc); t <= tc; t++) {
		printf("Case #%d:", t);
		int n, i, j;
		scanf("%d", &n);
		for(i = 0; i < n; i++)
			scanf(" %s", matr[i]);
		for(i = 0; i < n; i++)
			for(j = 0; j < n; j++)
				matr[i][j] -= '0';
		for(i = 0; i < n; i++) {
			for(j = n-1; j >= 0 && matr[i][j] == 0; j--);
			r[i] = j;
		}
		int ans = 0;
		for(i = 0; i < n; i++) {
			//for(j = 0; j < n; j++) fprintf(stderr, "%d ", r[j]); fprintf(stderr, "\n");
			for(j = i; j < n && r[j] > i; j++);
			assert(j < n);
			for(; j > i; j--, ans++)
				swap(r[j], r[j-1]);
		}
		printf(" %d\n", ans);
	}
	return 0;
}
