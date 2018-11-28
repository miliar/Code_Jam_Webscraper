#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<iterator>
using namespace std;

#define i64 __int64
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define pi acos(-1.0)
#define inf ((i64)1<<30)
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define pb push_back
#define eps 1e-11
#define MOD 100003

int vi[550][550],dp[550][550],f[550][550];

int func(int n,int r)
{
	if(r==1)
		return n;
	if(r==0 || n==r)
		return 1;
	if(vi[n][r])
	{
		return dp[n][r];
	}
	vi[n][r]=1;
	return dp[n][r]=func(n-1,r-1)+func(n-1,r);
}

int main()
{
	freopen("C-small-attempt2.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cs,i,n,t=1,j,k,x,y,res;
	f[2][1]=1;
	f[3][1]=1;
	f[3][2]=1;
	for(i=4;i<=500;i++)
	{
		f[i][1]=1;
		f[i][2]=1;
		for(j=3;j<i;j++)
		{
			for(k=j-1;k>0;k--)
			{
				x=j-k-1;
				if(i-j-1<x)
					break;
				x=func(i-j-1,x);
				//y=func(j-2,y);
				f[i][j]+=x*f[j][k];
				f[i][j]%=MOD;
			}
		}
	}
	cin>>cs;
	while(cs--)
	{
		cin>>n;
		res=0;
		for(i=1;i<n;i++)
		{
			res+=f[n][i];
			res%=MOD;
		}
		printf("Case #%d: %d\n",t++,res);
	}
	return 0;
}


