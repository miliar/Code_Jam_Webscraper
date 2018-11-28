#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <memory.h>
using namespace std;
int dp[108][108];
int P, Q;
int num[108];
bool people[1000];
int main() {
	int i, j, k;
	int T, t = 1;
	int begin, end;
	int add;
	int a,b;
	scanf("%d", &T);
	while (T--) {
		scanf("%d%d", &P, &Q);
		for (i = 0; i < Q; i++) {
			scanf("%d", num + i);
		}
		int res =  1000000000, tmp;
		do {
			tmp = 0;
			memset(people, 1, sizeof(people));
			for (i = 0; i < Q; i++) {
				
				for (j = num[i] - 1; j >= 1; j--) {
					if (people[j] == 1) tmp++;
					else break;
				}
				for (j = num[i] + 1; j <= P; j++) {
					if (people[j] == 1) tmp++;
					else break;
				}
				people[num[i]] = 0; 
			}
			if (tmp < res) res = tmp;
		}while (next_permutation(num, num + Q));
		printf("Case #%d: %d\n", t++ ,res);
	}
}
