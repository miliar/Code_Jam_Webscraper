#include <stdio.h>
#include <string.h>
#include <math.h>
#include <assert.h>
#include <map>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i=0,_n=n; i<_n; i++)

int T,N,A[1001],S[1001];

int rec(int idx){
	if (S[idx]) return 0; else S[idx] = 1;
	return 1 + rec(A[idx]);
}

int main(){
	scanf("%d",&T);
	REP(tc,T){
		scanf("%d",&N);
		map<int,int> idx;
		REP(i,N){
			scanf("%d",&A[i]);
			S[i] = A[i];
		}
		sort(S, S+N);
		REP(i,N) idx[S[i]] = i;
		REP(i,N) A[i] = idx[A[i]];
		assert(idx.size() == N);

		int res = 0;
		REP(i,N){
			if (A[i] != i) res++; // WTF is going on here??
		}
		printf("Case #%d: %d.000000\n",tc+1,res);
		fflush(stdout);
	}
}
