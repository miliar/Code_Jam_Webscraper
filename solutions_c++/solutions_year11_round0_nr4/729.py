#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define maxn 11000
int list[maxn];
int N,T,zu;
int main(){
	int i,j,tem,sum;
	double ans;
	/*freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);*/
	scanf("%d", &T);
	for (zu = 1; zu <= T; zu++){
		scanf("%d", &N);
		for (i = 1; i <= N; i++){
			scanf("%d", &list[i]);
		}
		sum = 0;
		for (i = 1; i <= N; i++)
			if (list[i] != i)
				sum++;
		ans = sum;
		printf("Case #%d: %.6lf\n",zu,ans);
	}
	return 0;
}