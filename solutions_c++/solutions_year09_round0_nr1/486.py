/**********************************************************************
Author: littlekid@whu
Created Time:  2009-9-3 12:53:03
File Name: gcj2009\QR\A.cpp
Description: 
**********************************************************************/
#include <iostream>
#include <string>
using namespace std;

const int MAXN = 5000;

typedef struct t_trie {
	t_trie *next[26];
	bool is_word;
};

t_trie trie;

void insert_word(char *str) {
	int id;
	t_trie *p = &trie;
	while (*str) {
		id = *str-'a';
		if (p->next[id] == NULL) {
			p->next[id] = new t_trie;
			p->next[id]->is_word = false;
			for (int ix = 0; ix < 26; ++ix) {
				p->next[id]->next[ix] = NULL;
			}
		}
		p = p->next[id];
		str++;	
	}
}

void dfs(char *pattern, t_trie *p, int pos, int len)
{
	if (len == 0) {
		p->is_word = true;
		return ;
	}
	--len;
	if (pattern[pos] == '(') {
		++pos;
		int nxt = pos;
		while (pattern[nxt] != ')') 
			++nxt;
		++nxt;
		while (pattern[pos] != ')') {
			if (p->next[ pattern[pos]-'a' ] != NULL)
				dfs(pattern, p->next[ pattern[pos]-'a' ], nxt, len);
			++pos;
		}
	} else {
		if (p->next[ pattern[pos]-'a' ] != NULL)
			dfs(pattern, p->next[ pattern[pos]-'a' ], pos+1, len);
	}
}

int word_count(t_trie *p, int len)
{
	if (len == 0) {
		if (p->is_word) {
			p->is_word = false;
			return 1;
		}
		else { 
			return 0;
		}
	}
	int res = 0;
	for (int ix = 0; ix < 26; ++ix) {
		if (p->next[ix] != NULL) 
			res += word_count(p->next[ix], len-1);
	}
	return res;
}

int main() 
{
	int L, D, N;
//	freopen("F:\\ACM\\gcj2009\\QR\\a.in", "r", stdin);
//	freopen("F:\\ACM\\gcj2009\\QR\\a.out", "w", stdout);
	scanf("%d %d %d", &L, &D, &N);
	char word[L+2];
	for (int ix = 0; ix < 26; ++ix) {
		trie.next[ix] = NULL;
	}
	for (int ix = 0; ix < D; ++ix) {
		scanf("%s", word);
		insert_word(word);
	}
	char pattern[L*26+L*4+1000];
	for (int ix = 0; ix < N; ++ix) {
		scanf("%s", pattern);	
		dfs(pattern, &trie, 0, L);
		cout << "Case #" << ix+1 << ": " << word_count(&trie, L) << endl;
	}
    return 0;
}

