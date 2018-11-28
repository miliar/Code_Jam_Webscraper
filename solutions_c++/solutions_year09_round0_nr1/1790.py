#include<stdio.h>
struct node{
	char strr[20];
}str1[5010];
int sum,L;
char str[10010],str2[20];
void dfs(int i,int j,int k){
	int x,y;
	if(i==L){
		if(str[j]=='\0')++sum;
		return ;
	}
	if(str[j]=='('){
		for(y=j+1;;++y)
			if(str[y]==')'||str[y]=='\0')break;
		j+=1;
	}
	else y=j+1;
	for(x=j;x<y;++x){
		if(str1[k].strr[i]==str[x]){
			if(str[y]==')')dfs(i+1,y+1,k);
			else dfs(i+1,y,k);
		}
	}
}
int main(){
	int N,i,j,x,D,t;
	freopen("0.in","r",stdin);
	freopen("0.out","w",stdout);
	while(scanf("%d%d%d",&L,&D,&N)!=EOF){
		for(i=0;i<D;++i)
			scanf("%s",str1[i].strr);
		for(t=1;t<=N;++t){
			scanf("%s",str);
			sum=0;
			if(str[0]=='('){
				for(x=1;;++x)
					if(str[x]==')'||str[x]=='\0')break;
			}
			else x=1;
			for(i=0;i<x;++i){
				for(j=0;j<D;++j){
					if(str1[j].strr[0]==str[i]){
						if(str[x]==')')dfs(1,x+1,j);
						else dfs(1,x,j);
					}
				}
			}
			printf("Case #%d: %d\n",t,sum);
		}
	}
	return 0;
}
