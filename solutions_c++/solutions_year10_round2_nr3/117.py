#include <iostream>
#include <algorithm>
using namespace std;
#define MAXN 510

const int base=100003;
long long c[MAXN][MAXN];
long long f[MAXN][MAXN];
int caseN;
int main()
{
	for (int i=0;i<=500;i++)
	{
		c[i][0]=1;
		for (int j=1;j<=i;j++)
			c[i][j]=(c[i-1][j]+c[i-1][j-1])%base;
	}
	for (int i=2;i<=500;i++)
	{
		f[i][1]=1;
		for (int j=2;j<i;j++)
		{
			f[i][j]=0;
			for (int k=1;k<j;k++)
				if (f[j][k] && i-j>=j-k)
				{
					f[i][j]+=f[j][k]*c[i-j-1][j-k-1];
					f[i][j]%=base;
				}
		}
	}
	cin>>caseN;
	for (int caseI=1;caseI<=caseN;caseI++)
	{
		int ans=0;
		int n;
		cin>>n;
		for (int i=1;i<n;i++)
			ans=(ans+f[n][i])%base;
		cout<<"Case #"<<caseI<<": "<<ans<<endl;
	}
	return 0;
}





