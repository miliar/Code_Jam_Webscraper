#include<iostream>
int ad[10][10],aa[300],bb[300],z[10],u[10],m,gt,tt,n;
void dfs(int p){
	if(p<=m){
		for(int i=1;i<=n;i++){
			if(!u[i]){
				u[i]=1;
				z[p]=i;
				dfs(p+1);
				u[i]=0;
			}
		}
	}else{
		for(int i=1;i<m;i++){
			if(ad[z[aa[i]]][z[bb[i]]]!=tt){
				return;
			}
		}
		gt=1;
	}
}
main(){
	int t,i,j,a,b;
	scanf("%d",&t);
	for(tt=1;tt<=t;tt++){
		scanf("%d",&n);
		gt=0;
		for(i=1;i<n;i++){
			scanf("%d",&a);
			scanf("%d",&b);
			ad[a][b]=tt;
			ad[b][a]=tt;
		}
		scanf("%d",&m);
		for(i=1;i<m;i++){
			scanf("%d",&aa[i]);
			scanf("%d",&bb[i]);
		}
		dfs(1);
		printf("Case #%d: ",tt);
		if(gt){printf("YES\n");}else{printf("NO\n");}
	}
	return 0;
}
