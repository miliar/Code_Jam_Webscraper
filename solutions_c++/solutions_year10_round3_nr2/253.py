#include <stdio.h>
#include <math.h>
long long  min(long long A,long long B){
	if(A>B) return B;
	return A;
}
long long max(long long A,long long B){
	if(A == 1000) return B;
	if(A>B) return A;
	return B;
}
int counter(long long L,long long P,long long C){
	if(P<=C*L) return 0;
//	printf("1: %Ld %Ld %Ld\n",L,P,C);
	long long X = (long long)(sqrt((double)P*L));
	long long X2 = (long long)(sqrt((double)P*L)+1);

//	printf("1: %Ld %Ld %Ld\n",L,P,C);
	int ct1,ct2,ct3,ct4;
	ct1 = ct2 = ct3 = ct4 = 1000;
	if(L != X)
		ct1 = counter(X,P,C);
	if(P != X)
		ct2 = counter(L,X,C);
	if(L!=X2)
		ct3 = counter(X2,P,C);
	if(P !=X2)
		ct4 = counter(L,X2,C);

	return min(max(ct1,ct2),max(ct3,ct4))+1;
}


int main(){
	int T;
	long long L,P,C;
	scanf("%d",&T);
	for(int i =0;i<T;i++){
		scanf("%Ld %Ld %Ld",&L,&P,&C);
		printf("Case #%d: %d\n",i+1,counter(L,P,C));
	}
	return 0;
}
