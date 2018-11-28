#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <deque>
#include <cmath>
#include <map>

using namespace std;
int n;
long long DP[501][501];
long long C[501][501];
const long long ttt=100003;
int main()
{
	C[1][1]=1;
	for(int i=0;i<=500;i++)
		C[i][0]=1;
	for(int i=2;i<=500;i++)
		for(int j=1;j<=i;j++)
			C[i][j]=(C[i-1][j]+C[i-1][j-1])%ttt;
	for(int i=2;i<=500;i++)
		DP[i][1]=1;
	for(int i=3;i<=500;i++)
		for(int j=i-1;j>=2;j--)
		{
			for(int k=1;k<j;k++)if(j-k<=i-j)
			{
				DP[i][j]+=(C[i-j-1][j-k-1]*DP[j][k])%ttt;
				DP[i][j]%=ttt;
			}
		}
	freopen("C-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int TT;
	cin>>TT;
	for(int t=1;t<=TT;t++)
	{
		cin>>n;
		long long ans=0;
		for(int i=0;i<n;i++)
		{
			ans+=DP[n][i];
			ans%=ttt;
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}