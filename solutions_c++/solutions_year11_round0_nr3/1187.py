#include<iostream>
#include<algorithm>
using namespace std;
int value[1010];
int flag[1010];
int bn[1010][20];
bool cmp(int a, int b){
	return a<b;
}
int main(){
	int cases,i,j,k,p,n;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&cases);
	for(i=1; i<=cases; i++){
		scanf("%d",&n);
		memset(flag,0,sizeof(flag));
		memset(bn,0,sizeof(bn));
		scanf("%d",&value[0]);
		int ans = value[0];
		int sum = ans;
		for(j=1; j<n; j++){
			scanf("%d",&value[j]);
			ans = (ans ^ value[j]);
			sum += value[j];
		}
		printf("Case #%d: ",i);
		if (ans != 0) {
			printf("NO\n");
			continue;
		}
		sort(value,value+n,cmp);
		ans = sum - value[0];
		printf("%d\n",ans);
	}
	return 0;
}