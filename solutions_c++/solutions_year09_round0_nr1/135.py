#include<iostream>
using namespace std;
int L,d,n,i,j,len,ans;
char s[500010];
int a[5010][20];
int b[20];
int ci;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d %d %d",&L,&d,&n);
	for (i=0;i<d;i++)
	{
		scanf("%s",&s);
		for (j=0;j<L;j++) a[i][j]=1<<(s[j]-'a');
	}
	for (ci=1;ci<=n;ci++)
	{
		scanf("%s",&s);
		len=strlen(s);
		i=0;
		for (j=0;j<len;j++)
		if (s[j]=='(')
		{
			b[i]=0;
			j++;
			while (isalpha(s[j]))
			{
				b[i]=b[i] | (1<<(s[j]-'a'));
				j++;
			}
			i++;
		}
		else 
		{
			b[i]=1<<(s[j]-'a');
			i++;
		}
		ans=0;
		for (i=0;i<d;i++)
		{
			for (j=0;j<L;j++)
			if (!(b[j] & a[i][j])) break;
			if (j==L) 
			{
//				cout<<i<<endl;
				ans++;
			}
		}
		printf("Case #%d: %d\n",ci,ans);
	}
	return 0;
}
