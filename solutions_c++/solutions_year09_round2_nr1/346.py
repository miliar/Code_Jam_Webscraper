#include <vector>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;

typedef struct node {
	char feat[100];
	bool hasF;
	double p;
	struct node *F, *notF;
} cell;
typedef cell *pointer;

typedef struct node2 {
	char feat[100];
	struct node2 *next;
} cell2;
typedef cell2 *pointer2;


const int MAX = 10000;
cell v[MAX];
cell2 v2[MAX];
int vp = 0, vp2 = 0;

pointer myAlloc() {
	return &(v[vp++]);
}

pointer2 myAlloc2() {
	return &(v2[vp2++]);
}

void myFree() {
	vp = 0;
}

void myFree2() {
	vp2 = 0;
}


pointer newCell() {
	pointer newC = myAlloc();
	newC->feat[0] = '\0';
	newC->p = 1.0;
	newC->hasF = false;
	newC->F = newC->notF = NULL;
	return newC;
}

pointer2 newCell2() {
	pointer2 newC = myAlloc2();
	newC->feat[0] = '\0';
	newC->next = NULL;
	return newC;
}

pointer2 newCell2(char feat[]) {
	pointer2 newC = myAlloc2();
	strcpy(newC->feat, feat);
	newC->next = NULL;
	return newC;
}



int L, line;
pointer head;
pointer2 headN;


pointer readInput() {
	if (line >= L) return NULL;

	pointer p = newCell();
	char c;

	while ((c = getchar()) != '(')
		if (c == '\n') line++;

	while ((c = getchar())== ' ' || c == '\n')
		if (c == '\n') line++;
	ungetc(c, stdin);

	double prob;
	scanf("%lf", &prob);
	p->p = prob;

	while ((c = getchar()) == ' ' || c == '\n')
		if (c == '\n') line++;

	if (c != ')') {
		char feat[100];
		feat[0] = c;
		int pos = 1;

		while ((c = getchar()) >= 'a' && c <= 'z')
			feat[pos++] = c;
		feat[pos] = '\0';

		strcpy(p->feat, feat);

		p->hasF = true;
		p->F = readInput();
		p->notF = readInput();
		while ((c = getchar()) != ')');
	}

	return p;
}


double findProb(pointer p) {
	if (p == NULL) return 1;

	double prob = 1;

	prob *= p->p;

	bool foundF = false;
	if (p->hasF) {
		for (pointer2 q = headN->next; q != NULL; q = q->next) {
			if (strcmp(q->feat, p->feat) == 0) {
				prob *= findProb(p->F);
				foundF = true;
			}
		}
	}
	if (!p->hasF || !foundF)
		prob *= findProb(p->notF);

	return prob;
}


int main() {
	int T;
	scanf("%d", &T);

	for (int cases = 1; cases <= T; cases++) {
		scanf("%d", &L);
		getchar(); // \n

		head = newCell();

		line = 0;
		head = readInput();

		printf("Case #%d:\n", cases);

		int A;
		scanf("%d", &A);

		for (int i = 0; i < A; i++) {
			char name[100];
			int n;
			headN = newCell2();

			scanf("%s %d", name, &n);
			for (int j = 0; j < n; j++) {
				char feat[100];
				scanf("%s", feat);

				pointer2 aux = newCell2(feat);
				aux->next = headN->next;
				headN->next = aux;
			}

			printf("%.7lf\n", findProb(head));
			myFree2();
		}


		myFree();
	}

	return 0;
}
