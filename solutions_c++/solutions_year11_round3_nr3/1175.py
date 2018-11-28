#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  

using namespace std;  

int N[100];
int n, h, l, t;

void solve(int t) {
	for(int i = l; i <= h; i++) {
		int flag = 1;
		for(int j = 0; j < n; j++) {
			if(max(i, N[j]) % min(i, N[j]) != 0) {
				flag = 0;
				break;
			}
		}

		if(flag) {
			printf("Case #%d: %d\n", t+1, i);
			return;
		}
	}
	
	printf("Case #%d: NO\n", t+1);
}

int main() {
	scanf("%d\n", &t);
	for(int i = 0; i < t; i++) {
		scanf("%d %d %d", &n, &l, &h);
		for(int j = 0; j < n; j++) {
			scanf("%d", &(N[j]));
		}
		solve(i);
	}
	return 0;
}