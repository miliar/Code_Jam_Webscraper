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

using namespace std;

int k, n;
int a[1000006];

int calc(int x) {
	int t = 0, s = k-x;
	for (int i = x; i > 0; i--) {
		t = (t + i) % s;
		t++;
		s++;
	}
	return t;
}

int calcrev(int t) {	
	int s = k;
	for (int i = 1; t != 0; i++) {
		s--;
		t--;
		t = (t-i%s+s) % s;
	}
	return k-s;
}

void solvecase() {
	scanf("%d%d", &k, &n);
	//FOR(i, k) a[calc(i)] = i;
	FOR(i, n) {
		int t;
		scanf("%d", &t);
		//int res = a[t-1]+1;
		int res2 = calcrev(t-1) + 1;
		//if (res != res2) {
		//	printf("\n! %d %d\n", res, res2);
		//}
		printf("%d ", res2);
	}
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
	freopen("y", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}