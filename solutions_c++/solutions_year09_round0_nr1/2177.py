#include <stdio.h>
#include <string.h>

char words[5005][20];

int main(void)
{
	int l,d,n;
	int i,j,k,len;
	int ans;
	int f[20][27];
	char s[1000];
	
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);

	while(scanf("%d%d%d",&l,&d,&n)==3)
	{
		for(i=0; i<d; i++)
			scanf("%s", words[i]);
		for(i=1; i<=n; i++)
		{
			scanf("%s",s);
			len = strlen(s);
			for(j=0; j<l; j++)
			{
				for(k=0; k<26; k++)
					f[j][k] = 0;
			}
			k = 0;
			for(j=0; j<l && k<len; j++)
			{
				if(s[k]=='(')
				{
					k++;
					while(s[k]!=')')
					{
						f[j][s[k]-'a']=1;
						k++;
					}
					k++;
				}
				else
				{
					f[j][s[k]-'a']=1;
					k++;
				}
			}
			ans = 0;
			for(j=0; j<d; j++)
			{
				for(k=0; k<l; k++)
				{
					if(f[k][words[j][k]-'a'] != 1)
					{
						break;
					}
				}
				if(k==l)
					ans++;
			}
			printf("Case #%d: %d\n",i,ans);
		}
	}
	return 0;
}