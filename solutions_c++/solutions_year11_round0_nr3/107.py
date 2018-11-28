#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;

char s[200];

int main(){
	int i, j, k, m, n, cas, p;
	freopen("C-large (1).in", "r", stdin);
	freopen("w.txt", "w", stdout);
	scanf("%d", &cas);
	for(int ri = 1; ri <= cas; ri++){
		printf("Case #%d: ", ri);
		scanf("%d", &n);
		int sum = 0, mn = 1e6 + 1, p = 0;
		for(i = 0; i < n; i++){
			scanf("%d", &k);
			sum += k;
			mn = min(k, mn);
			p ^= k;
		}
		if(p){
			puts("NO");
		}else{
			printf("%d\n", sum - mn);
		}
	}
}
