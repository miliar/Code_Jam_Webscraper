#include <stdio.h>

int num[10001];
void solve(){
	int n,l,h,i,j;
	int g;
	bool valid=true;
	scanf("%d %d %d", &n, &l, &h);
	for(i=0;i<n;i++)
		scanf("%d", &num[i]);
	for(i=l;i<=h;i++){
		for(j=0;j<n;j++){
			if(i%num[j]!=0 && num[j]%i!=0)
				break;
		}
		if(j==n){
			printf("%d\n", i);
			return;
		}
	}
	printf("NO\n");
	return;
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
