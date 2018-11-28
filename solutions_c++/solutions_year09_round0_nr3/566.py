#include<cstdio>
#include<cstring>

int t,i,j,k,n;
char a[1000];
char b[]=" welcome to code jam";
int count[20];
#define MAX 19
#define MOD 10000

int main()
{
	freopen("c_input.in","r",stdin);
	freopen("c_output.out","w",stdout);

	scanf("%d ",&t);
	while(t--)
	{
		++k;
		memset(count,0,sizeof(count));
		count[0]=1;
		fgets(a,999,stdin);
		n = strlen(a);
		for(i=0;i<n;++i)
			for(j=MAX;j>0;--j)
				if(a[i]==b[j])
				{
					count[j] += count[j-1];
					if(count[j]>=MOD) count[j] -= MOD;
				}
		printf("Case #%d: %04d\n",k,count[MAX]);
	}

	fclose(stdout);
	return 0;
}
