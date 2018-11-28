/*
 * =========================================================
 *       Filename:  A.cpp
 *    Description:  
 *        Created:  2011/5/21 9:18:28
 *         Author:  rocket323
 * =========================================================
 */
#include <stdio.h>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

bool check(int n, int pd, int pg) {
}

int main() {
	int t, n, pd, pg;
	scanf("%d", &t);
	for(int q=1; q<=t; ++q) {
		scanf("%d%d%d", &n, &pd, &pg);
		int f1 = 0;
		for(int i=1; i<=min(n, 100); ++i) {
			if(i * pd % 100 == 0) f1 = 1;
		}

		printf("Case #%d: ", q);
		if((pd != 0 && pg == 0) || (pd != 100 && pg == 100)) f1 = 0;
		puts(f1 ? "Possible" : "Broken");
		//puts(check(n, pd, pg) ? "Possible" : "Broken");
	}
	return 0;
}

