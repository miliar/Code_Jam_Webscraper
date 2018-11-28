#include <stdio.h>
#define MAX	1024

int a[MAX],b[MAX];

int intersect(int i, int j){
	if(a[i] > a[j] && b[i] < b[j]) return 1;
	if(a[i] < a[j] && b[i] > b[j]) return 1;
	return 0;
}
void solve(){
	int i,j;
	int n, count=0;
	scanf("%d", &n);
	for(i=0;i<n;i++)
		scanf("%d %d", &a[i], &b[i]);
	for(i=0;i<n;i++){
		for(j=i+1;j<n;j++)
			if(intersect(i,j))
				count++;
	}
	printf("%d\n", count);
}
int main(){
	int i,T;
	scanf("%d", &T);
	for(i=1;i<=T;i++){
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
