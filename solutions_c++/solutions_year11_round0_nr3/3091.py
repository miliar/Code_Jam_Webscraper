#include <iostream>
using namespace std;

const int N = 1010;
int v[N];
int ans;
int n;

void solve(int xor1, int sum1, int xor2, int sum2, int flag, int i)
{
	if ( i==n )
		return;
	if ( flag )
	{
		xor1 ^= v[i];
		sum1 += v[i];
	}
	else
	{
		xor2 ^= v[i];
		sum2 += v[i];
	}
	if (i==n-1 && xor1==xor2 && xor1!=0 )
	{
		int tem = max(sum1,sum2);
		if( tem > ans )
			ans = tem;
	}
	solve(xor1,sum1,xor2,sum2,0,i+1);
	solve(xor1,sum1,xor2,sum2,1,i+1);
}

int main()
{
	//freopen("F:\\DownLoad\\C-small-attempt0.in","r",stdin);
	//freopen("F:\\C-small-attempt0.out","w",stdout);
	int t;
	scanf("%d",&t);
	for ( int c = 1; c <= t; c++ )
	{
		ans = 0;
		scanf("%d",&n);
		for ( int i = 0; i < n; i++ )
			scanf("%d",&v[i]);
		solve(0,0,0,0,0,0);
		solve(0,0,0,0,1,0);
		if ( ans==0 )
			printf("Case #%d: NO\n",c);
		else
			printf("Case #%d: %d\n",c,ans);
	}
}