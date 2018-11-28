#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <queue>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

int geti() { int n; scanf("%d", &n); return n; }

#define i(n) for (int i = 0; i < (n); i++)
#define j(n) for (int j = 0; j < (n); j++)

typedef pair<int,int> pii;

struct TrieNode {
	int letter;
	TrieNode *next[26];
	TrieNode(char c) : letter(c) {
		i(26) {
			next[i] = NULL;
		}
	};
};

int toIndex(char c) {
	return c - 'a';
}

int L, D, N;
TrieNode *root;

void addWord(char *word, TrieNode *root) {
	if (word[0] == '\0') return;
	int ci = toIndex(word[0]);
	if (root->next[ci] == NULL) {
		root->next[ci] = new TrieNode(word[0]);
	}
	addWord(word+1, root->next[ci]);
}

int sum(char *pattern, TrieNode *root) {
	if (root == NULL) {
		return 0;
	} else if (pattern[0] == '\0') {
		return 1;
	} else if (pattern[0] != '(') {
		return sum(pattern+1, root->next[toIndex(pattern[0])]);
	} else {
		char *np = ++pattern;
		while (*(np++) != ')');
		int s = 0;
		for (; pattern < np-1; pattern++) {
			s += sum(np, root->next[toIndex(pattern[0])]);
		}
		return s;
	}
}

int main() {

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	L = geti();
	D = geti();
	N = geti();

	root = new TrieNode('\0');

	i(D) {
		char buff[1000];
		scanf("%s", buff);
		addWord(buff, root);
	}

	for (int Case = 1; Case <= N; Case++) {
		char pattern[10000];
		scanf("%s", pattern);
		printf("Case #%d: %d\n", Case, sum(pattern, root));
	}
}