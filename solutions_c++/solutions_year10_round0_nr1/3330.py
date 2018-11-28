/*******************************************************
*		Problem Name:			Snapper
*		Problem ID:				
*		Occassion:				_ Contest _ _ _
*
*		Algorithm:				
*		Special Case:			
*		Judge Status:			
*		Author:					Saint Atique
*		Notes:					
*								
*******************************************************/
//#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
//#include <new>
#include <vector>
#include <queue>
//#include <map>
#include <algorithm>
//#include <iomanip>//for cout formatting
#define	INF 2147483648
#define EPS 1e-8
using namespace std;

int main() {
	//freopen("p1_in.txt", "r", stdin);
	//freopen("p1_out.txt", "w", stdout);

	int i,t, N, K, mod;

	scanf("%d", &t);

	for (i=0; i<t; i++) {
		scanf("%d%d", &N, &K);

		mod = (K+1) % (int)pow(2.0, (double)N);

		if (mod)
			printf("Case #%d: OFF\n", i+1);
		else
			printf("Case #%d: ON\n", i+1);
	}
	
	return 0;
}
