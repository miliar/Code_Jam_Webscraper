#include <iostream>
using namespace std;

int l, d, n;
struct node
{
	char c;
	node * next;
}nlist[20];
char strlist[500][20];
int i, j;
char tmp[3000];

int main()
{
	freopen("e:\\a-easy.in", "r", stdin);
	freopen("e:\\a-easy.out", "w", stdout);
	scanf("%d%d%d", &l, &d, &n);
	for (i=0; i<d; i++)
	{
		scanf("%s", strlist[i]);
	}
	getchar();
	int np = 0;
	for (i=1; i<=n; i++)
	{
		gets(tmp);
		int flag = 0;
		int index = 0;
		node * p;
		np = 0;
		while (tmp[np] != 0)
		{
			if (tmp[np] == '(')
			{
				flag = -1;
				p = &nlist[index];
				np++;
				continue;
			}
			if (tmp[np] == ')')
			{
				flag = 0;
				index ++;
				np++;
				continue;
			}
			if (flag == 0)
			{
				nlist[index].c = tmp[np];
				nlist[index].next = NULL;
				index ++;
				np++;
				continue;
			}
			if (flag == -1)
			{
				p->c = tmp[np];
				if (tmp[np+1] != ')')
				{
					node * q = new node();
					p->next = q;
					p = p->next;
				}
				else
				{
					p->next = NULL;
				}
				np++;
			}
		}
		int cnt = 0;
		for (j=0; j<d; j++)
		{
			for (int k=0; k<l; k++)
			{
				node * p = &nlist[k];
				int flag = 0;
				while (p != NULL)
				{
					if (p->c == strlist[j][k])
					{
						p = NULL;
						flag = 1;
					}
					else
					{
						p = p->next;
					}
				}
				if (flag == 0)
				{
					break;
				}
				if ( k == l - 1 && flag == 1)
				{
					cnt++;
				}
			}
		}
		printf("Case #%d: %d\n", i, cnt);
	}
}