#include <stdio.h>
#include <string.h>

char name[200][200];
char q[2000][200];

int main()
{
	int i,j,k;
	int t,n,m,C;
	int CASE=1;
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d\n",&n);
		for(i=0;i<n;i++) gets(name[i]);
		scanf("%d\n",&m);
		for(i=0;i<m;i++) gets(q[i]);
		k=0;
		C=0;
		while(k<m)
		{
			int max=-1;
			for(i=0;i<n;i++)
			{
				for(j=k;j<m;j++)
				{
					if(strcmp(name[i],q[j])==0) break;
				}
				if(j>max) max=j;
			}
			k=max;
			C++;
		}
		if(C==0) C=1;
		printf("Case #%d: %d\n",CASE,C-1);
		CASE++;
	}
	return 0;
}