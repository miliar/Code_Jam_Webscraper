#include<stdio.h>
#include<algorithm>
using namespace std;

int f[201][201],data[201];
int balance(int x)
{
	return x/3+(x%3!=0);
}
int imba(int x)
{
	return x/3+(x%3!=2?1:2);
}
int main()
{
	int t,bk,n,s,p,i,j;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for(bk=1;bk<=t;++bk)
	{
		scanf("%d%d%d",&n,&s,&p);
		for(i=1;i<=n;++i)
			scanf("%d",&data[i]);
		
		for(i=1;i<=s;++i)
			f[0][i]=-1<<20;
		f[0][0]=0;
		for(i=1;i<=n;++i)
			for(j=0;j<=s;++j)
			{
				f[i][j]=f[i-1][j]+(balance(data[i])>=p);
				if(j&&data[i]>=2&&data[i]<=28)
					f[i][j]=max(f[i][j],f[i-1][j-1]+(imba(data[i])>=p));
			}
		printf("Case #%d: %d\n",bk,f[n][s]);
	}
	return 0;
}
