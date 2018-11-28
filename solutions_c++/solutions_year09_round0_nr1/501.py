#include <stdio.h>
#include <string.h>
const int maxn = 6000;
const int maxm = 30;

int i,j,k,l,r,t,ans,th,n,m,r1;
int tree[maxn*maxm][maxm],ls[maxn*maxm*maxm][2];
char str[maxn];

void newnode()
{
	int i;
	th++;
	for (i=0;i<26;i++) tree[th][i]=0;
}
void insert(int p,int deep)
{
	if (deep>=m) return ;
	int i=str[deep]-'a';
	if (tree[p][i]==0) 
	{
		newnode();
		tree[p][i]=th;
	}
	insert(tree[p][i],deep+1);
}
void work(int l,int r,int l1,int r1,int & newr)
{
	int i,j,p,d,ch;
	newr=r;
	for (i=l;i<=r;i++)
	{
		p=ls[i][0];
		d=ls[i][1];
		for (j=l1;j<=r1;j++)
		{
			ch=str[j]-'a';
			if (tree[p][ch]!=0)
			{
				newr++;
				ls[newr][0]=tree[p][ch];
				ls[newr][1]=d+1;
			}
		}
	}
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d%d%d",&m,&n,&t);
	th=0;
	newnode();
	for (i=1;i<=n;i++)
	{
		gets(str);
		while (str[0]==0) gets(str);
		insert(1,0);
	}
	for (i=1;i<=t;i++)
	{
		l=1; r=1; ls[1][0]=1; ls[1][1]=0;
		gets(str);
		while (str[0]==0) gets(str);
		j=0; n=strlen(str);
		while (j<n)
		{
			if (str[j]=='(')
			{
				k=j+1;
				while (str[k]!=')') k++;
				j++;
				k--;
			} else
			k=j;
			work(l,r,j,k,r1);
			l=r+1;
			r=r1;
			j=k+1;
			if (str[j]==')') j++;
		}
		ans=0;
		for (j=1;j<=r;j++)
			if (ls[j][1]==m) ans++;
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}