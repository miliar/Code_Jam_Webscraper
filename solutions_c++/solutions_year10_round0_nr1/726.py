// AlgorithmProject.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	int t, n, k;

	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &t);
	for(int i = 0;i < t;i++){
		scanf("%d%d", &n, &k);
		printf("Case #%d: ", i + 1);
		if(((k + 1) % (1 << n)) == 0){
			puts("ON");
		}else{
			puts("OFF");
		}
	}
	return 0;
}

