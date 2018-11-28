#include<cstdio>
#include<algorithm>

using namespace std;

int main(){
	int ans,n[1001],n1[1001],N,T;

	scanf("%d",&T);
	for(int i=0; i<T; i++){
		ans = 0;
		scanf("%d",&N);
		for(int j=0; j<N; j++)	scanf("%d",n+j);
		for(int j=0; j<N; j++)	n1[j] = n[j];
		sort(n1,n1+N);
		for(int j=0; j<N; j++)	if( n1[j]!=n[j] ) ans++;
		printf("Case #%d: %.06lf\n",i+1,double(ans));
	}
	return 0;
}
