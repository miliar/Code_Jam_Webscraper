#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>

using namespace std;

struct Trie{
	Trie *child[27];
	int end;
};

Trie tree[100000];
int tri;
int ans;
int L,D,N;

void insert(Trie *trie, char *word){
	int i = 0;
	int j;
	while( word[i] ){
		j = word[i] - 'a';
		if( trie->child[j] == NULL )	trie->child[j] = &tree[tri++];
		trie = trie->child[j];
		i++;
	}
	trie->end = 1;
	return ;
}

void count(Trie *trie, char *word, int l){
	if( l == L && trie->end ){	ans++;	return ;	}
	int i = 0;
	int j;
	int r;
	if( word[i] == '(' ){
		i++;	r = i;
		while( word[r] != ')' )	r++;
		r++;
	}
	else	r = i+1;
	
	for(; word[i] != ')' && i < r; i++){
		j = word[i] - 'a';
		if( trie->child[j] == NULL )	continue;
		count(trie->child[j], word+r,l+1);
	}
	return ;
}

int main()
{
	freopen("AL.out","w",stdout);
	scanf("%d%d%d\n",&L,&D,&N);
	memset(tree,0,sizeof(tree));
	tri = 0;
	Trie *root = &tree[tri++];
	
	char tmp[20];
	for(int i = 0; i < D; i++){
		scanf("%s",tmp);
		insert(root,tmp);
	}
	char pat[500];
	for(int i = 1; i <= N; i++){
		ans = 0;
		scanf("%s",&pat);
		count(root,pat,0);
		printf("Case #%d: %d\n",i,ans);
	}

	return 0;
}
		
