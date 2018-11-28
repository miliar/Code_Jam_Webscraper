#include<cstdio>
#include<string>
using namespace std;

int n,m;
string se[101];
string q[1001];
char name[101];
int td[2][101];
int main()
{
	int test,i,j,k,T=1;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&test);
	for(;test>0;test--)
	{
		scanf("%d",&n);
		gets(name);
		for(i=0;i<n;i++)
		{
			gets(name);
			se[i]=name;
		}
		scanf("%d",&m);
		gets(name);
		for(i=1;i<=m;i++)
		{
			gets(name);
			q[i]=name;
		}
		for(j=0;j<n;j++)
		{
			td[0][j]=0;
		}
		int f=0;
		for(i=1;i<=m;i++)
		{
			for(j=0;j<n;j++)
				td[1-f][j]=100000;
			for(j=0;j<n;j++)
			{
				if(q[i]==se[j])continue;
				for(k=0;k<n;k++)
				{
					if(j==k)
					{
						if(td[1-f][j]>td[f][k])
							td[1-f][j]=td[f][k];
					}
					else
					{
						if(td[1-f][j]>td[f][k]+1)
							td[1-f][j]=td[f][k]+1;
					}
				}
			}
			f=1-f;
		}
		int ans=1000000;
		for(j=0;j<n;j++)
		{
			if(ans>td[f][j])
				ans=td[f][j];
		}
		printf("Case #%d: %d\n",T++,ans);
	}
}
