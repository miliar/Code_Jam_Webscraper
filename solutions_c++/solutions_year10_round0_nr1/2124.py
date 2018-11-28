#include <cstdio>
using namespace std;
int main(){
	
	/*freopen("A-large.in","r", stdin);
	freopen("salida.out","w", stdout);*/
	int N, K, T;
	scanf("%d", &T);
	for( int i=1;i<=T;i++ ){
		scanf("%d%d", &N, &K);
		int pot=1<<N;
		if( K==0 || K<(pot-1) )
			printf("Case #%d: OFF\n", i);
		else{
			if( K==(pot-1) || (K-pot+1)%(pot)==0 )
			printf("Case #%d: ON\n", i);
			else printf("Case #%d: OFF\n", i);
		}	
	}
	return 0;
}

