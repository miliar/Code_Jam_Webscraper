#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i=0,_n=n; i<_n; i++)

int C, N,K,B,T,X[100],V[100],slow[100];

int main(){
	scanf("%d",&C);
	REP(tt,C){
		printf("Case #%d: ",tt+1);

		scanf("%d %d %d %d",&N,&K,&B,&T);
		REP(i,N) scanf("%d",&X[i]);
		REP(i,N) scanf("%d",&V[i]);

		REP(i,N){
			int dx = B - X[i];
			slow[i] = (dx > T * V[i]);
		}

		int res = 0, rem = K;
		for (int i=N-1; i>=0; i--){
			if (slow[i]) continue;
			if (rem-- <= 0) break;

			int swap = 0;
			for (int j=i+1; j<N; j++)
				if (slow[j]) swap++;
			res += swap;
		}
		if (rem > 0) puts("IMPOSSIBLE");
		else printf("%d\n",res);
	}
}
