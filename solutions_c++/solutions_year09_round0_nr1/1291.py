#include <cstdio>
#include <cstring>
int L, D;

typedef struct Node *pNode;
struct Node {
	pNode child[26];
	Node() {
		memset(child, 0, sizeof(child));
	}
};

Node root;

void insert(pNode node, char *buf, int l) {
	if (l) {
		if (!node->child[*buf])
			node->child[*buf] = new Node();
		insert(node->child[*buf], buf + 1, l - 1);
	}
}	

void insert(char *buf) {
	for (char *pc = buf; *pc; pc++)
		*pc -= 'a';
	insert(&root, buf, L);
}

int getCount(pNode node, char *buf) {
	if (!*buf)
		return 1;
	if (*buf >= 'a' && *buf <= 'z')
		if (node->child[*buf - 'a'])
			return getCount(node->child[*buf - 'a'], buf + 1);
		else
			return 0;
	int sum = 0;
	char *rightBr = strchr(buf, ')');
	for (buf++; buf < rightBr; buf++) {
		if (node->child[*buf - 'a'])
			sum += getCount(node->child[*buf - 'a'], rightBr + 1);
	}
	return sum;
}

int getCount(char *buf) {
	return getCount(&root, buf);
}

int main(void) {
	int N;
	FILE *f = fopen("A-large.in", "r");
	FILE *out = fopen("A-large.out", "w");
	fscanf(f, "%d%d%d", &L, &D, &N);
	for (int i = 0; i < D; i++) {
		char buf[L + 3];
		fscanf(f, "%s", buf);
		insert(buf);
	}
	for (int i = 0; i < N; i++) {
		char buf[28 * L + 3];
		int k = 0;
		fscanf(f, "%s", buf);
		k = getCount(buf);
		fprintf(out, "Case #%d: %d\n", i+1, k);
	}
	fclose(out);
	fclose(f);
	return 0;
}
