/*
 * Candy Splitting.cpp
 *
 *  Created on: 07/05/2011
 *      Author: francisco
 */

#include <stdio.h>

int main(void) {
	unsigned int t,nc,n,i,ans,min,aux,total;

	scanf("%d",&t);
	for(nc = 1; nc <= t; nc++) {
		ans = 0;
		min = 9999999;
		total = 0;
		scanf("%d",&n);
		for(i = 0; i < n; i++) {
			scanf("%d ",&aux);
			if(aux < min) min = aux;
			total += aux;
			ans = ans^aux;
		}
		total -= min;
		printf("Case #%d: ",nc);
		if(!ans) printf("%d\n",total);
		else printf("NO\n");
	}
	return 0;
}
