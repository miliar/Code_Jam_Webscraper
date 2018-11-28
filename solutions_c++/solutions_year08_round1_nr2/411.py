#include <stdio.h>
#include <algorithm>
#include <math.h>
using namespace std;
#define N 2010

int n, m;
int favor[N][N], nf[N], mask[N], odd[N];

bool check(int odds, int evens)
{
	for(int i = 0; i < m; i++) {
		if((odd[i]==0||(odds & (1<<(odd[i]-1)))==0) && (evens & mask[i])==0)
			return false;
	}
	return true;
}

int main()
{
  	int t, index, i, j;
  	int malted, min_malted, sol;
	scanf("%d", &t);
	for(index = 1; index <= t; index++)
	{
		scanf("%d%d", &n, &m);
		for(i = 0; i < m; i++) {
			scanf("%d", &nf[i]);
			mask[i] = odd[i] = 0;
			for(j = 0; j < nf[i]; j++) {
				scanf("%d%d", &favor[i][j], &malted);
				if(malted) odd[i] = favor[i][j];
				else mask[i] |= 1<<(favor[i][j]-1);
			}
		}
		min_malted = n+1, sol = -1;;
		for(i = 0; i < (1<<n); i++) {
			for(j = (1<<n), malted=0; j > 0; j>>=1)
				if(i & j) malted++;
   			if(malted >= min_malted) continue;
   			if(check(i, i^((1<<n)-1))) {
   				min_malted = malted;
   				sol = i;
   			}
		}
		if(min_malted > n)
  			printf("Case #%d: IMPOSSIBLE\n", index);
		else {
  			printf("Case #%d:", index);
  			for(i = 1; i < (1 << n); i<<=1)
  				if(sol & i) printf(" 1");
  				else printf(" 0");
  			printf("\n");
 		}
	}
	return 0;
}

