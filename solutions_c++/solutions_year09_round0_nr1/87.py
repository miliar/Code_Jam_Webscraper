#include <stdio.h>
#include <string.h>

int match(char *str, char expr[15][26]){
	int i;
	for(i=0; str[i]; i++)
		if(!expr[i][str[i]-'a'])
			return 0;
	return 1;
}

int main(){
	int L, D, N;
	scanf("%d %d %d ", &L, &D, &N);
	int i;
	char dict[5000][16];
	for(i=0; i<D; i++)
		gets(dict[i]);
	for(i=0; i<N; i++){
		char expr[15][26];
		char str[28*16];
		gets(str);
		int j, pos, paren;
		memset(expr, 0, sizeof(expr));
		for(j=0, pos=0, paren=0; str[j]; j++){
			if(str[j]=='('){
				paren=1;
			}else if(str[j]==')'){
				paren=0;
				pos++;
			}else{
				expr[pos][str[j]-'a']=1;
				if(!paren) pos++;
			}
		}
		int res=0;
		for(j=0; j<D; j++)
			if(match(dict[j], expr))
				res++;
		printf("Case #%d: %d\n", i+1, res);
	}
	return 0;
}
