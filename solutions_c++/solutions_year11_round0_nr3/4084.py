#include<cstdio>
int max(int a, int b) { return a > b ? a: b;}
#define siz 16
int arr[siz];
int N;
int tot;
int f(){
	int i, j, res,ret;
	int a, b, sum;
	res = -1;
	for( i =1 ; i < (1<<N) - 1; i++){
		a = 0; b = 0; sum = 0;
		for( j = 0; j < N; j++){
			if(i&(1<<j)){
				a^=arr[j];
				sum+=arr[j];
			}
			else b^=arr[j];
		}
		ret = max(sum, tot - sum);
		if(a==b) res = max(res, ret);
	}
	return res;
}
int main(){
	//freopen("C.in","r",stdin);
	//freopen("out.txt","w",stdout);
	int kase, ct = 1; 
	int i;
	scanf("%d",&kase);
	while(kase--) {
		scanf("%d",&N);
		tot = 0;
		for( i = 0; i<N; i++){
		scanf("%d",&arr[i]);
		tot+=arr[i] ;
		}
		int res = f();
		if(res>-1){
			printf("Case #%d: %d\n",ct++,res);
		}
		else printf("Case #%d: NO\n",ct++);
	}
	return 0;
}