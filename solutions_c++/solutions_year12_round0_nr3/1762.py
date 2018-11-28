#include<stdio.h>
int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.txt","w",stdout);
	int i,x,y,T,t,j,m,ans;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d%d",&x,&y);
		i=x;
		m=1;
		ans=0;
		while(i>=10){i/=10;m*=10;}
		for(i=x;i<=y;i++){
			j=i%m*10+i/m;
			while(j!=i){
				if(j>i&&j<=y&&j>=x)ans++;
				j=j%m*10+j/m;
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}
}
