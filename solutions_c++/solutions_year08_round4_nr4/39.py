#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <iostream>
#include <queue>
#include <set>
#include <map>

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define LD long double
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define DFOR(a,b) for(int a=b-1;a>=0;a--)
#define CLR(a,b) memset(a,b,sizeof(a))
#define inf 1000000

using namespace std;

char s[1005], t[1005];
int k;
int n;
int a[20];

void solvecase() {
	scanf("%d", &k);
	scanf("%s", s);
	n = strlen(s);
	FOR(i, k) a[i] = i;
	int res = inf;
	do {
		for (int i = 0; i < n; i+=k) {
			FOR(j, k) t[i+j] = s[i+a[j]];
		}
		int q = 1;
		for (int i = 1; i < n; i++) if (t[i] != t[i-1]) q++;
		res = min(res, q);
	} while (next_permutation(a, a+k));
	printf("%d", res);	
}

void solve() {
	int n;
	scanf("%d\n", &n);
	FOR(i, n) {
		printf("Case #%d: ", i+1);
		solvecase();
		printf("\n");
	}
}

int main() {
	freopen("x", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}