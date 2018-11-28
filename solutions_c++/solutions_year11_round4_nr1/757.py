#include<stdio.h>
#include<algorithm>
struct GO {
	int B,E,W;
	double dW,dRW;
}go[1001];
struct ND {
	int DIS;
	double xd;
	int W;
	bool operator<(ND x)const {
		return W<x.W;
	}
}dd[1001];
	
main(){
	int i,j,k;
	int TT,TN;
	int X,S,R,T,N;
	int DIF;
	int dALL;
	double rcost;
	double dt,TA;
	scanf("%d",&TT);
	for(TN=1;TN<=TT;TN++){
		printf("Case #%d: ",TN);
		
		scanf("%d%d%d%d%d",&X,&S,&R,&T,&N);
		
		DIF=R-S; //R>S
		dt=T;
		
		dALL=0;
		for(i=0;i<N;i++){
			scanf("%d%d%d",&go[i].B,&go[i].E,&go[i].W);
			dALL+=go[i].E-go[i].B;
			dd[i+1].DIS=go[i].E-go[i].B;
			dd[i+1].W=(double)S+go[i].W;
		}
		dd[0].DIS=X-dALL;
		dd[0].W=S;
		
		
		std::sort(dd,dd+N+1);
		
		
		for(i=0;i<=N;i++){
			dd[i].xd=dd[i].DIS;
			rcost=(double)dd[i].DIS/((double)dd[i].W+(double)DIF);
			if(rcost<=dt){
				dt-=rcost;
				dd[i].xd*=(double)dd[i].W/((double)dd[i].W+(double)DIF);
			} else {
				dd[i].xd=dt*((double)dd[i].W) + ((double)dd[i].xd-(double)dt*((double)dd[i].W+(double)DIF));
				dt=0;
			}
		}
		TA=0;
		for(i=0;i<=N;i++){
			TA+=(double)dd[i].xd/(double)dd[i].W;
		}
		printf("%.8lf\n",TA);
			
		
		
	}
}
