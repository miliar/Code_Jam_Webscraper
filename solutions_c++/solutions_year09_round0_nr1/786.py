#include <cstdio>
#include <cstring>

const int dmax=5000;
const int lmax=15;
char word[dmax][lmax+1];
char s[1000];
bool bad[dmax];
bool used[256];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int l,d,n,t,i,j,ans;

	scanf("%d%d%d",&l,&d,&n);
	gets(word[0]);
	for(i=0;i<d;i++) gets(word[i]);

	for(t=1;t<=n;t++)
	{
		gets(s);
		memset(bad,0,sizeof(bad));
		l=0;
		for(i=0;s[i];i++,l++)
		{
			memset(used,0,sizeof(used));
			if (s[i]=='(')
			{
				while(s[++i]!=')') used[s[i]]=true;
			} else used[s[i]]=true;
			for(j=0;j<d;j++)
				if (!used[word[j][l]]) bad[j]=true;
		}

		ans=0;
		for(i=0;i<d;i++)
			if (!bad[i]) ++ans;

		printf("Case #%d: %d\n",t,ans);

	}

	return 0;
}