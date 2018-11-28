/*
 * gcj.cpp
 *
 *  Created on: 2011-5-7
 *      Author: kokopelli
 */

#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <queue>
#include <map>
#include <set>
using namespace std;

int c[1005];

int main(){
	freopen("C-large.in", "r", stdin);
	freopen("resC.txt", "w", stdout);
	int t; cin >> t;
	for (int cas = 1; cas <= t; cas++){
		int n; cin >> n;
		int i, j;
		for (i = 1; i <= n; i++)
			scanf("%d", &c[i]);
		int sum1 = 0, sum2 = 0;
		for (i = 1; i <= n; i++){
			sum1 = (sum1 ^ c[i]);
			sum2 = (sum2 + c[i]);
		}
		int ans = -1;
		for (i = 1; i <= n; i++){
			if ((sum1 ^ c[i]) == c[i]){
				if (sum2 - c[i] > ans)
					ans = sum2 - c[i];
			}
		}
		printf("Case #%d: ", cas);
		if (ans == -1)
			printf("NO\n");
		else
			printf("%d\n", ans);
	}
	return 0;
}
