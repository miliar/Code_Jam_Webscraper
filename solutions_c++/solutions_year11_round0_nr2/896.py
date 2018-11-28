#include<stdio.h>
#include<string.h>
int a[26][26];
int c[26][26];
char s[10000];
int b[1000];
int d[26];
int main()
{
	int t,tt,m,i,j;
	scanf("%d",&t);
	for (tt=1;tt<=t;tt++)
	{
		memset(a,-1,sizeof(a));
		scanf("%d",&m);
		while (m>0)
		{
			m--;
			scanf("%s",s);
			a[s[0]-'A'][s[1]-'A']=a[s[1]-'A'][s[0]-'A']=s[2]-'A';
		}
		memset(c,0,sizeof(c));
		scanf("%d",&m);
		while (m>0)
		{
			m--;
			scanf("%s",s);
			c[s[0]-'A'][s[1]-'A']=c[s[1]-'A'][s[0]-'A']=1;
		}
		scanf("%d %s",&m,s);
		m=0;
		memset(d,0,sizeof(d));
		for (i=0;s[i]!='\0';i++)
		{
			b[m]=s[i]-'A';
			d[b[m]]++;
			m++;
			if (m>=2)
			{
				if (a[b[m-1]][b[m-2]]!=-1)
				{
					d[b[m-1]]--;
					d[b[m-2]]--;
					b[m-2]=a[b[m-1]][b[m-2]];
					m--;
					d[b[m-1]]++;
				}
			}
			for (j=0;j<26;j++)
			{
				if (d[j]==0)
					continue;
				if (c[b[m-1]][j]==0)
					continue;
				m=0;
				memset(d,0,sizeof(d));
				break;
			}
		}
		printf("Case #%d: [",tt);
		for (i=0;i<m;i++)
		{
			if (i!=0)
				printf(", ");
			printf("%c",b[i]+'A');
		}
		printf("]\n");
	}
	return 0;
}