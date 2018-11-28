#include<cstdio>
#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
#include<sstream>
#include<queue>
#include<string>
#include<cmath>

using namespace std;

#define pb push_back
#define re return
#define sf scanf
#define pf printf

int OK[100];
int N, K, B, T;
int D[100];
int V[100];

int main() {
	int t, i, j;
	int cases = 1;
	for( sf("%d", &t); t--;) {
		cin >> N >> K >> B >> T;
		for(i=0;i<N;i++) {
			cin >> D[i];
		}
		for(i=0;i<N;i++)
		 cin >> V[i];

		for(i=0;i<N;i++) {
			int d = B - D[i];
			int x = V[i] * T;
			if( x >= d ) OK[i] = 1;
			else OK[i] = 0;
		}

		int res = 0;
		int cnt = 0;
		for(i=N-1; cnt<K && i>=0;i--) {
			if( OK[i] ) {
				for(j=i+1;j<N;j++)
				 if( OK[j] == 0 ) res++;
				cnt++;
			}
		}
		if( cnt < K ) {
			pf("Case #%d: %s\n", cases++, "IMPOSSIBLE");
		}
		else
			pf("Case #%d: %d\n", cases++, res);
	}
	return 0;
}
