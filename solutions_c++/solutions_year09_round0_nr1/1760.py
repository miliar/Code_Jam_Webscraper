#include <iostream>
#include <string.h>
#include <map>
#define MAXN 300

using namespace std;

int St[MAXN], End[MAXN];

struct tree
{
	tree(){ memset(next, 0, sizeof(next)); }
	char c;
	bool isleaf;
	tree * next[30];
}node[1000000];

int p, len;
char str[30];

void insert(int t, tree * now)
{
	if(t == len)
	{
		now->isleaf = true;
		return ;
	}
	if(now->next[str[t]-'a'] == NULL)
	{
		node[p] = tree();
		now->next[str[t]-'a'] = &node[p ++];
	}
	insert(t + 1, now->next[str[t]-'a']);
}

char in[1000000];
int ans, L;
tree * tr;
void dfs(int t, tree * now)
{
	if(t == L)
	{
		ans ++;
		return ;
	}
	int i;
	for(i = St[t]; i <= End[t]; i ++)
	{
		if(now->next[in[i] - 'a'] != NULL)
			dfs(t+1, now->next[in[i] - 'a']);
	}
}
void work(int Test)
{
	int i,j,ll = strlen(in), k = 0;
	for(i = 0; i < ll; i ++)
	{
		if(in[i] != '(')
		{
			St[k] = End[k ++] = i;
		}
		else
		{
			St[k] = i+1;
			while(i < ll)
			{
				if(in[i] == ')')
					break;
				i ++;
			}
			End[k++] = i-1;
		}
	}

	if(k != L)
	{
		printf("Case #%d: 0\n", Test);
		return ;
	}
	ans = 0;
	dfs(0, tr);
	printf("Case #%d: %d\n", Test, ans);
}

int main()
{
    freopen("A-large.in.txt", "r", stdin);
    freopen("A-large.txt", "w", stdout);
	int D,N,i,j,k;
	while(3 == scanf("%d %d %d",&L,&D,&N))
	{
	
		tr = new tree();
		p = 0;
		for(i = 0; i < D; i ++)
		{
			scanf("%s", str);
			len = strlen(str);
			insert(0, tr);
		}
		
		for(i = 1; i <= N; i ++)
		{
			scanf("%s", in);
			work(i);
		}

	}
	return 0;
}
