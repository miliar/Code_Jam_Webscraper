#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int main(){
	int n, t, x;
	char s[10];
	int preo, preb, pre;
	int curb, curo;

	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	
	scanf("%d", &t);
	for (int k = 1; k <= t; k++){
		scanf("%d", &n);
		preo = 0; preb = 0; pre = 0;
		curo = 1; curb = 1;
		for (int i = 0; i < n; i++){
			scanf("%s%d", s, &x);
			if (s[0] == 'O') {
				pre = max(pre, preo + abs(x - curo)) + 1;
				preo = pre;
				curo = x;
			}else {
				pre = max(pre, preb + abs(x - curb)) + 1;
				preb = pre;
				curb = x;
			}
		}
		printf("Case #%d: %d\n", k, pre);
	}

	return 0;
}