#include<stdio.h>
#include<string.h>
#include<math.h>
int main() {
	int i,j,T,L,P,C,cnt;
	freopen("google2.in","r",stdin);
	freopen("google2.out","w",stdout);
	scanf("%d", &T);
	for(i=0;i<T;i++){
		cnt = 0;
		scanf("%d %d %d", &L,&P,&C);
		if(L*C>=P) {printf("Case #%d: %d\n", i+1, 0);continue;}
		double ans = log((log(P) - log(L))/log(C))/log(2);
		cnt = (int)(ans+1e-6);
		if(cnt < ans - 1e-6)cnt+=1;		
		printf("Case #%d: %d\n", i+1, cnt);		
	}
	
	return 0;	
}
