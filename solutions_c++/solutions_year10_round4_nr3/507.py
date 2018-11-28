#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
bool bac[1010][1010];
bool run(){
	bool f=0;
	int i,j;
	for(i=100;i>=1;i--){
		for(j=100;j>=1;j--){
			if(bac[i-1][j]&&bac[i][j-1])bac[i][j]=1;
			if(bac[i][j]&&!bac[i][j-1]&&!bac[i-1][j])bac[i][j]=0;
			if(bac[i][j])f=1;
		//	if(i<=7&&j<=7)printf("%d ",bac[i][j]);
		}
		//if(i<=7)puts("");
	}
//	puts("");
	return f;
}
int main(){
	int t,cas=1,i,j;
	scanf("%d",&t);
	while(t--){
		int r,a,b,c,d;
		scanf("%d",&r);
		memset(bac,0,sizeof(bac));
		while(r--){
			scanf("%d%d%d%d",&a,&b,&c,&d);
			for(i=a;i<=c;i++)for(j=b;j<=d;j++)bac[i][j]=1;
		}
		int ans=0;
		while(run())ans++;
		printf("Case #%d: %d\n",cas++,ans+1);
	}
}


