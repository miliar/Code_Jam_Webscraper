#include<stdio.h>

int trie[100000][30],top;
int L,D,N,K;
char str[1024];
int mundo[17][27];

void intro(char *c){
	int w;
	for(w=0;*c;w=trie[w][*c-'a'],c++)
		if(!trie[w][*c-'a']) trie[w][*c-'a']=++top;
	trie[w][29]=1;
}

void leer(){ gets(str); }
void escribir(int caso){ printf("Case #%i: %i\n",caso,K);}
void interpreta(){
	int i,j;
	for(i=0;i<L;i++)
		for(j=0;j<26;j++)	mundo[i][j]=0;
	for(i=0,j=0;j<L && str[i];j++,i++){
		if(str[i]=='('){
			while(str[++i]!=')') mundo[j][str[i]-'a']=1;
		} else mundo[j][str[i]-'a']=1;
	}
}

void busca(int l=0,int w=0){
	if(trie[w][29]){ K++; return; }
	for(int i=0;i<26;i++)
		if(trie[w][i] && mundo[l][i]) busca(l+1,trie[w][i]);
}

int main(){
	scanf("%i%i%i\n",&L,&D,&N);
	while(D--){
		leer(); 
		intro(str);
	}
	for(int i=1;i<=N;i++){
		K=0;
		leer();
		interpreta();
		busca();
		escribir(i);
	}
	return 0;
}

