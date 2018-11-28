#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int n, k;
int a[205][205];
int source=0, sink=1;
int w[205][205], Z;
int used[205];

int flow(int x){
	if(x==sink){
		return 1;
	}
	used[x]=1;
	for(int i=1;i<Z;i++)
		if(!used[i] && a[x][i] && flow(i)){
			a[x][i] = 0;
			a[i][x] = 1;
			return 1;
		}
	return 0;
}

int main(void)
{
	int T,i,j,u, cs=0;
	scanf("%d",&T);
	while(T--){
		memset(a,0,sizeof(a));
		scanf("%d%d",&n,&k);
		for(i=1;i<=n;i++){
			for(j=0;j<k;j++){
				scanf("%d",&w[i][j]);
			}
		}
		for(i=1;i<=n;i++){
			for(j=1;j<=n;j++){
				if(w[i][0]>w[j][0]){
					for(u=1;u<k;u++)
						if(w[i][u]<=w[j][u])
							break;
					if(u==k)
						a[i*2][j*2+1] = 1;
				}
			}
		}
		Z = 2*n+2;
		for(i=1;i<=n;i++){
			a[source][i*2] = 1;
			a[i*2+1][sink] = 1;
		}
		int ans=n;
		while(1){
			memset(used,0,sizeof(used));
			j = flow(source);
			if(j) --ans;
			else
				break;
		}
		printf("Case #%d: %d\n",++cs, ans);
	}
	return 0;
}
