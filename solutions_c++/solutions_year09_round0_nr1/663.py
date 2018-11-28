#include <cstdio>
#include <cstring>

struct node
{
	int next[26], cnt;
}tree[100003];
int L, D, N, tot, cnt, ans;
char key[900], ch[30][30];

void add_node()
{
	for(int i = 0; i < 26; i++)
		tree[tot].next[i] = -1;
	tree[tot++].cnt = 0;
}

void insert()
{
	int i = 0, t = 0;
	while(key[i])
	{
		int idx = key[i] - 'a';
		if(tree[t].next[idx] == -1)
		{
			tree[t].next[idx] = tot;
			add_node();
		}
		t = tree[t].next[idx];
		i++;
	}
	tree[t].cnt = 1;
}

void init()
{
	tot = 0;
	add_node();
	for(int i = 0; i < D; i++)
	{
		scanf("%s", key);
		insert();
	}
}

void dfs(int t, int k)
{
	for(int i = 0; ch[t][i] != '\0'; i++)
	{
		int idx = ch[t][i] - 'a';
		if(tree[k].next[idx] != -1)
		{
			if(tree[tree[k].next[idx]].cnt)
			{
				ans++;
				continue;
			}
			dfs(t+1, tree[k].next[idx]);
		}
	}
}

void solve()
{
	int i, j, k, len;
	for(i = 0; i < N; i++)
	{
		scanf("%s", key);
		memset(ch, '\0', sizeof(ch));
		cnt = j = 0;
		len = strlen(key);
		while(j < len)
		{
			if(key[j] == '(')
			{
				j++;
				k = 0;
				while(key[j] != ')')
					ch[cnt][k++] = key[j++];
				cnt++;
			}
			else
				ch[cnt++][0] = key[j];
			j++;
		}
		ans = 0;
		dfs(0, 0);
		printf("Case #%d: %d\n", i+1, ans);
	}
}

int main()
{
//	freopen("A-large.in", "r", stdin);
//	freopen("A-large.out", "w", stdout);
	while(scanf("%d %d %d", &L, &D, &N) != EOF)
	{
		init();
		solve();
	}
	return 0;
}
