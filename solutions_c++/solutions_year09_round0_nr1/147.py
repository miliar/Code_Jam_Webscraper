#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <string>

using namespace std;

struct node{
	node *next[26];
	int count;
};

int L, D, N;
vector <char> Pos[20];
node *Root;

node *newNode(void){
	node *ret = new node;
	memset(ret -> next, 0, sizeof(ret -> next));
	ret -> count = 0;
	return ret;
}

int insert(char *s){
	node *now = Root;
	for (int i = 0; i < L; i ++){
		int id = s[i] - 'a';
		if (!now -> next[id]) now -> next[id] = newNode();
		now = now -> next[id];
	}
	now -> count ++;
	return 0;
}

int count(node *now, int depth){
	if (depth >= L)
		return now -> count;
	int ret = 0;
	for (int i = 0; i < Pos[depth].size(); i ++){
		int id = Pos[depth][i] - 'a';
		if (now -> next[id]) ret += count(now -> next[id], depth + 1);
	}
	return ret;
}

int main(void){
	Root = newNode();
	scanf("%d%d%d", &L, &D, &N);
	for (int i = 0; i < D; i ++){
		char s[50];
		scanf("%s", s);
		insert(s);
	}
	for (int i = 0; i < N; i ++){
		for (int j = 0; j < L; j ++) Pos[j].clear();
		char s[1000];
		scanf("%s", s);
		int len = strlen(s), p = 0;
		for (int j = 0; j < len; p ++){
			if (s[j] == '('){
				int k;
				for (k = j + 1; s[k] != ')'; k ++) Pos[p].push_back(s[k]);
				j = k + 1;
			}  else {
				Pos[p].push_back(s[j]);
				j ++;
			}
		}
		printf("Case #%d: %d\n", i + 1, count(Root, 0));
	}
	return 0;
}
