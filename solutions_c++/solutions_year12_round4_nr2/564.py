#include<stdio.h>
#include<stdlib.h>
int N,W,L;
int r[1021];
int x[1021],y[1021];
int max(int a,int b){
	if(a > b)return a;
	return b;
}
int min(int a,int b){
	if(a < b)return a;
	return b;
}
int abs(int a){
	if(a > 0)return a;
	return -a;
}
int main(){
	int T;
	scanf("%d",&T);
	for(int ca = 1;ca<=T;ca++){
		scanf("%d %d %d",&N,&W,&L);
		for(int i=0;i<N;i++)
			scanf("%d",&r[i]);
		x[0] = 0;
		y[0] = 0;
		int NowW = r[0];
		int NowL = r[0];
		int Lline = 0;
		for(int i=1;i<N;i++){
			if(NowL + r[i] > L){
				Lline = Lline + NowW;
				//xposition = xposition + NowW;
				x[i] = Lline + r[i];
				y[i] = 0;
				NowW = 2 * r[i];
				NowL = r[i];
			}else{
				if(Lline == 0)
					x[i] = 0;
				else
					x[i] = Lline + r[i];
				y[i] = NowL + r[i];
				if(Lline == 0)
					NowW = max(NowW,r[i]);
				else
					NowW = max(NowW,2 * r[i]);
				NowL = NowL + 2 * r[i];
			}
			if(x[i] > W || y[i] > L)fprintf(stderr,"error\n");
		}
		for(int i=0;i<N;i++){
			if(x[i] > W || y[i] > L){
				fprintf(stderr,"%d:i = %d [%d,%d] > [%d,%d]\n",ca,i,x[i],y[i],W,L);
			}
			for(int j=0;j<N;j++){
				if(i == j)continue;
				long long int dx = abs(x[i] - x[j]);
				long long int dy = abs(y[i] - y[j]);
				long long int tr = r[i] + r[j];
				if(dx * dx + dy * dy < tr * tr ){
					fprintf(stderr,"%d:(i,j) = (%d,%d)[%d,%d][%d,%d] %d+%d\n",ca,i,j,x[i],y[i],x[j],y[j],r[i],r[j]);
				}
			}
		}
		printf("Case #%d:",ca);
		for(int i=0;i<N;i++){
			printf(" %d %d",x[i],y[i]);
		}
		printf("\n");
	}
	return 0;
}
