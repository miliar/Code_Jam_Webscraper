/*
	jamaj
*/

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>

using namespace std;

int T, N, K;
	
int main()
{	
//	freopen("A-large.in", "r", stdin);
//	freopen("A-large.out", "w", stdout);
	
	scanf("%d", &T);
	
	for (int t = 1; t <= T; t++) {
		scanf("%d %d", &N, &K);
		
		printf("Case #%d: ", t);
		
		if ((K + 1)%(1 << N) == 0) {
			printf("ON\n");
		} else {
			printf("OFF\n");
		}
	}
	
	return 0;
}
