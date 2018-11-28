#include<iostream>
using namespace std;
int arr[1010];
bool flag[1010];
int main(){
	int cases,i,j,k,ans,n;
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	scanf("%d",&cases);
	for(i=1; i<=cases; i++){
		ans = 0;
		scanf("%d",&n);
		for(j=1;j<=n;j++){
			scanf("%d",&arr[j]);
			flag[j]=0;
		}
		for(j=1;j<=n; j++){
			if(flag[j] == 0){
				int f = j;
				flag[j] = 1;
				int t = arr[j];
				int num = 1;
				while(t != f) {
					
					flag[t] = 1;
					t = arr[t];
					num++;
				}
				if (num != 1){
					ans += num;
				}
			}
		}
		printf("Case #%d: ",i);
		printf("%d.000000\n",ans);
	}
	return 0;
}