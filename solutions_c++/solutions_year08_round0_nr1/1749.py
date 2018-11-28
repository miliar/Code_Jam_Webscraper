#include <stdio.h>
#include <string.h>

#define LEN 110
#define MAX 110

int main()
{
	int n;
	scanf("%d ",&n);

	for(int i=1;i<=n;i++)
	{
		int s;
		char se[MAX][LEN];
		scanf("%d ",&s);

		for(int j=0;j<s;j++)
			gets(se[j]);

		int q, qs[MAX];
		char qu[MAX][LEN]={0};
		scanf("%d ",&q);
	

		for(int j=0;j<q;j++)
		{
			gets(qu[j]);
			qs[j]=-1;
			for(int k=0;k<s;k++)
				if(strcmp(qu[j],se[k])==0)
				{
					qs[j]=k;
					break;
				}
				
		}
		
		int j=0,c=0,n=0;
		bool x[MAX]={0};
		while(j<q)
		{
			if(x[qs[j]]==false)
			{
				x[qs[j]]=true;
				c++;

				if(c==s)
				{
					for(int k=0;k<s;k++) x[k]=false;
					n++;
					c=1;
					x[qs[j]]=true;
				
				}
			}

			j++;
		}

		printf("Case #%d: %d\n",i,n);

	}


	return 0;
}
