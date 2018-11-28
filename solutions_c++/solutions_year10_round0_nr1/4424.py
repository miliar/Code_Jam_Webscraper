#include<iostream>
using namespace std;

int main(){
	int T,N,K;
	freopen("C:\\Documents and Settings\\yx\\×ÀÃæ\\1.txt","w",stdout);
	scanf("%d",&T);
	for(int cas = 1;cas <= T; ++cas){
		scanf("%d %d",&N,&K);
		K %= (1 << N);
		if(K == (1 << N) - 1)
			printf("Case #%d: ON\n",cas);
		else
			printf("Case #%d: OFF\n",cas);

	}
	return 0;
}