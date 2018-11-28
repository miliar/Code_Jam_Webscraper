#include<iostream>
#include<cstring>
char s[50545],t[50545];
int k,u[564],e[564],l,p,ans;
void dfs(int lev){
	if(lev<k){
		for(int i=0;i<k;i++){
			if(!u[i]){
				u[i]=1;
				e[lev]=i;
				dfs(lev+1);
				u[i]=0;
			}
		}
	}else{
		int cons=1;
		for(int i=0;i<p;i++){
			for(int j=0;j<k;j++){
				t[i*k+e[j]]=s[i*k+j];
			}
		}
		t[l]='\0';
		//printf("%s\n",t);
		for(int i=1;i<l;i++){
			if(t[i]!=t[i-1]){
				cons++;
			}
		}
		ans<?=cons;
	}
}
main(){
	int tt,t;
	scanf("%d",&t);
	for(tt=1;tt<=t;tt++){
		scanf("%d",&k);
		scanf("%s",s);
		l = strlen(s);
		p = l/k;
		ans = l;
		dfs(0);
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}
