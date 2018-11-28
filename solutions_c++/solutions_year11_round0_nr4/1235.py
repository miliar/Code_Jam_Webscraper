#include<stdio.h>
#include<cstdlib>
#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<cstring>

using namespace std;

#define REP(I,N) for(int I=0 ; I<N ; I++)
#define SZ(A) ((int)(A).size())
#define PB push_back
#define F first
#define S second

bool used[1010];
int A[1010];
int dfs(int node) {
	used[node] = true;
	int len = 1;
	if(!used[A[node]]) len += dfs(A[node]);
	return len;
}

int main() {

	int T;
	cin >> T;
	for(int t=0 ; t<T ; t++) {
		memset(used, false, sizeof(used));
		int n;
		cin >> n;		
		REP(i,n) {
			cin >> A[i];
			A[i]--;
		}

		int res = 0;
		for(int i=0 ; i<n ; i++) if(!used[i]) {
			int l = dfs(i);
			if(l > 1) res += l;
		}
		printf("Case #%d: %.6lf\n", t+1, (double)res);

	}	
	return 0;
}
