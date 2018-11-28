#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const int MAX = 5001;
char word[MAX][20];
int L, D, T;

struct Node{
	bool used[26];
	void init(){		for(int i=0;i<26;++i)	used[i] = false;	}
	void assign(char ch){		used[ch-'a'] = true;	}
} node[20];

void parse(char *s){
	int i;
	for(i=0;i<L;++i){
		node[i].init();
		if( (*s)=='(' ){
			++s;
			while( (*s)!=')' ){
				node[i].assign( (*s) );
				++s;
			}
		}
		else	node[i].assign( (*s) );
		
		++s;
	}
}

int main(){
	int turn, T;
	//freopen("A-large.in","r",stdin);
	scanf("%d%d%d",&L,&D,&T);
	
	int i;
	for(i=0;i<D;++i)	scanf("%s",word[i]);	
	
	char str[1000];
	for(turn = 0;turn<T;++turn){
		scanf("%s",str);
		parse(str);
		int j, acc = 0;
		for(i=0;i<D;++i){
			bool match = true;
			for(j=0;j<L;++j){
				if( !node[j].used[ word[i][j]-'a' ] ){
					match = false;
					break;
				}
			}
			if( match )	++acc;
		}
		printf("Case #%d: %d\n",1+turn,acc);
	}
	
	return 0;
}
