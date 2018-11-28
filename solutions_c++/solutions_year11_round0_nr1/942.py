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
		int pos[2] = {1, 1};
		int tm[2] = {0, 0};
		int n;
		scanf("%d", &n);
		for(int i = 0; i < n; i++){
			char c;
			int loc;
			scanf(" %c %d", &c, &loc);
			c = (c == 'O') ? 0 : 1;
			int curt = abs(pos[c] - loc) + 1 + tm[c];
			pos[c] = loc;
			curt = max(curt, tm[!c] + 1);
			tm[c] = curt;
		}
		printf("Case #%d: %d\n", test, max(tm[0], tm[1]));
	}
	return 0;
}

