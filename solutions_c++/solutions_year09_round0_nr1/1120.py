#include <stdio.h>
#include <string.h>
char s[10000][20];
int matr[26][30];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int l,n,m;
	scanf("%d%d%d",&l,&m,&n);
	for (int i=0;i<m;i++)
		scanf("%s",s[i]);
	for (int j=0;j<n;j++)
	{
		int ans=0;
		memset(matr,0,sizeof(matr));
		char token[600];
		scanf("%s",token);
		int pos=0;
		for (int k=0;k<l;k++)
		{
			if (token[pos]!='(')
			{
				matr[k][token[pos]-'a']=1;
				pos++;
			}
			else
			{
				pos++;
				while(token[pos]!=')')
				{
					matr[k][token[pos]-'a']=1;
					pos++;
				}
				pos++;
			}
		}
		for (int i=0;i<m;i++)
		{
			int ind=1;
			for (int k=0;k<l;k++)
				if (!matr[k][s[i][k]-'a'])
					ind=0;
			ans+=ind;
		}
		printf("Case #%d: %d\n",j+1,ans);
	}
	return 0;
}