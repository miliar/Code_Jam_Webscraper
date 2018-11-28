//============================================================================
// Name        : A.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;
#define MAXW 102
#define MAXN 102

typedef struct TRIE{
	int next[36];
	bool isword;
}NODE;

NODE trie[MAXW*MAXN];
int N,M,numW,outp;
FILE *out;

void insert(char word[]){//trie insert
	int len=(int)strlen(word);
//	fprintf(out, "len:%d\n", len);
	int i,j,ptr;
	for(i = 1, ptr=1; i < len; ++i){
		if(word[i] == '/'){
			trie[ptr].isword = true;
			continue;
		}
		if(word[i] >= 'a' && word[i] <= 'z')
			j = word[i]-'a';
		else
			j = word[i]-'0'+26;
		if(trie[ptr].next[j] == 0)
			trie[ptr].next[j] = ++numW;//°O¿ý¦r¥Àªºindex
//		fprintf(out, "%d ", trie[ptr].next[j]);
		ptr = trie[ptr].next[j];

	}
	trie[ptr].isword = true;
//	fprintf(out, "\n");
}

int main() {
	int cas,ind,i,j,k,cnt=0,ptr;
	char s[MAXW];
	freopen("A-small-attempt0.in", "r", stdin);
	out = fopen("output.txt", "w");
	scanf("%d", &cas);
	while(cas--){
		scanf("%d%d", &N, &M);
		gets(s);
		numW = 1;
		outp = 0;
		memset(trie,0,sizeof(trie));
		for(i = 0; i < N; ++i){
			ind = -1;
			scanf("%s", s);
			printf("%s\n", s);
			insert(s);
		}
		for(i = 0; i < M; ++i){
			ind = -1;
			ptr = 1;
			scanf("%s", s);
			printf("%s", s);
			for(j = 1; j < (int)strlen(s); ++j){
				if(s[j] == '/'){
					if(!trie[ptr].isword){
						++outp;
						trie[ptr].isword = true;
					}
				}
				else{
					if(s[j] >= 'a' && s[j] <= 'z')
						k = s[j] - 'a';
					else if(s[j] >= '0' && s[j] <= '9')
						k = s[j] - '0' + 26;
					if(trie[ptr].next[k] == 0)
						trie[ptr].next[k] = ++numW;
					ptr = trie[ptr].next[k];
				}
			}
			if(!trie[ptr].isword){
				++outp;
				trie[ptr].isword = true;
			}
			putchar('\n');
		}
		fprintf(out, "Case #%d: %d\n", ++cnt, outp);
	}
	fclose(out);
	return 0;
}
