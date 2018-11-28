#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Node {
	double w;
	char name[100];
	struct Node *left;
	struct Node *right;
};
struct Node root;

void init(struct Node *current)
{
	current->left = NULL;
	current->right = NULL;
}

void parse(struct Node *current)
{
	char ctmp;
	while (scanf("%c", &ctmp) == 1)
		if (ctmp == '(')
			break;
	scanf("%lf", &(current->w));
//	printf("w = %lf\n", current->w);
	while ((ctmp = getc(stdin)) == ' ');
	if (ctmp == ')')	return;
	else	ungetc(ctmp, stdin);
	scanf("%s", current->name);
//	printf("feature = %s\n", current->name);
	current->left = (struct Node *) malloc(sizeof(struct Node));
	current->right = (struct Node *) malloc(sizeof(struct Node));
	init(current->left);
	init(current->right);
//	printf("parse left\n");
	parse(current->left);
//	printf("parse right\n");
	parse(current->right);
	while (scanf("%c", &ctmp) == 1)
		if (ctmp == ')')
			break;
}

char features[105][100];
int n;

double pred(struct Node *current, double p)
{
	p = p*current->w;
	if (current->left == NULL)	return p;

	for (int i = 0; i<n; i++)
		if (strcmp(features[i], current->name) == 0) {
//			printf("pred go left, feature = %s\n", current->name);
			return pred(current->left, p);
		}
		
//	printf("pred go right, feature = %s\n", current->name);
	return pred(current->right, p);
}

void release(struct Node *current)
{
	if (current == NULL)	return;
	release(current->left);
	free(current->left);
	release(current->right);
	free(current->right);
}

int main()
{
	int N, dtmp, A;
	char str[100];
	scanf("%d", &N);
	for (int iter = 1; iter <= N; iter++) {
		printf("Case #%d:\n", iter);
		scanf("%d", &dtmp);
		init(&root);
		parse(&root);
		scanf("%d", &A);
		for (int a = 0; a<A; a++) {
			scanf("%s%d", str, &n);
			for (int i = 0; i<n; i++)
				scanf("%s", features[i]);

			double ans = pred(&root, 1.0);
			printf("%.06lf\n", ans);
		}
		release(&root);
	}
	return 0;
}

