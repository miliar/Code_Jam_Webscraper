#include<cstdio>
#include<algorithm>
using namespace std;

int a[1000005];
int N,x=0,sum=0,T;

int main(){
	scanf("%d",&T);
	for (int t=1;t<=T;++t){
		scanf("%d",&N);
		x = 0;
		sum = 0;
		for (int i=0;i<N;++i){
			scanf("%d",&a[i]);
			x ^= a[i];
			sum += a[i];
		}
		printf("Case #%d: ",t);
		if (x){
			printf("NO\n");
		}else{
			sort(a,a+N);
			printf("%d\n",sum-a[0]);
		}
	}
	return 0;
}
