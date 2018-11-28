#include <stdio.h>

const int size=10000;
int a[size+1][2],c[size+1],g[size+1];

void gate(int i,int g,int f){
	int j,k;
	for(j=0; j<2; j++){
		if(a[i*2][j]<0) continue;
		for(k=0; k<2; k++){
			if(a[i*2+1][k]<0) continue;
			int t=a[i*2][j]+a[i*2+1][k]+f;
			int x=(g==1)?(j&k):(j|k);
			if(a[i][x]<0||a[i][x]>t)
				a[i][x]=t;
		}
	}
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("a.txt","w",stdout);
	int n,t;
	scanf("%d",&n);
	for(t=1; t<=n; t++){
		int m,v,i,x;
		scanf("%d%d",&m,&v);
		for(i=1; i<=(m-1)/2; i++)
			scanf("%d%d",&g[i],&c[i]);
		for(; i<=m; i++){
			scanf("%d",&x);
			a[i][x]=0;
			a[i][1-x]=-1;
		}
		for(i=(m-1)/2; i>0; i--){
			a[i][0]=a[i][1]=-1;
			gate(i,g[i],0);
			if(c[i])
				gate(i,1-g[i],1);
		}
		printf("Case #%d: ",t);
		if(a[1][v]<0)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",a[1][v]);
//		for(i=1; i<=(m-1)/2; i++)
//			printf("%d %d %d\n",i,a[i][0],a[i][1]);
	}
	scanf("%*d");
	return 0;
}
