#include <stdio.h>
#include <string.h>

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T,k,i,n;
	__int64 ans;
	char s[1000];
	int u[1000];
	scanf("%d",&T);
	int j=1;
	while(T--)
	{
		scanf("%s",&s);
		printf("Case #%d: ",j);
		j++;
		memset(u,-1,sizeof(u));
		u[s[0]]=1;
		n=strlen(s);
		k=0;
		for(i=1;i<n;i++)
		{
			if(u[s[i]]==-1)
				u[s[i]]=k++;
			if(k==1)
				k++;
		}
		if(k<2)
			k=2;
		ans=0;
		for(i=0;i<n;i++)
			ans=ans*k+u[s[i]];
		printf("%I64d\n",ans);
	}
	return 0;
}