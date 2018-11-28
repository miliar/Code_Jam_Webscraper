#include<cstdio>
#include<cstring>
char comb[30][30];
bool elim[30][30];
int main(){
	int T;
	int C;
	int D;
	int N;
	char s[105];
	bool clear;
	scanf("%d",&T);
	for (int k=1; k <= T; ++k){
		memset(comb,0,sizeof(comb));
		memset(elim,0,sizeof(elim));
		scanf("%d",&C);
		for (int i=0; i < C; ++i){
			scanf("%s",s);
			comb[ s[0] - 'A'][ s[1] - 'A' ] = s[2];
			comb[ s[1] - 'A'][ s[0] - 'A' ] = s[2];
		}
		scanf("%d",&D);
		for (int i=0; i < D; ++i){
			scanf("%s",s);
			elim[ s[0] - 'A'][ s[1] - 'A' ] = true;
			elim[ s[1] - 'A'][ s[0] - 'A' ] = true;
		}
		scanf("%d",&N);
		scanf("%s",s);
		char sol[105];
		int n = 0;
		for (int i=0; i < N; ++i){
			sol[n++] = s[i];
			if (n > 1 && comb[sol[n-1]-'A'][sol[n-2]-'A'] !='\0'){
				sol[n-2] = comb[sol[n-1]-'A'][sol[n-2]-'A'];
				n--;
			}
			else {
				clear = false;
				for (int j=0; j < n-1; ++j) if ( elim[ sol[j] - 'A' ][ sol[n-1] - 'A' ] ){ 
					clear = true;
					break;
				}
				if (clear) n = 0;
			}
		}
		printf("Case #%d: [",k);
		if (n){
			for (int i=0; i < n; ++i)
				if (i) printf(", %c",sol[i]);
				else printf("%c",sol[i]);
		}
		printf("]\n");
	}

	return 0;
}