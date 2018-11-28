#include <iostream>

#define MAX 5002
using namespace std;

const int mm = 27;
struct Node
{
	Node *p[mm];
	Node()
	{
		for(int i = 0; i < mm; i++)
			p[i] = NULL;
	}
}*k, *pp;

int l, d, n;
char str[20], cas[mm*20];
int mat[20][mm];
int ans;


void dfs(int t, Node *p)
{
	if(t >= l-1)
	{
		ans++;
		return;
	}
//	printf("***%d\n", t);
	int i;
	for(i = 0; i < mm; i++)
		if(mat[t][i] && p->p[i])
			dfs(t+1, p->p[i]);
	return;
}

void solve()
{
	memset(mat, 0, sizeof(mat));
	int i, j, t;
	t = 0;
	for(j = -1, i = 0; i < strlen(cas); i++)
	{
		if(cas[i] == '(')
		{
			t = 1;
			j++;
		}
		else	if(cas[i] == ')')
			t = 0;
		else if(t)
		{
			mat[j][cas[i]-'a'] = 1;
		}
		else
		{
			j++;
			mat[j][cas[i]-'a'] = 1;
		}
	}
/*	printf("%s\n", cas);
	for(i = 0; i < l; i++)
	{
		for(j = 0; j < mm; j++)
			printf("%d ", mat[i][j]);
		printf("\n");
	}
	*/
	ans = 0;
	dfs(0, k);
}



int main()
{
//	freopen("A-small-attempt3.in", "r", stdin);
//	freopen("out.txt", "w", stdout);
	int i, j, t;
	while(scanf("%d%d%d", &l, &d, &n) != EOF)
	{
		k = new Node;
		for(i = 0; i < d; i++)
		{
			scanf("%s", str);
			pp = k;
			for(j = 0; j < l; j++)
			{
				t = str[j] - 'a';
				if(pp->p[t] == NULL)
					pp->p[t] = new Node;
				pp = pp->p[t];
			}
		}
		i = 0;
		while(i < n)
		{
			scanf("%s", cas);
			solve();
			printf("Case #%d: %d\n", i+1, ans);
			i++;
		}
	}
return 0;
}