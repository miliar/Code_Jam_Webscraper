/*******************************************************
*		Problem Name:			Coast Rider
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
	//freopen("Qc_in.txt", "r", stdin);
	//freopen("p1_out.txt", "w", stdout);

	int R, k, N, a, t, profit,		// profit is total profit of coast rider
		tp,							// total people on a single ride
		tap;						// Total available people for a single ride
	int i,j;

	scanf("%d", &t);

	for (i=0; i<t; i++) {
		queue<int> Q;
		profit = 0;
		scanf("%d%d%d", &R, &k, &N);
		for (tap=0,j=0; j<N; j++) {
			scanf("%d", &a);
			Q.push(a);
			tap += a;
		}
		for (j=0; j<R; j++) {
			tp = 0;
			while (true) {
				if (Q.empty())
					break;
				a = Q.front();
				if (a + tp <= k && a + tp <= tap) {
					tp += a;
					Q.pop();
					Q.push(a);
				}
				else
					break;
			}
			profit+= tp;
		}
		printf("Case #%d: %d\n", i+1, profit);
	}


	return 0;
}
