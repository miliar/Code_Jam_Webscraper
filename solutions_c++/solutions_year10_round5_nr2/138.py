#include <iostream>
#include <algorithm>
using namespace std;


int b[111];
int mem[1111111];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for (int i=1;i<=t;i++)
	{
		cerr<<i<<endl;
		printf("Case #%d: ",i);

		long long l;
		int n;
		scanf("%lld%d",&l,&n);
		for (int j=0;j<n;j++)
			scanf("%d",b+j);
		sort(b,b+n);

		memset(mem,0,sizeof(mem));
		mem[0]=1;
		for (int j=1;j<=1000000;j++)
		{
			for (int h=0;h<n-1;h++)
				if (j>=b[h]&&mem[j-b[h]])
				{
					if (!mem[j]||mem[j]>mem[j-b[h]]+1)
					{
						mem[j]=1+mem[j-b[h]];
					}
				}
		}
		long long res=0;
		for (int j=0;j<=1000000&&l>=j;j++)
		{
			if (mem[j]&&(l-j)%b[n-1]==0)
			{
				long long val=(l-j)/b[n-1];
				val+=mem[j]-1;
				if (!res||res>val)
					res=val;
			}
		}
		if (!res)
			printf("IMPOSSIBLE\n");
		else
			printf("%lld\n",res);
	}
	return 0;
}