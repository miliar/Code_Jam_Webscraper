#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct NODE
{
	int value;
	NODE* child[26];
};
char words[5001][16];
int l,n,d;
int length;
__int64 ans;
char question[500];
void addtotree(NODE* node, char myword[])
{
	for (int level = 0; level < l; ++level)
	{
		if (node->child[myword[level]-'a'] == NULL)	node->child[myword[level]-'a'] = new NODE();
		node = node->child[myword[level]-'a'];
		node->value = myword[level]-'a';
	}

}
NODE* root;
char* getitem(char st[], int start, int end)
{
	char item[30];
	strcpy(item, "");
	int index = 0;
	if (st[start] == '(')
	{
		start += 1;
		while (st[start] >='a' && st[start] <= 'z') item[index++] = st[start++];
		item[index]=0;
		return item;
	}
	item[0] = st[start];
	item[1] = 0;
	return item;

}

void findans(NODE* node, char question[], int start)
{
	bool f = false;
	for (int i = 0; i < 26; ++i)
		if (node->child[i] != NULL) 
		{
			f = true;
			break;
		}
	if (f == false) 
	{
		ans += 1;
		return;
	}
	if (start >= length) return;
	char item[30];
	strcpy(item, getitem(question, start, length));
	if (strlen(item) == 1) start += 1;
	else start += (strlen(item) + 2);

	for (int i = 0; i < strlen(item); ++i)
	{
		if (node->child[item[i] - 'a'] != NULL) findans(node->child[item[i] - 'a'], question, start);
	}

	
}
int main()
{
	root = new NODE();
	FILE *fp;
	freopen("input.txt","r",stdin);
	freopen("output2.txt","w",stdout);
	scanf("%d%d%d", &l, &d, &n);
	for (int i = 1; i <= d; ++i) 
	{
		scanf("%s", &words[i]);
		addtotree(root, words[i]);
	}
	for (int i = 1; i<=n; ++i)
	{
		ans = 0;
		scanf("%s",&question);
		length =strlen(question);
		findans(root, question, 0);
		printf("Case #%d: %I64d\n",i, ans);
	}
	return 0;
}