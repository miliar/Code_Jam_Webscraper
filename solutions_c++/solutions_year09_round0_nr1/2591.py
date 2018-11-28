#include<iostream>
#include<fstream>
using namespace std;

struct node
{
	(node*) next[26];
	node()
	{
		for (int i = 0; i < 26; ++i)
			next[i] = NULL;
	}
} tnode[10000];

int nodecnt = 0;
int L, d, n;
int stack[16][26];
int num[16];
int total;

void TreeAdd(node *now, char*st, int c)
{
	if (now->next[ st[c] - 'a' ] == NULL)
	{
		now->next[ st[c] - 'a' ] = &tnode[nodecnt++];
	}
	if (c != L - 1) 
		TreeAdd(now->next[ st[c] - 'a' ], st, c + 1);
}

bool Check (node *now, char *st, int c)
{
	if (now->next[st[c] - 'a'] == NULL) return false;
	if (c == L - 1) return true;
	return Check(now->next[ st[c] - 'a' ], st, c + 1);
}

void Found(int c, node *now)
{
	int i;
	for (i = 1; i <= num[c]; ++i)
	{
		if (now->next[stack[c][i]] != NULL)
			if (c == L) total++;
			else Found(c + 1, now->next[stack[c][i]]);
	}
}

fstream ouf, inf;

int main()
{
	ouf.open("f:\\yy.txt", ios::out);
	inf.open("f:\\A-small-attempt1.in", ios::in);
	//scanf("%d %d %d", &L, &d, &n);
	inf>>L>>d>>n;
	int i;
	char st[16];
	node *head = &tnode[nodecnt++];
	for (i = 1; i <= d; ++i)
	{
		//getchar();
		//scanf("%s", &st);
		inf>>st;
		TreeAdd(head, st, 0);
	}

	int j;
	for (i = 1; i <= n; ++i)
	{
		//getchar();
		char ch;
		for (j = 1; j <= L; ++j)
		{
			num[j] = 0;
		//	ch = getchar();
			inf>>ch;
			if (ch == '(')
			{
				//ch =getchar();
				inf>>ch;
				while (ch != ')')
				{
					num[j]++;
					stack[j][num[j]] = ch - 'a';
					//ch = getchar();
					inf>>ch;
				}
			} else
			{
				num[j]++;
				stack[j][num[j]] = ch - 'a';
			}
		}
		total = 0;
		Found(1, head);
//		printf("Case #%d: %d\n", i, total);
		ouf<<"Case #"<<i<<": "<<total<<endl;
	}
	ouf.close();
	inf.close();
	return 1;
}