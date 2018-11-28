#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 5010
#define LEN 2000
#define LETTER 30

int l,d,n;
char word[MAXN][LEN];
char str[LEN];
int table[LETTER][LETTER*10];

int str2table()
{
	int i,j;
	
	memset(table,0,sizeof(table));
	
	j=0;
	for(i=0;i<l;i++)
	{
		if (str[j]!='(')
		{
			table[i][str[j]]=1;
			j++;
		}
		else
		{
			j++;
			do
			{
				//printf("i j str %d %d %s\n",i,j,str);
				table[i][str[j]]=1;
				j++;
			}
			while(str[j]!=')');
			j++;
		}
	}	
	
	return 0;
}

int count()
{
	int i,j;
	int total;
	int flag;
	
	total=0;
	
	for(i=1;i<=d;i++)
	{
		flag=1;
		for(j=0;j<l;j++)
		{
			if (table[j][word[i][j]]==0)
			{
				flag=0;
				break;
			}
		}
		total+=flag;
	}
	
	return total;
}

int solve(int i)
{
	int ans;
	
	str2table();
	
	ans=count();
	
	printf("Case #%d: %d\n",i,ans);
	
	return 0;
}

int main()
{
	int i,j,k;
	char ch;
	
	freopen("a.in","r",stdin);	
	freopen("a.out","w",stdout);
	
	scanf("%d %d %d",&l,&d,&n);
	
	for(i=1;i<=d;i++)
	{
		/*
		for(j=0;j<l;j++)
		{
			scanf("%c",&ch);
			word[i][j]=ch;
		}
		word[i][l]='\0';
		*/
		
		scanf("%s",word[i]);
		//printf("word %i:%s\n",i,word[i]);
		
	}
	
	for(i=1;i<=n;i++)
	{
		scanf("%s",str);
		//printf("%s\n",str);
		/*
		k=0;
		for(j=0;j<l;j++)
		{
			scanf("%c",&ch);
			if (ch!='(')
			{
				str[k]=ch;
				k++;
			}
			else
			{
				do
				{
					scanf("%c",&ch);
					str[k]=ch;
					k++;
				}
				while(ch==')');
			}
			k++;
			str[k]='\0';
		}
		*/
		solve(i);
	}
	
	return 0;
}