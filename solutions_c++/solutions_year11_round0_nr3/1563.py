#include <stdio.h>
#include <stdlib.h>

int c[1024];
int low2high[1024], high2low[1024];
int compare(const void *a, const void *b){
	return (*(int *)a - *(int *)b);
}
void solve(){
	int i, j, n, sum=0;
	scanf("%d", &n);
	for(i=0;i<n;i++)
		scanf("%d", &c[i]);
	qsort(c, n, sizeof(int), compare);

//	for(i=0;i<n;i++)
//		printf("%d ", c[i]);
//	printf("\n");

	low2high[0] = c[0];
	high2low[n-1] = c[n-1];

	for(i=1;i<n;i++){
		low2high[i] = low2high[i-1]^c[i];
		high2low[n-1-i] = high2low[n-i]^c[n-1-i];
	}
	for(i=0;i<n-1;i++){
		if(low2high[i] == high2low[i+1])
			break;
	}
	if(i<n-1){
		for(j=i+1;j<n;j++)
			sum += c[j];
		printf("%d\n", sum);
	} else
		printf("NO\n");
}
int main(){
	int i, T;
	scanf("%d", &T);
	for(i=0;i<T;i++){
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}
