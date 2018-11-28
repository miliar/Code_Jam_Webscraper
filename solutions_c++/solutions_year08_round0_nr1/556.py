#include<stdio.h>
#include<string.h>
int main()
{
	int n;
	int i,j;
	int num;
	int ns,nq;
	int fs[105];
	char s[105][105],q[1005][105];
	int swi;
	int cases=0;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	while(1==scanf("%d",&n))
	{
		
		while(n--)
		{
			scanf("%d",&ns);
			getchar();
			for(i=0;i<ns;i++)
				gets(s[i]);
			scanf("%d",&nq);
			getchar();
			for(i=0;i<nq;i++)
				gets(q[i]);

			memset(fs,0,sizeof(fs));
			num=0;
			swi=0;
			for(i=0;i<nq;i++)
			{
				for(j=0;j<ns;j++)
				{
					if(strcmp(s[j],q[i])==0)
					{
						if(fs[j]==0) 
						{
							fs[j]=-1;
							num++;
							if(num==ns)
							{
								swi++;
								num=0;
								memset(fs,0,sizeof(fs));
								fs[j]=-1;
								num++;
							}
						}
					}
				}
			}

			printf("Case #%d: %d\n",++cases,swi);

		}
	}
	return 0;
}