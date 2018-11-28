#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <set>
using namespace std;

/*
 * from http://zh.wikipedia.org/wiki/Trie
 */
#define TREE_WIDTH 256
#define WORDLENMAX 128

const int WORD_LEN = 20;

char input[WORD_LEN][WORDLENMAX];
set<char> input_set[WORD_LEN];

struct trie_node_st {
	int count;
	struct trie_node_st *next[TREE_WIDTH];
};

static struct trie_node_st root = { 0, { NULL } };

int L, N, D;
int case_number;
int total_count = 0;

static int insert(const char *word) {
	int i;
	struct trie_node_st *curr, *newnode;

	if (word[0] == '\0') {
		return 0;
	}
	curr = &root;
	for (i = 0;; ++i) {
		if (curr->next[word[i]] == NULL) {
			newnode = (trie_node_st*) malloc(sizeof(struct trie_node_st));
			memset(newnode, 0, sizeof(struct trie_node_st));
			curr->next[word[i]] = newnode;
		}
		if (word[i] == '\0') {
			break;
		}
		curr = curr->next[word[i]];
	}
	curr->count++;

	return 0;
}

static char *spaces = " \t\n/.\"\'()";

static void printword(const char *str, int n) {
	printf("%s\t%d\n", str, n);
}

static int do_travel(struct trie_node_st *rootp) {
	static char worddump[WORDLENMAX + 1];
	static int pos = 0;
	int i;

	if (rootp == NULL) {
		return 0;
	}
	if (rootp->count) {
		worddump[pos] = '\0';
//		printword(worddump, rootp->count);
		total_count++;
	}
	for (i = 0; i < TREE_WIDTH; ++i) {
		worddump[pos] = i;
		if (input_set[pos].find((char)i) != input_set[pos].end()) {
			pos++;
			do_travel(rootp->next[i]);
			pos--;
		}

	}
	return 0;
}

int main(void) {

	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small.out", "w", stdout);

	cin >> L >> D >> N;

	char word[WORDLENMAX];
	for (int i = 0; i < D; i++) {
		cin >> word;
		insert(word);
	}

	case_number = 1;

	char target[TREE_WIDTH];
	for (int i = 0; i < N; i++) {
		char * word;
		cin >> target;

		// init
		memset(input, 0, sizeof(char) * WORDLENMAX * WORD_LEN);
		for (int i = 0; i < L; i++) {
			input_set[i].clear();
		}
		total_count=0;

		// input
		bool pass = false;
		int j = 0;
		int x = 0;
		int y = 0;
		while (target[j] != '\0') {
			if (target[j] == '(') {
				pass = true;
			} else if (target[j] == ')') {
				pass = false;
				x++;
				y = 0;
			} else {
				input[x][y++] = target[j];
				if (!pass) {
					x++;
					y = 0;
				}
			}
			j++;
		}
/*
		for (int i = 0; i < L; i++) {
			cout << input[i] << endl;
		}
		cout << endl;
*/
		for (int i = 0; i < L; i++) {
			for (int j = 0; input[i][j] != 0; j++) {
				input_set[i].insert(input[i][j]);
			}
		}

		// travel
		do_travel(&root);
		printf("Case #%d: %d\n", i + 1, total_count);
	}

	return 0;
}
