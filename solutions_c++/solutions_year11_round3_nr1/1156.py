#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
char s[100][100];
int main()
{
	int t,i,j,r,c,huang,cas=0;
		freopen("A-large.in","r",stdin);
		freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	while (t--)
	{
		cas++;
		scanf("%d%d",&r,&c);
		for (i=0;i<r;i++)
		{
			getchar();
			for (j=0;j<c;j++)
				scanf("%c",&s[i][j]);
		}
		huang=1;
		for (i=0;i<r;i++)
		{
			for (j=0;j<c;j++)
			{
				if (s[i][j]=='#')
				{	
					if (i+1==r) huang=0;
					if (j+1==c) huang=0;
					if (s[i][j]!='#') huang=0;
					if (s[i+1][j]!='#') huang=0;
					if (s[i][j+1]!='#') huang=0;
					if (s[i+1][j+1]!='#') huang=0;
					
					s[i][j]='/';
					s[i][j+1]='\\';
					s[i+1][j]='\\';
					s[i+1][j+1]='/';
					
				}
				if (huang==0) break;
			}
		}
		printf("Case #%d:\n",cas);
		if (huang==1)
			for (i=0;i<r;i++)
			{
				for (j=0;j<c;j++)
					printf("%c",s[i][j]);
				printf("\n");
			}
			else
				printf("Impossible\n");
	}
			return 0;
	}