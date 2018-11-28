#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i=0,_n=n; i<_n; i++)

int T,N,C[1001];

int main(){
	scanf("%d",&T);
	REP(tc,T){
		scanf("%d",&N);
		REP(i,N) scanf("%d",&C[i]);

		// after observing the results of the small input,
		// it seemed that the result always of the form:
		// pick the lowest value candy, and xor the rest of the candies.
		// if they match, output the sum of the rest of the candies.

		sort(C,C+N);

		int res = -1, x = 0, s = 0;
		for (int i=1; i<N; i++) x ^= C[i], s += C[i];
		if (x == C[0] && res < s) res = s;

		printf("Case #%d: ",tc+1);
		if (res == -1) puts("NO");
		else printf("%d\n",res);
		fflush(stdout);
	}
}
