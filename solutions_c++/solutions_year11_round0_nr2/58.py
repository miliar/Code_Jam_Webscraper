#include<stdio.h>
#include<memory.h>
int C,D,N;
char c[36][5],d[28][5],s[200],st[200];
int alp[30];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test,i,j,T=1;
	scanf("%d",&test);
	for(;test>0;test--)
	{
		scanf("%d",&C);
		for(i=0;i<C;i++)
			scanf("%s",c[i]);
		scanf("%d",&D);
		for(i=0;i<D;i++)
			scanf("%s",d[i]);
		scanf("%d",&N);
		scanf("%s",s);
		memset(alp,0,sizeof(alp));
		int m=0;
		for(i=0;i<N;i++)
		{
			alp[s[i]-'A']++;
			st[m++]=s[i];
			if(m>=2)
			{
				for(j=0;j<C;j++)
				{
					if((c[j][0]==st[m-1] && c[j][1]==st[m-2]) || (c[j][1]==st[m-1] && c[j][0]==st[m-2]))
					{
						alp[c[j][0]-'A']--;
						alp[c[j][1]-'A']--;
						alp[c[j][2]-'A']++;
						m--;
						st[m-1]=c[j][2];
						break;
					}
				}
				if(j==C)
				{
					for(j=0;j<D;j++)
					{
						if(d[j][0]==st[m-1] && alp[d[j][1]-'A']>0)
						{
							m=0;
							memset(alp,0,sizeof(alp));
							break;
						}
						else if(d[j][1]==st[m-1] && alp[d[j][0]-'A']>0)
						{
							m=0;
							memset(alp,0,sizeof(alp));
							break;
						}
					}
				}
			}
		}
		printf("Case #%d: [",T++);
		if(m>0)
			printf("%c",st[0]);
		for(i=1;i<m;i++)
			printf(", %c",st[i]);
		printf("]\n");
	}
	return 0;
}
