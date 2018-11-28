// aa.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>

using namespace std;
int n, k;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, a;
	scanf("%d", &t);
	a = 0;
	while (t--){
		a++;
		printf("Case #%d: ", a);
		scanf("%d%d", &n, &k);
		if ((((1<<n)-1)&k)==(1<<n)-1)
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}

