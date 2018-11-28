#include <stdio.h>
#include <string.h>

#define MAX 1000

int main(void){
	freopen("B-large.in", "r", stdin);
	freopen("result.txt", "w", stdout);
	int T, k = 0;
	scanf("%d", &T);
	while(k++ < T){
		int N, S, p, score;
		int count = 0;
		scanf("%d%d%d", &N, &S, &p);
		int res = 0;
		for(int i = 0; i < N; ++i){
			scanf("%d", &score);
			if(score >= 3 * p - 2)
				++res;
			else if(score >= 3 * p -4 && score >= p)
				++count;
		}
		res += ((count > S) ? S : count);
		printf("Case #%d: %d\n", k, res);
	}
	return 0;
}
