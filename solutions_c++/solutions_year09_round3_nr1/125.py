#include <stdio.h>
#include <string.h>
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int cases;
	scanf("%d\n",&cases);
	for (int k=1;k<=cases;k++)
	{
		printf("Case #%d: ",k);
		char s[100];
		int hash[256];
		memset(hash,-1,sizeof(hash));
		scanf("%s\n",s);
		hash[s[0]]=1;
		int count=1;
		for (int i=1;i<strlen(s);i++)
			if (hash[s[i]]<0)
			{
				if (count==1)
					hash[s[i]]=0;
				else hash[s[i]]=count;
				count++;
			}
		if (count==1) count++;
		long long ans=0;
		for (int i=0;i<strlen(s);i++)
			ans=ans*count+hash[s[i]];
		printf("%lld\n",ans);
	}
	return 0;
}