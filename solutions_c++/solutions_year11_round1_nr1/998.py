#include <stdio.h>

void simple (long long int * PD, long long int * D){
	while ( (*PD) % 2 == 0 && (*D) %2==0){
		(*PD)/=2;
		(*D)/=2;
	}
	while ( (*PD) % 5 == 0 && (*D) %5==0){
		(*PD)/=5;
		(*D)/=5;
	}

}
int main(){
    int T,T_index;
    int i,j,index;
    long long int N, PD, PG,D,G;
    scanf("%d",&T);
    for (T_index=1;T_index<=T;T_index++){
        printf("Case #%d: ",T_index);
        scanf("%lld %lld %lld",&N,&PD,&PG);
//		printf("N is %lld\n",N);
//        scanf("%lld %lld %lld",&N,&PD,&PG);
		
        D = G = 100;
        simple(&PD, &D);
        simple(&PG, &G);
		if (D <=N && PD <= PG && D <= G && (D-PD) <= (G-PG) ){
//		if (D <=N && (G-PG)!=0 ){
			printf("Possible\n");
		}else if( PD != 0 && PG == 0) {
			printf("Broken\n");
		}else if( (D-PD) != 0 && (G-PG) == 0) {
			printf("Broken\n");
		}else if (D <=N ) {
			printf("Possible\n");
		}else  {
			printf("Broken\n");
		}
	}
}