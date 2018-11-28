#include<iostream>
using namespace std;

struct node
{
	node *ptr[26];
	node()
	{
		int i;
		for(i=0;i<26;i++)
			ptr[i]=NULL;
	}
}root;

void Insert(char *s)
{
	node *p=&root;
	int i,l=strlen(s),t;
	for(i=0;i<l;i++)
	{
		t=s[i]-'a';
		if(p->ptr[t]==NULL)
			p->ptr[t]=new node();
		p=p->ptr[t];
	}
}

char c[20],ch[500],v[20][100];
int l,ans,num[20];

void dfs(node *p,int i)
{
	if(p==NULL)
		return ;
	if(i==l)
	{
		ans++;
		return ;
	}
	int j;
	for(j=0;j<num[i];j++)
	{
		dfs(p->ptr[v[i][j]-'a'],i+1);
	}
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	int d,n,T=0,i,j;
	scanf("%d%d%d",&l,&d,&n);
	while(d--)
	{
		scanf("%s",c);
		Insert(c);
	}
	while(n--)
	{
		scanf("%s",ch);
		i=0;
		j=0;
		memset(num,0,sizeof(num));
		while(ch[i])
		{
			if(ch[i]=='(')
			{
				i++;
				while(ch[i]!=')')
				{
					v[j][num[j]++]=ch[i];
					i++;
				}
				i++;
				j++;
			}
			else
			{
				v[j][num[j]++]=ch[i];
				i++;
				j++;
			}
		}
		ans=0;
		dfs(&root,0);
		printf("Case #%d: %d\n",++T,ans);

	}
	return 0;
}