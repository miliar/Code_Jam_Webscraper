#include<iostream>
#include<vector>

using namespace std;

struct node
{
	int count;
	node* next[26];
	node()
	{
		count = 0;
		for (int i = 0; i < 26; i++)
			next[i] = 0;
	}
};

node* root;

void insert(char* str)
{
	int i = 0;
	node* p = root;
	while (str[i] != '\0')
	{
		int pos = str[i] - 'a';
		if (p->next[pos] == 0)
		{
			p->next[pos] = new node;
		}

		p = p->next[pos];
		i++;
	}
	p->count++;
}

bool search(char* str)
{
	int i = 0;
	node* p = root;
	while (str[i] != '\0')
	{
		int pos = str[i] - 'a';
		if (p->next[pos] == 0)
			return false;
		else
			p = p->next[pos];
		i++;
	}
	if (p->count > 0)
		return true;
	else
		return false;
}

void remove(node*& p)
{
	for (int i = 0; i < 26; i++)
		if (p->next[i])
			remove(p->next[i]);
	delete p;
}

char buf[100000];

char buf2[20];
int ans = 0;

int L,D,N;

void dfs(node* p,int u,int pos)
{
	if (u >= L)
	{
		buf2[u] = '\0';

		if (p->count > 0)
			ans++;
		return;
	}


	if (buf[pos] == '(')
	{
		int mybeg,mylast;
		mybeg = pos + 1;
		while (buf[pos] != ')')
		{
			pos++;
		}
		mylast = pos - 1;

		for (int i = mybeg; i <= mylast; i++)
		{
			buf2[u] = buf[i];

			//检测是否有该节点的
			if (p->next[buf2[u] - 'a'] == 0)
				continue;

			dfs(p->next[buf2[u] - 'a'], u + 1,pos + 1);
		}
	}
	else
	{
		buf2[u] = buf[pos];
		//检测是否有该节点的
		if (p->next[buf2[u] - 'a'] == 0)
			return;

		dfs(p->next[buf2[u] - 'a'],u + 1, pos + 1);
	}
}



int main()
{
	freopen("A-large.in","r",stdin);
	freopen("1.txt","w",stdout);
	root = new node;

	scanf("%d%d%d",&L,&D,&N);
	for (int i = 0; i < D; i++)
	{
		scanf("%s",buf);
		insert(buf);
	}

	for (int i = 0; i < N; i++)
	{	
		ans = 0;
		scanf("%s",buf);
		//printf("%s\n",buf);
		dfs(root, 0, 0);
		printf("Case #%d: %d\n",i + 1, ans);
	}
	remove(root);

	return 0;
}