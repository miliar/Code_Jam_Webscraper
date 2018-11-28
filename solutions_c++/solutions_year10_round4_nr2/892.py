#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
#include<queue>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<sstream>
#include<cctype>

using namespace std;

#define pb push_back
#define pf printf
#define sf scanf
#define re return

#define DBG 0

int P;
int M[15000];
int res;
void dfs(int p, int l, int r) {
	if( l >= r || p == 0) return;
	//cout << l << " " << r << endl;
	int i;
	for(i=l;i<=r;i++) {
		if( M[i] < p ) break;
	}
	int cnt = 0;

	if( i <= r ) {
		//for(i=l;i<=r;i++)
		//  M[i]++;

		dfs(p-1, l, l + (r-l)/2);
		dfs(p-1,  l + (r-l)/2 + 1, r);
		res++;
	}
	else {
		dfs(p-1, l, l + (r-l)/2);
		dfs(p-1,  l + (r-l)/2 + 1, r);
	}
}

int main() {
	int t, cases = 1;
	int i;
	for( sf("%d", &t); t--; ) {
		cin >> P;
		for(i=0;i<(1<<P);i++) {
		 cin >> M[i];
		 //M[i] = P - M[i];
	 	}

		// fao input nao
		int k = 1;
		int a;
		for(i=0;i<P;i++) {
			int j = k;
			while(j--) cin >> a;
			k *= 2;
		}
		res = 0;
		dfs(P, 0, (1<<P) - 1);
		pf("Case #%d: %d\n", cases++, res);
	}
	return 0;
}
