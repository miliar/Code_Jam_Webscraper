#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;


typedef struct node
{
	struct node * next[26];
	int count;
} node;

int sum;

vector<string> split(char *p)
{
	vector<string> vs;
	char *start;
	int flag = 0;
	while(*p != '\0')
	{
		if(*p == '(')
		{
			start = p+1;
			flag = 1;
		}
		else if(*p == ')')
		{
			string s(start, 0, p-start);
			flag = 0;
			vs.push_back(s);
		}
		else if(flag == 0)
		{
			string s(p, 0, 1);
			vs.push_back(s);
		}
		p++;
	}
	return vs;
}

void recursive(vector<string> vs, node *p, int n)
{
	if(!p)
	{
		return;
	}
	if(n == vs.size())
	{
		if(p->count != 1)
		{
			p->count = 1;
			sum ++;
			return ;
		}
	}
	for(int i=0; i<vs[n].size(); i++)
	{
		recursive(vs, p->next[vs[n][i]-'a'], n+1);
	}
}

void recursiveClear(node *p, int n, int all)
{
	if(!p)
	{
		return;
	}
	if(n == all)
	{
		p->count = 0;
		return;
	}
	for(int i=0; i<26; i++)
	{
		recursiveClear(p->next[i], n+1, all);
	}
}


int main()
{
	freopen("A-small-attempt5.in", "r", stdin);
	int L, D, N;
	scanf("%d%d%d", &L, &D, &N);
	
	node *root = (node *)malloc(sizeof(node));
	memset(root, 0, sizeof(node));
	for(int i=0; i<D; i++)
	{
		node *n = root;
		char c[11] = {0};
		scanf("%s", c);
		char *p = c;
		while(*p != '\0')
		{
			if(n->next[(*p)-'a'] == 0)
			{
				node *n1 = (node *)malloc(sizeof(node));
				memset(n1, 0, sizeof(node));
				n->next[(*p)-'a'] = n1;
				n = n1;
			}
			else
			{
				n = n->next[(*p)-'a'];
			}
			p++;
		}
	}

	ofstream out("out.txt");
	for(int i=0; i<N; i++)
	{
		sum = 0;
		char c[1000] = {0};
		scanf("%s", c);
		vector<string> vs = split(c);
		recursive(vs, root, 0);
		out << "Case #" << i+1 << ": " << sum << endl;
//		printf("Case #%d: %d\n", i+1, sum);
		recursiveClear(root, 0, L);
	}
	return 0;
}	
