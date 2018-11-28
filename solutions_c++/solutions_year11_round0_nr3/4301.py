#include<stdio.h>
#include<string.h>
int a[100];
int b[100];
int mm,n;
int step;
void dfs(int sum1,int sum2,int k1,int k2,int max,int t){
	int i,j;
	step++;
	if(sum1>max)return;
	if(t>n+1)return;
	if(t==n+1){
		if(sum2>mm&&k1==k2&&k1>0){
			mm=sum2;
		}
		return;
	}
	dfs(sum1+a[t],sum2,k1^a[t],k2,max,t+1);
	dfs(sum1,sum2+a[t],k1,k2^a[t],max,t+1);
	return;
}
		
int main(){
	int cas,i,j,sum;
	int count=1;
	freopen("C:\\Documents and Settings\\海鹏\\桌面\\C-small-attempt0.in","r",stdin);
	freopen("C:\\Documents and Settings\\海鹏\\桌面\\stdout.txt","w",stdout);
	scanf("%d",&cas);
	while(cas--){
		step=0;
		mm=0,sum=0;
		scanf("%d",&n);
		memset(b,0,sizeof(b));
		for(i=1;i<=n;i++){
			scanf("%d",&a[i]);
			sum+=a[i];
		}
		dfs(0,0,0,0,sum/2,1);
		printf("Case #%d: ",count++);
		if(mm==0)
		printf("NO\n");
		else
		printf("%d\n",mm);
	}
	return 0;
}
		
