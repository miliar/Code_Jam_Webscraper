#include <stdio.h>
#include <stdlib.h>
#include <string.h>

class Cute {
public:
	char trait[20];
	double val;
	Cute *ifyes, *ifno;
	Cute() {  *trait = 0; val = 1.0; ifyes=NULL; ifno=NULL; }
};

int nextChar() {
	int c;
	do {
		c= getchar();
	} while (c!=EOF && (c==' ' || c=='\t' || c=='\n'));
	return c;
}

int cmp(const void *a, const void *b) {
	return strcmp((char*)a, (char*)b);
}
	

double match(Cute *root, double init, int ntraits, char traits[][20]) {
	double val = init * root->val;
	if (!root->trait[0])
		return val;
	if (bsearch(root->trait, traits,  ntraits, 20, cmp)) {
		val = match(root->ifyes, val, ntraits, traits);
	} else
		val = match(root->ifno, val, ntraits, traits);
	return val;
}

Cute *parse() {
	Cute *root = new Cute;
	double val;
	char buf[100];
	int i;
	int c = nextChar();
	if (c=='(') {
		scanf("%lf", &val);
		root->val = val;
		c = nextChar();
		if (c==')')
			return root;
		i = 0;
		while (c != '(') {
			buf[i++] = c;
			c = nextChar();
		}
		ungetc(c, stdin);
		buf[i] = 0;
		strcpy(root->trait, buf);
		root->ifyes = parse();
		root->ifno = parse();
		nextChar(); // )
	}
	return root;
}

Cute *topParse() {
	Cute *cute = parse();
	int c;
	while ((c = getchar() )!= '\n')
		;
	return cute;
}

void printTree(Cute *root, int d=0) {
	int i;
	for (i=0; i < d*2; i++) putchar(' ');
	printf ("(%lf ", root->val);
	if (!root->trait[0]) {
		printf(")\n");
		return;
	}
	printf ("%s\n", root->trait);
	if (root->ifyes)
		printTree(root->ifyes, d+1);
	if (root->ifno)
		printTree(root->ifno, d+1);
	for (i=0; i < d*2; i++) putchar(' ');
	printf (")\n");
}

int main() {
	int N, i, j;
	scanf("%d\n", &N);
	for (i=0; i < N; ++i) {
		int nlines, nanims;
		scanf("%d\n", &nlines); // ignored
		Cute *tree;
		tree = topParse();
//		printTree(tree);
		scanf("%d\n", &nanims);
		printf("Case #%d:\n", i+1);
		for (j=0; j<nanims; j++) {
			char animal[100], trait[100][20];
			int ntraits;
			scanf("%s %d", animal, &ntraits);
			for (int k=0; k < ntraits; k++)
				scanf("%s", trait[k]);
			qsort(trait, ntraits, 20, cmp);
#if 0
			printf ("%s ", animal);
			for (int k=0; k < ntraits; k++)
				printf("%s ", trait[k]);
			printf("\n");
#endif
			printf ("%lf\n", match(tree, 1.0, ntraits, trait));
		}
		delete tree;
	}
	

}
