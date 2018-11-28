#include<iostream>
#include<cstdio>
#include<math.h>
#include<cstdlib>
using namespace std;

int gdc(int A, int B){
	if(abs(B)>abs(A)){
		int aux = A;
		A = B;
		B = aux;
	}
	while(B!=0){
		int T = B;
		B = A%B;
		A = T;
	}
	return A;
}

int main(void){
	int PG, PD, N;
	int tc;
	bool pode;
	scanf("%d",&tc);
	for(int i=0;i<tc;i++){
		pode = false;
		scanf("%d%d%d",&N,&PD,&PG);
		if(PG==0 && PD==0) pode = true;
		else if(PG==100 && PD==100) pode = true;
		else if( (PG!=100 && PD!=100) && (PD!=0 && PG!=0)){
			for(int j=1;j<=N && !pode;j++){
				double ganho_dia  = (double)(PD*j)/(double)100;
				if( (ganho_dia - (int)ganho_dia) ==0){
					if(PG==100){
						if(100*ganho_dia - PG*j>=0) pode = true;
					}else if (PG!=0){
						int K = gdc(PG,PG-100);
						int U = 100*ganho_dia - PG*j;
						if(!(U%K))	pode = true;
					}
				}
			}
		}
		if(pode) printf("Case #%d: Possible\n",i+1);
		else printf("Case #%d: Broken\n",i+1);
	}
	
	return 0;
}
