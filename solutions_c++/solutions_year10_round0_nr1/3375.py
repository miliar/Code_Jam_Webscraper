#include <cstdio>

int pow(int x,int y){
	int t = 1,i;
	for(i = 1; i <= y; i++){
		t *= x;
	}
	return t;
}

int main(){
	//freopen("in.in","rt",stdin);
	//freopen("out.out","wt",stdout);
	int N,K,T,i;
	scanf("%d",&T);	
	for(i = 0; i < T; i++){
		scanf("%d %d",&N,&K);
		int x = pow(2,N);		
		if( (K + 1)% x == 0)
			printf("Case #%d: ON\n",i+1);
		else
			printf("Case #%d: OFF\n",i+1);
	}
	//fclose(stdin);
	//fclose(stdout);
	return 0;
}