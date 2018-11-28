#include<cstdio>
char f[55][55];
int t,mt,n,m,find,i,j;
int main()
{
	freopen("Al.in","r",stdin);
	freopen("Al.out","w",stdout);
	scanf("%d",&t);
	for(mt=1;mt<=t;mt++)
	{
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)scanf("%s",f[i]);
		find=0;
		for(i=0;i<n;i++)
		for(j=0;j<m;j++)
		{
			if (f[i][j]=='#')
			{
				if (i==n-1||j==m-1) 
				{
					find=1;
					goto sa;
				}
				if (f[i+1][j]!='#'||f[i][j+1]!='#'||f[i+1][j+1]!='#')
				{
					find=1;
					goto sa;
				}
				f[i][j]='/';
				f[i][j+1]='\\';
				f[i+1][j]='\\';
				f[i+1][j+1]='/';
			}
		}
		sa:printf("Case #%d:\n",mt);
		if(find) printf("Impossible\n");
		else
		{
			for(i=0;i<n;i++) printf("%s\n",f[i]);
		}
	}
}
