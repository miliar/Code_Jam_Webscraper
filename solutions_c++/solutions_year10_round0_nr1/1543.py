#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <cmath>

int main(){
	int T, N, K, Case, tmp;
	scanf("%d", &T);
	for(Case = 1; Case <= T; ++Case)
	{
		scanf("%d%d", &N, &K);
		tmp = pow(2, N);
		if((K+1) % tmp != 0)
			printf("Case #%d: OFF\n", Case);
		else
			printf("Case #%d: ON\n", Case);
	}
	return 0;
}
