#include <stdio.h>
#include <string.h>

int main(){
	freopen("D-small-attempt0.in","r",stdin);
	freopen("d.txt","w",stdout);
	const int size=128;
	const int m=10007;
	int N,T,W,H,R,d[size][size],i,j;
	scanf("%d",&N);
	for(T=1; T<=N; T++){
		memset(d,0,sizeof(d));
		scanf("%d%d%d",&H,&W,&R);
		while(R--){
			scanf("%d%d",&i,&j);
			d[i][j]=-1;
		}
		d[1][1]=1;
		for(i=1; i<=H; i++){
			for(j=1; j<=W; j++){
				if(d[i][j]<0) continue;
				if(i>1&&d[i-2][j-1]>0)
					d[i][j]+=d[i-2][j-1];
				if(j>1&&d[i-1][j-2]>0)
					d[i][j]+=d[i-1][j-2];
				d[i][j]%=m;
			}
		}
		printf("Case #%d: %d\n",T,d[H][W]);
	}
	return 0;
}
