#include<stdio.h>
#include<ctype.h>
#include<string.h>
#include<algorithm>
using namespace std;

int tests;
int n, s, p, score, ret;

int main() {
	scanf("%d\n",&tests);
	for(int t = 1; t <= tests; t++) {
		ret = 0;
		scanf("%d %d %d",&n,&s,&p);
		for(int i = 0; i < n; i++) {
			scanf("%d",&score);
			if (score == 0) {
				if (p == 0) ret++;
				continue;
			}			
			if (score >= p*3-2) {
				ret++;
			} else if (score >= p*3 - 4 && s > 0) {
				s--;
				ret++;
			}
		}
		printf("Case #%d: %d\n",t,ret);
	}		
	return 0;
}