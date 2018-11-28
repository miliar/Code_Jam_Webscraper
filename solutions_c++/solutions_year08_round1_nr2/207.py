#include <stdio.h>
#include <string.h>

const int size=2048;
int n,m,f[size][size],c[size],r[size];

int main(){
	freopen("B-large.in","r",stdin);
	freopen("b.txt","w",stdout);
	int C,t,i,j,u,v;
	scanf("%d",&C);
	for(t=1; t<=C; t++){
		memset(f,0,sizeof(f));
		memset(c,0,sizeof(c));
		memset(r,-1,sizeof(r));
		scanf("%d%d",&n,&m);
		for(i=0; i<m; i++){
			scanf("%d",&c[i]);
			for(j=0; j<c[i]; j++){
				scanf("%d%d",&u,&v);
				f[i][u-1]|=1<<v;
			}
		}
		u=1;
		while(u){
			for(i=0; i<m; i++)
				if(c[i]==1) break;
			if(i==m){
				for(i=0; i<n; i++)
					if(r[i]<0) r[i]=0;
				break;
			}
			for(j=0; j<n; j++)
				if(f[i][j]>0&&r[j]<0) break;
			r[j]=(f[i][j]==1)?0:1;
			for(i=0; i<m; i++){
				if(f[i][j]==0||c[i]==0) continue;
				if((f[i][j]&(1<<r[j]))>0)
					c[i]=0;
				else if(c[i]>1)
					c[i]--;
				else 
					u=0;
			}
		}
		printf("Case #%d:",t);
		if(!u)
			printf(" IMPOSSIBLE\n");
		else{
			for(i=0; i<n; i++)
				printf(" %d",r[i]);
			printf("\n");
		}
	}
	scanf("%*s");
	return 0;
}

