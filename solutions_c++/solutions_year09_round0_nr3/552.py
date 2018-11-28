#include<stdio.h>
#include<string.h>
int ans,a[20][510],i,j,k,z,ls,lt,n;
char s[510];
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("Clarge.txt","w",stdout);
	char *t="welcome to code jam#";
	lt=20;
	scanf("%d\n",&n);
	for (z=1;z<=n;z++)
	{
		gets(s);
		ls=strlen(s);
		s[ls++]='#';
		memset(a,0,sizeof a);
		for (j=0;j<ls;j++)
			if (s[j]==t[0]) a[0][j]=1;
		for (i=1;i<lt;i++)
			for (j=0;j<ls;j++) 
				if (t[i]==s[j])
				{
					for (k=0;k<j;k++) 
						if (s[k]==t[i-1]) 
						{
							a[i][j]+=a[i-1][k];
							if (a[i][j]>9999) a[i][j]%=10000;
						}
				}
		printf("Case #%d: %04d\n",z,a[lt-1][ls-1]);
	}
}
