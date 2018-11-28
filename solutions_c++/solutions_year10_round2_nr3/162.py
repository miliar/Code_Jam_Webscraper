#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <string>
using namespace std;

const int MAXN=1000;
const long long P=100003;

long long res2[MAXN];

bool can(int mask,int n)
{
	int cur=n;

	while (true)
	{
		if ((mask&(1<<cur))==0)
		{
			if (cur==1)
				return true;
			return false;
		}
		int cnt=1;
		for (int i=0;i<cur;i++)
			if (mask&(1<<i))
				++cnt;

		if (cur==cnt)
			return false;
		cur=cnt;
	}
}

long long get_res(int x)
{
	if (x<0)
		return 0;
	return res2[x];
}

long long CNK[MAXN][MAXN];

void getCNK()
{
	CNK[0][0]=1;
	for (int i=1;i<=500;i++)
	{
		CNK[i][0]=1;
		CNK[i][i]=1;

		for (int j=1;j<i;j++)
		{
			CNK[i][j]=(CNK[i-1][j]+CNK[i-1][j-1])%P;
		}
	}
}

long long cnk(int x,int y)
{
	if (x<0 || y<0)
		return 0;
	return CNK[x][y];
}

long long a[MAXN][MAXN];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	getCNK();
	//for (int n=2;n<=25;n++)
	//{
	//	for (int j=0;j<(1<<(n-2));j++)
	//	{
	//		if (can((j<<2)|(1<<n),n))
	//			++res2[n];
	//	}
	//}

	memset(a,0,sizeof(a));
	a[2][1]=1;
	for (int i=3;i<=500;i++)
	{
		a[i][1]=1;
		for (int j=2;j<=i-1;j++)
		{
			for (int k=1;k<=j-1;k++)
				a[i][j]=(a[i][j]+cnk(i-j-1,j-k-1)*a[j][k])%P;
		}
	}
	
	int T;
	scanf("%d\n",&T);
	for (int test=1;test<=T;test++)
	{
		int n;
		cin>>n;

		long long r=0;
		for (int j=1;j<=n;j++)
			r+=a[n][j];
		
		cout<<"Case #"<<test<<": "<<r%P<<endl;
	}
	return 0;
}