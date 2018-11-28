#include<cstdio>

const int maxn=100000+10;
struct Ttrie
{
	int w[26];
	int cnt;	
} t[maxn];
int L,D,N,num;
char st[maxn];
bool word[maxn][26];
int res;

void dfs(int d,int dep)
{
	if (!t[d].cnt) return;
	if (dep==L) {res+=t[d].cnt;return;}
	for (int i=0;i<26;i++)
	if (t[d].w[i] && word[dep][i])
	{
		t[t[d].w[i]].cnt+=t[d].cnt;
		dfs(t[d].w[i],dep+1);
	}
}

int main()
{
	freopen("input.txt","r",stdin);
	
	scanf("%d%d%d",&L,&D,&N);
	for (int i=0;i<D;i++)
	{
		scanf("%s",st);
		for (int j=0,k=0;st[j];j++)
		if (!t[k].w[st[j]-'a'])
			k=t[k].w[st[j]-'a']=++num;
		else k=t[k].w[st[j]-'a'];
	}
	
	for (int i=0;i<N;i++)
	{
		scanf("%s",st);
		for (int j=0,k=0;j<L;j++)
		{
			for (int tmp=0;tmp<26;tmp++) word[j][tmp]=0;
			if (st[k]=='(')
			{
				for (++k;st[k]>='a' && st[k]<='z';k++) word[j][st[k]-'a']=true;
				k++;
			} else word[j][st[k++]-'a']=true;
		}
		for (int j=0;j<=num;j++) t[j].cnt=0;
		t[0].cnt=1;
		res=0;
		dfs(0,0);
		printf("Case #%d: %d\n",i+1,res);
	}
}