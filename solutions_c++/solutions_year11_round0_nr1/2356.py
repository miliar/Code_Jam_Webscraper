/*
 * Bot_Trust.cpp
 *
 *  Created on: 07/05/2011
 *      Author: francisco
 */

#include <stdio.h>

inline int dist(int& x, int& y) {
	if(x > y) return x - y;
	return y - x;
}

int main(void) {
	int t,nc,n,i,ans,sto,stb,mvo,mvb,aux;
	int button[100];
	char color[100];

	scanf("%d",&t);
	for(nc = 1; nc <= t; nc++) {
		sto = stb = 1;
		ans = mvo = mvb = aux = 0;
		scanf("%d ",&n);
		for(i = 0; i < n; i++) scanf("%c %d ",&color[i], &button[i]);
		for(i = 0; i < n; i++) {
			if(color[i] == 'O') {
				aux = dist(button[i],sto) + 1 - mvb;
				sto = button[i];
				mvo += (aux > 0)?aux:1;
				ans += (aux > 0)?aux:1;
				mvb = 0;
			} else { // color = BLUE
				aux = dist(button[i],stb) + 1 - mvo;
				stb = button[i];
				mvb += (aux > 0)?aux:1;
				ans += (aux > 0)?aux:1;
				mvo = 0;
			}
		}
		printf("Case #%d: %d\n",nc,ans);
	}
	return 0;
}
