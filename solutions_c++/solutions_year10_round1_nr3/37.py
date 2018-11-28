#include <stdio.h>

typedef long long LL;
LL MIN(LL a,LL b){
	return a<b? a:b;
}
LL MAX(LL a, LL b){
	return a<b? b:a;
}

LL P(LL A, LL B){
	if(A==0 || B==0) return 0;
	LL ans=0LL;
	LL Fa=3, Ga=1, Fb=2, Gb=1;
	LL x = 0;
	while(A>=Fa*1 && B>=Fb*1){
		for(x=1;A - Fa*x >=0 && B - Fb*x>=0;x++){
			ans += MAX(0, MIN((A - Fa * x)/Ga+1, (B - Fb * x)/Gb+1));
		}
		Fb += Fa; 
		Gb += Ga;
		Fa += Fb;
		Ga += Gb;
	}
		//printf("P(%I64d, %I64d) = %I64d\n", A, B, ans);
	return ans;
}

LL R(LL A, LL B){

	return A*B - P(A, B) - P(B, A) - MIN(A,B);
}
LL Q(LL A1, LL A2,LL B1, LL B2){
//printf("R(%I64d,%I64d) = %I64d\n", A2, B2, R(A2, B2));
	return R(A2, B2) - R(A1-1, B2) - R(A2, B1-1) + R(A1-1, B1-1);
}

int main(void)
{
	int T, cs;
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++){
		LL a1,a2,b1,b2;
		scanf("%I64d%I64d%I64d%I64d",&a1,&a2,&b1,&b2);
		printf("Case #%d: %I64d\n", cs, Q(a1,a2,b1,b2));
		fprintf(stderr,"Case #%d: %I64d\n", cs, Q(a1,a2,b1,b2));
	}
	return 0;
}
