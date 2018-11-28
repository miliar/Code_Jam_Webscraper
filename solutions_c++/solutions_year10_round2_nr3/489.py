#include<iostream>
#include<map>
#include<fstream>
using namespace std;

map<pair<int,int> , int> sub;
int dp[1000][1000];
int v[501][501];
int POW(int hd,int nd)
{
	if( hd<nd)
		return 0;
	return v[hd][nd];
}

int main()
{
	int t;
	int n;
	int f[501];
	cin >> t;
	f[1] = 1;
	f[2] = 1;
	v[0][0] = v[1][0] = v[1][1] = 1;
	for(int i=2;i<501;i++)
	{
		v[i][0] = 1;
		for(int j=1;j<i;j++)
		{
			v[i][j] = v[i-1][j]+v[i-1][j-1];
			v[i][j] %= 100003;
		}
		v[i][i] = 1;
	}
	ofstream fout("ans");
	for(int m=0;m<t;m++)
	{
		for(int i=0;i<1000;i++)
			for(int j=0;j<1000;j++)
				dp[i][j] = 0;
		cin >> n;
		for(int i=2;i<=n;i++)
			dp[i][1] = 1;
		for(int i=3;i<=n;i++)
		{
			for(int k=i-1;k>1;k--)
			{
				for(int j=k-1;j>=1;j--)
				{
					int md = i-k-1;
					dp[i][k] +=dp[k][j]*POW(md,k-j-1);
					dp[i][k] %= 100003;
				}
			}
		}
		int sum = 0;
		for(int i=1;i<n;i++)
		{
			sum += dp[n][i];
			sum %= 100003;
		}
		fout << "Case #" <<m+1 << ": ";
		fout << sum << endl;
	}
}
