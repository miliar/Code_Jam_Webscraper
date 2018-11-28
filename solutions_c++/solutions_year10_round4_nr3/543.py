#include<stdio.h>
#include<memory.h>
/*
google code jam 2010
C Bacteria
*/
#define N 100
long bac[2][N][N];
void fill(long x1,long y1,long x2,long y2){
	long i,j;
	for(i=x1;i<=x2;i++)for(j=y1;j<=y2;j++)bac[0][i][j]=1;
}
long forward(long pnow,long pnext){
	long i,j,has=0;
	memset(bac[pnext],0,sizeof(bac[pnext]));
	for(i=0;i<N;i++)for(j=0;j<N;j++){
		long b1=(i==0||bac[pnow][i-1][j]==0),b2=(j==0||bac[pnow][i][j-1]==0);
		if(bac[pnow][i][j])has=1;
		if(b1&&b2)continue;
		if(b1+b2==0)bac[pnext][i][j]=1;
		else bac[pnext][i][j]=bac[pnow][i][j];
	}
	return has;
}
int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	long z,zi;
	scanf("%ld",&z);
	for(zi=1;zi<=z;zi++){
		long nr,i;
		scanf("%ld",&nr);
		memset(bac,0,sizeof(bac));
		for(i=0;i<nr;i++){
			long x1,y1,x2,y2;
			scanf("%ld%ld%ld%ld",&x1,&y1,&x2,&y2);
			fill(x1-1,y1-1,x2-1,y2-1);
		}
		long pnow=0,pnext=1,ans=0;
		for(;;ans++){
			if(!forward(pnow,pnext))break;
			pnow=pnext;pnext=1-pnext;
		}
		printf("Case #%ld: %ld\n",zi,ans);
	}
	return 0;
}
