#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int N, L, A;

typedef struct Node
{
	char feature[15];
	float data;
	struct Node* left;
	struct Node* right;
	struct Node* father;
}Node;

void destroy(Node* root)
{
	if (root == NULL)
	{
		return;
	}
	delete[] root->feature;
	destroy(root->left);
	destroy(root->right);
}

Node* root;
int top;
char tempC[100];
char tempA[110][100];

void push()
{
	++top;
}

void pop()
{
	--top;
}

int empty()
{
	if (top == 0)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

void clear()
{
	top = 0;
}

void print(Node* root)
{
	if (root == NULL)
	{
		return;
	}
	printf("%s %f\n", root->feature, root->data);
	print(root->left);
	print(root->right);
}

void input(void)
{
	int i, flag;
	float data;
	char op;
	Node** cur;
	Node* father = NULL;
	scanf("%d", &L);
//	destroy(root);
	root = NULL;
	cur = &root;
	clear();
	flag = 1;
	while (!empty() || flag)
	{
		flag = 0;
		op = ' ';
		while (op != '(' && op != ')')
		{
			scanf("%c", &op);
		}
		if (op == ')')
		{
			pop();
			continue;
		}
		push();
		*cur = new Node;
		(*cur)->father = father;
		(*cur)->left = NULL;
		(*cur)->right = NULL;
		scanf("%f", &((*cur)->data));
		scanf("%s", tempC);
		if (tempC[0] == ')')
		{
			i = 1;
			while (tempC[i] == ')')
			{
				pop();
				++i;
			}
			pop();
			(*cur)->feature[0] = '\0';
			while (father != NULL)
			{
				if (father->right == NULL)
				{
					cur = &(father->right);
					break;
				}
				father = father->father;
			}
		}
		else
		{
			strcpy((*cur)->feature, tempC);
			father = *cur;
			cur = &(father->left);
		}
	}
}

void solve(int index)
{
	int M, i, j, flag;
	float res;
	scanf("%d", &A);
	printf("Case #%d:\n", index);
	for (j = 0; j < A; ++j)
	{
		scanf("%s", &tempC);
		scanf("%d", &M);
		for (i = 0; i < M; ++i)
		{
			scanf("%s", tempA[i]);
		}

		Node* cur;
		cur = root;
		res = 1;
		while (cur != NULL)
		{
			res *= cur->data;
			flag = 1;
			for (i = 0; i < M; ++i)
			{
				if (strcmp(tempA[i], cur->feature) == 0)
				{
					flag = 0;
					break;
				}
			}
			if (flag == 0)
			{
				cur = cur->left;
			}
			else
			{
				cur = cur->right;
			}
		}
		printf("%.7f\n", res);
	}
}

int main(void)
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int i;
	scanf("%d", &N);
	root = NULL;
	for (i = 0; i < N; ++i)
	{
		input();
//		print(root);
		solve(i + 1);
	}
	return 0;
}
