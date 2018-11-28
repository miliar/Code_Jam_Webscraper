#include <vector>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

typedef struct node {
	struct node *next[26];
} cell;
typedef cell *pointer;

pointer *head;

const int MAX = 100000;
cell v[MAX];
int vp = 0;
pointer myAlloc() {
	return &(v[vp++]);
}

void myFree() {
	vp = 0;
}


pointer newCell() {
	pointer p = myAlloc();
	for (int k = 0; k < 26; k++)
		p->next[k] = NULL;
	return p;
}

int findNumWords(int line[][26], int pos, pointer p, int len) {
	if (pos == len && p != NULL)
		return 1;
	if (p == NULL && pos != 0)
		return 0;

	int soma = 0;
	for (int i = 0; i < 26 && line[pos][i] != -1; i++) {
		if (pos == 0) // head
			soma += findNumWords(line, pos+1, head[line[pos][i]], len);
		else
			soma += findNumWords(line, pos+1, p->next[line[pos][i]], len);
	}

	return soma;
}


int main() {
	int L, D, N;
	scanf("%d %d %d", &L, &D, &N);
	getchar(); // \n

	head = new pointer[26];
	for (int i = 0; i < 26; i++)
		head[i] = NULL;

	char c;

	for (int i = 0; i < D; i++) {
		pointer p = NULL;

		for (int j = 0; j < L; j++) {
			c = getchar() - 'a';

			if (p == NULL) { // head
				if (head[c] == NULL) head[c] = newCell();
				p = head[c];
			}
			else {
				if (p->next[c] == NULL)
					p->next[c] = newCell();
				p = p->next[c];
			}
		}

		getchar(); // \n
	}

	for (int i = 1; i <= N; i++) {
		int line[L][26];
		char word[1000];

		for (int j = 0; j < L; j++)
			for (int k = 0; k < 26; k++)
				line[j][k] = -1;

		scanf("%s", word);
		int size = strlen(word);
		bool loop = false;
		int pos1 = 0, pos2 = 0;

		for (int j = 0; j < size; j++) {
			c = word[j];

			if (c == '(')
				loop = true;
			else if (c == ')') {
				pos1++;
				pos2 = 0;
				loop = false;
			}

			else {
				if (!loop)
					line[pos1++][0] = c - 'a';
				else
					line[pos1][pos2++] = c - 'a';
			}
		}

		printf("Case #%d: %d\n", i, findNumWords(line, 0, NULL, L));
	}

	return 0;
}

