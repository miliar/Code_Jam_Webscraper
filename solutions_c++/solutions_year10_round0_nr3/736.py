#include <cstdio>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <utility>
#include <algorithm>

int main() {
	int i,j,k,c,T,R,K,N,group,it;
	unsigned long long int money,g[2050],aux;
	scanf("%d ",&T);
	for(c=1;c<=T;c++) {
		scanf("%d %d %d ",&R,&K,&N);
		g[0]=0;
		for(i=1;i<=N;i++) {
			scanf("%lld ",&(g[i]));
			g[i+N] = g[i];
		}
		for(i=1;i<=2*N;i++)
			g[i] += g[i-1];
		money = 0;
		group = 1;
		if(g[N] <= K) {
			printf("Case #%d: %lld\n",c,R * g[N]);
			continue;
		}
		for(i=1;i<=R;i++) {
			aux = K + g[group-1];
			it=group;
			while(g[it]<=aux)
				it++;
			it--;
			money += g[it] - g[group-1];
			group = it+1;
			if(group > N)
				group -= N;
		}
		printf("Case #%d: %lld\n",c,money);
	} 
	return 0;
}
		
		
		
		
		
		
