#include<iostream>
using namespace std;
const long long mod = 100003;
long long zuhe[501][501]={};
long long res[501][501];
int main()
{
	zuhe[0][0]=1;
	for(int i=0;i<=500;i++)zuhe[i][0]=zuhe[i][i]=1;
	for(int i=1;i<=500;i++)for(int j=1;j<i;j++)zuhe[i][j]=(zuhe[i-1][j-1]+zuhe[i-1][j])%mod;


	int d = 500;
	for(int i=2;i<=d;i++)
	{
		res[i][1]=1;
		for(int j=2;j<i;j++)
		{
			res[i][j]=0;
			for(int k=1;k<j;k++)
			{
				res[i][j]=(res[i][j]+res[j][k]*zuhe[i-j-1][j-k-1])%mod;
			}
		}
	}
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int zu;
	cin>>zu;
	for(int Cas =1 ; Cas<=zu;Cas++)
	{
		printf("Case #%d: ",Cas);
		int x;
		cin>>x;
		long long r =0;
		for(int i=0;i<=x;i++)
			r=(r+res[x][i])%mod;
		cout<<r<<endl;
	}
}