#include<stdio.h>
#include<string.h>

using namespace std;

int main(){
	int T,i,j,N;
	char C[104], R[30]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	scanf("%d ",&T);
	for(i=1; i<=T; i++){
		gets(C);
		N=strlen(C);
		for(j=0; j<N; j++){
			if(C[j]!=' ')
				C[j]= R[C[j]-'a'];
		}
		printf("Case #%i: %s\n",i,C);
	}
	return 0;
}
