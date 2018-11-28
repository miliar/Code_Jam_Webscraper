#include<stdio.h>
#include<string.h>

char p[5010][100];
char str[5000];
bool pt[100][100];

bool match(char str[],int j)
{
	
	int l=strlen(p[j]);
	for (int i=0;i<l;i++)
	{
		if (!pt[i][p[j][i]-'a']) return 0;
	}
	return 1;
}

int main()
{
	freopen("R:\\in.txt","r",stdin);
	freopen("R:\\out.txt","w",stdout);
	int l,d,n;
	scanf("%d %d %d",&l,&d,&n);
	memset(p,0,sizeof(p));
	for (int i=0;i<d;i++)
		scanf("%s",p[i]);
	for (int i=0;i<n;i++)
	{
		scanf("%s",&str);
		int ct=0;
		memset(pt,0,sizeof(pt));
		int l=strlen(str);
		int pos = 0;
		int st = 0;
		for (int i=0;i<l;i++)
		{
			if (str[i]=='(')
				st = 1;
			else if (str[i]==')')
			{
				pos++;
				st = 0;
			}
			else
			{
				pt[pos][str[i]-'a'] = 1;
				if (!st) pos++;
			}
		}
		for (int j=0;j<d;j++)
		{
			if (match(str,j)) ct++;
		}
		printf("Case #%d: %d\n",i+1,ct);
	}
	return 0;
}
