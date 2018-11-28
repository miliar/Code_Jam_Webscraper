#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
#define MAXN 11

int n;
long long f[1<<MAXN][MAXN];
int price[1<<MAXN];
int leaf[1<<MAXN];

int caseN;
int main()
{
	scanf("%d",&caseN);
	for (int caseI=1;caseI<=caseN;caseI++)
	{
		scanf("%d",&n);
		memset(leaf,127,sizeof(leaf));
		for (int i=(1<<n)-1;i>=0;i--)
		{
			int k=i/2+(1<<(n-1))-1;
			int a;
			scanf("%d",&a);
			leaf[k]=min(a,leaf[k]);
		}
		for (int i=(1<<n)-2;i>=0;i--)
				scanf("%d",&price[i]);
		for (int i=(1<<n)-2;i>=0;i--)
			for (int j=0;j<=n;j++)
			{
				if (i>=(1<<(n-1))-1)
				{
					if (j>leaf[i])
						f[i][j]=2000000000;
					else if (j==leaf[i])
						f[i][j]=price[i];
					else
						f[i][j]=0;
				}
				else
				{
					f[i][j]=f[i*2+1][j]+f[i*2+2][j]+price[i];
					if (j<n)
						f[i][j]=min(f[i][j],f[i*2+1][j+1]+f[i*2+2][j+1]);
				}
//				cout<<i<<' '<<j<<' '<<price[i]<<' '<<f[i][j]<<endl;
			}
		printf("Case #%d: %d\n",caseI,(int)f[0][0]);
	}
	return 0;
}


