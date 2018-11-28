#include <stdio.h>
#include <string.h>

bool c[20][255];

char word[5010][20];
char str[300];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int l ,d, n, i, j, k, ans;
	scanf("%d%d%d", &l, &d, &n);
	for (i=0; i<d; i++)
	  scanf("%s", word[i]);
	for (i=1; i<=n; i++)
	{
		memset(c, false, sizeof(c));
		scanf("%s", str);
		k=0;
		j=0;
		while (str[j]!='\0')
		{
			if (str[j]=='(')
			{
				j++;
				while (str[j]!=')')
				{
				  c[k][str[j]]=true;
				  j++;
				}
				j++;
			}
			else c[k][str[j++]]=true;
			k++;
		}
		ans=0;
		for (j=0; j<d; j++)
		{
			for (k=0; k<l; k++)
			 if (!c[k][word[j][k]]) break;
			if (k==l) ans++; 
		}
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}
