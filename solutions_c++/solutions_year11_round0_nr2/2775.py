#include<cstdio>
#include<cstring>
int main()
{
	int t,n,c,d,i,j,k,st[26][26],dp[26][26],l,ca=0;
	char ch,str[200],s[200];
	scanf("%d%c",&t,&ch);
	while(t--)
	{
		ca++;
		for (i=0;i<26;i++)
			for (j=0;j<26;j++)
				st[i][j] = 0;
		scanf("%d",&c);
		for (i=0;i<c;i++)
		{
			scanf("%s",str);
			j = str[0]-'A';
			k = str[1]-'A';
			st[j][k] = 1;
			d = str[2]-'A';
			dp[j][k] = d;
			dp[k][j] = d;
			st[k][j] = 1;
		}
		scanf("%d",&d);
		for (i=0;i<d;i++)
		{
			scanf("%s",str);
			j = str[0]-'A';
			k = str[1]-'A';
			if (st[j][k]==1)
			{
				st[j][k] = 2;
				st[k][j] = 2;
			}
			else
			{
				st[j][k] = -1;
				st[k][j] = -1;
			}
		}
		l = 0;
		scanf("%d",&n);
		scanf("%s",str);
		for (i=0;i<n;i++)
		{
			if (l >= 2)
			{
				if (st[s[l-1]][s[l-2]] > 0)
				{
					s[l-2] = dp[s[l-1]][s[l-2]];
					l--;
				}
				for (j=0;j<l-1;j++)
				{
					if (st[s[j]][s[l-1]]==-1 || st[s[j]][s[l-1]]==2)
					{
						l = 0;
						break;
					}
				}
			}
			s[l] = str[i]-'A';
			l++;
	/*		printf("Last char checked %c\n",str[i]);
			for (j=0;j<l;j++)
				printf("%c",s[j]+'A');
			printf("\n");*/
		}
		if (l >= 2)
		{
			if (st[s[l-1]][s[l-2]] > 0)
			{
				s[l-2] = dp[s[l-1]][s[l-2]];
				l--;
			}
			for (j=0;j<l-1;j++)
			{
				if (st[s[j]][s[l-1]]==-1 || st[s[j]][s[l-1]]==2)
				{
					l = 0;
					break;
				}
			}
		}
		printf("Case #%d: ",ca);
		if (l==0)
			printf("[]\n");
		else if (l==1)
			printf("[%c]\n",s[0]+'A');
		else
		{
			printf("[");
			for (i=0;i<l-1;i++)
				printf("%c, ",s[i]+'A');
			printf("%c]\n",s[l-1]+'A');
		}
	}
	return 0;
}
