#pragma comment(linker,"/STACK:32000000")
#include <stdio.h>
#include <iostream>
#include <sstream>
#include <queue>
#include <algorithm>
#include <vector>
#include <math.h>
#include <set>
#include <map>
#include <string>

using namespace std;

#define infile ".in"
#define outfile ".out"
#define FOR(i, n) for (int i = 0; i <(n); i++)
#define DFOR(i, n) for (int i = (n) - 1; i >= 0; i--)
#define PB push_back
#define MP make_pair
#define ALL(x) x.begin(), x.end()
#define LL long long
#define SQR(x) ((x) * (x))
#define ABS(x) ((x) < 0 ? -(x) : (x))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define CLR(a, b) memset((a), (b), sizeof(a))
#define SS stringstream
#define PII pair<int, int>
#define VPII vector < PII >

void init(){
	freopen(infile, "r", stdin);
	freopen(outfile, "w", stdout);
}

#define maxn 50

int n;
int a[maxn];
int ans = 0;

void solvecase(){
	ans = 0;
	FOR(i, n){
		for(int j=i; j<n; j++)if(a[j]<=i){
			ans += j-i;
			for(int k=j; k>i; k--) a[k] = a[k-1];
			break;
		}
	}
	printf("%d\n", ans);
}

void solve(){
	int t;
	scanf("%d\n", &t);
	FOR(q, t){
		scanf("%d\n", &n);
		FOR(j, n){
			int last = 0;
			FOR(k, n){
				char c;
				scanf("%c", &c);
				if(c=='1') last = k;
			}
			scanf("\n");
			a[j] = last;
		}
		printf("Case #%d: ", q+1);
		solvecase();
	}
}

int main(){
	init();
	solve();
	return 0;
}