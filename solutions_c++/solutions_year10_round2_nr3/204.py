#include<iostream>
#include<string>
#include<vector>
#include<set>
using namespace std;

int comb[501][501];
int main()
{

	freopen("C:\\Documents and Settings\\Administrator\\桌面\\gcj\\C-large.in","r",stdin);
	freopen("C:\\Documents and Settings\\Administrator\\桌面\\gcj\\C-large.out","w",stdout);
	for(int i=0;i<=500;i++)
	{
		comb[i][0]=1;
		for(int j=1;j<=i;j++)
		{
			comb[i][j]=comb[i-1][j-1];
			if(j!=i)
			{
				comb[i][j]+=comb[i-1][j];
				comb[i][j]%=100003;
			}
		}
	}
	int n=500;


	vector<vector<int> > dp(n+1,vector<int>(n,0));//dp[i][j] i是第j名

	for(int i=2;i<=n;i++)
	{
		for(int j=1;j<i;j++)
		{
			if(j==1)
			{
				dp[i][j]=1;
			}
			else
			{
				//i是第j名
				//j,j+1,...,i-1,i
				//j是第k名
				//中间有j-k-1个,一共有i-j-1个
				//comb(i-j-1,j-k-1)

				for(int k= max(2*j-i,1);k<j;k++)
				{
					long long tm=dp[j][k];
					tm*=comb[i-j-1][j-k-1];
					tm%=100003;
					dp[i][j]+=tm;
					dp[i][j]%=100003;
				}
			}
		}
	}

	int cas;
	cin>>cas;
	for(int cs=1;cs<=cas;cs++)
	{
		cin>>n;
		int res=0;
		for(int j=1;j<n;j++)
		{
			res+=dp[n][j];
			res%=100003;
		}
		cout<<"Case #"<<cs<<": "<<res<<"\n";

	}

}