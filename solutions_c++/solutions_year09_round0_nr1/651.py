#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>

using namespace std;

typedef long long ll;

const int TSIZE=20*5000+5;
const int CN=26;

//Trie

struct Trie
{
	int c[CN];
	bool flag;
	void Init()
	{
		memset(c,0,sizeof(c));
		flag=false;
	}
};

Trie trie[TSIZE];
int len;

void Pro()
{
	trie[0].Init();
	len=1;
}

void Insert(char *str,bool flag)
{
	int r=0;
	int i,ch;
	for (i=0;str[i];i++)
	{
		ch=str[i]-'a';
		if (!trie[r].c[ch])
		{
			trie[len].Init();
			trie[r].c[ch]=len;
			len++;
		}
		r=trie[r].c[ch];
	}
	trie[r].flag=true;
}

int L,D,N;
char buffer[10000];
bool has[20][26];
int g_ans=0;

void DFS(int dep,int state)
{
	if (dep==L)
	{
		if (trie[state].flag)
			g_ans++;
		return;
	}

	int i;
	for (i=0;i<26;i++)
		if (has[dep][i] && trie[state].c[i])			
			DFS(dep+1,trie[state].c[i]);
}

int Solve(char *str)
{
	int sz=strlen(str);
	memset(has,0,sizeof(has));
	int i,j,cur;
	cur=0;
	for (i=0;i<sz;i++)
	{
		if(str[i]=='(')
		{
			for (j=i+1;j<sz && str[j]!=')';j++);
			for (i++;i<j;i++)
				has[cur][str[i]-'a']=true;
			cur++;
		}
		else
		{
			has[cur++][str[i]-'a']=true;
		}
	}

	g_ans=0;
	DFS(0,0);
	return g_ans;
}

int main()
{
	int i;

	freopen("in","r",stdin);
	freopen("out","w",stdout);

	while (scanf("%d%d%d",&L,&D,&N)!=EOF)
	{
		Pro();
		for (i=0;i<D;i++)
		{
			scanf("%s",buffer);
			Insert(buffer,true);
		}
		for (i=1;i<=N;i++)
		{
			scanf("%s",buffer);
			printf("Case #%d: %d\n",i,Solve(buffer));
		}
	}

	return 0;
}