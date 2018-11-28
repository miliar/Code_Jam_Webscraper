//be name oo
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iostream>

using namespace std;

int main(){
	int t;
	scanf("%d", &t);
	for(int test = 1; test <= t; test++){
		int a, b, ans = 0;
		scanf("%d %d", &a, &b);
		for(int n = a; n <= b; n++)
			for(int m = n + 1; m <= b; m++){
				int tmpn = n;
				int dig = 0, mult = 1;
				while(tmpn){
					dig++;
					tmpn /= 10;
					mult *= 10;
				}
				if(m >= mult || m < mult / 10)
					continue;
				int tmpm = m;
				while(dig--){
					int last = tmpm % 10;
					tmpm += mult * last;
					tmpm -= last;
					tmpm /= 10;
					if(tmpm == n){
						ans++;
						break;
					}
				}
			}
		printf("Case #%d: %d\n", test, ans);
	}
	return 0;
}

