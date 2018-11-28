//#include <stdafx.h>

#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
using namespace std;


int main() {
	/*freopen("D:\\a.in", "r", stdin);
	freopen("D:\\a.out", "w", stdout);*/
	int T;
	scanf("%d", &T);
	for (int I = 0; I < T; I++) {
		int n, s, p;
		scanf("%d%d%d", &n, &s, &p);
		int ans = 0;
		for (int i = 0; i < n; i++) {
			int x;
			scanf("%d",&x);
			if ((x + 2) / 3 >= p) ans++;
			else if (s) {
				if (((x % 3 == 0) && (x > 0) && (x / 3 + 1 >= p)) ||
					((x % 3 == 2) && (x / 3 + 2 >= p))) {
					ans++; s--; 
				}
			}; 
		}
		printf("Case #%d: %d\n", I + 1, ans);
	}
}