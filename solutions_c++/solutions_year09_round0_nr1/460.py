#include <iostream>
#include <string>

using namespace std;

#define SZ(c) ((int) c.size())

const int MAX_L = 15;

int L;
int D;
int N;
char word[16];
char pattern[512];

struct trie_t {
	trie_t *children[26];
	trie_t() {
		memset(children, 0, sizeof(children));
	}
};

trie_t *root;

void trie_add(trie_t *tree, const char *s)
{
	if (*s == '\0')
		return;
	int k = *s - 'a';
	if (tree->children[k] == NULL) 
		tree->children[k] = new trie_t();
	trie_add(tree->children[k], s + 1);
}

int trie_get(trie_t *tree, const char *p)
{
	if (tree == NULL)
		return 0;
	if (*p == '\0')
		return 1;
	int res;
	if (*p == '(') {
		const char *q;
		for (q = ++p; *q != ')'; ++q) ;
		res = 0;
		for (const char *s = p; s != q; ++s) {
			int k = *s - 'a';
			res += trie_get(tree->children[k], q + 1);
		}
	} else {
		res = trie_get(tree->children[*p - 'a'], p + 1); 
	}
	return res;
}

int main()
{
	scanf("%d %d %d", &L, &D, &N);
	root = new trie_t();
	for (int i = 0; i < D; ++i) {
		scanf("%s", word);
		trie_add(root, word);
	}
	for (int casenum = 1; casenum <= N; ++casenum) {
		scanf("%s", pattern);
		printf("Case #%d: %d\n", casenum, trie_get(root, pattern));
	}
	return 0;
}
