#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Node
{
	char end;
	Node* p;
	Node* c[26];
};

Node* root, *tree;
char list[30][30];
int len[30], c, ans, l;
//char *token, sep[] = "()\n";

void clear(Node*& t)
{
	int i;
	for ( i = 0; i < 26; i++ )
	{
		if ( !t->c[i] ) continue;
		clear(t->c[i]);
	}
	free(t);
	t = NULL;
}

void recur(int a, Node* t)
{
	int i;
	if ( a == l )
	{
		if ( t->end ) ans++;
		return;
	}
	
	for ( i = 0; i < len[a]; i++ )
	{
		if ( !t->c[list[a][i]] ) continue;
		//printf("%d\n",list[a][i]);
		recur(a+1,t->c[list[a][i]] );
	}
}

int main()
{
	int d, n, i, j, t, length;
	int aa;
	char buffer[1000];
	gets(buffer);
	sscanf(buffer,"%d %d %d",&l,&d,&n);
	root = (Node*) malloc(sizeof(Node));
	memset(root->c,0,sizeof(root->c));
	root->end = 0;
	for ( i = 0; i < d; i++ )
	{
		gets(buffer);
		tree = root;
		for ( j = 0; j < l; j++ )
		{
			t = buffer[j]-'a';
			if ( !tree->c[t] )
			{
				tree->c[t] = (Node*) malloc(sizeof(Node));
				memset(tree->c[t]->c,0,sizeof(tree->c[t]->c));
				tree->c[t]->end = 0;
				tree->c[t]->p = tree;
			}
			tree = tree->c[t];
		}
		tree->end = 1;
	}
	
	for ( aa = 1; aa <= n; aa++ )
	{
		gets(buffer);
		
		i = c = 0;
		memset(len,0,sizeof(len));
		length = strlen(buffer);
		while ( i < length )
		{
			if ( buffer[i] != '(' ) {
				list[c][len[c]++] = buffer[i++]-'a';
				c++;
				continue;
			}
			i++;
			while ( buffer[i] != ')' ) {
				//printf("%d [%c]\n",c,buffer[i]);
				list[c][len[c]++] = buffer[i++]-'a';
			}
			i++;
			c++;
		}
		ans = 0;
		recur(0, root);
		printf("Case #%d: %d\n",aa,ans);
	}

	clear(root);
	return 0;
}

