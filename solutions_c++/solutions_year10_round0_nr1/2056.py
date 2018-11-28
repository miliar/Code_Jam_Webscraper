#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

int pow[31];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,cas = 1;
	pow[0] = 1;
	for(int i = 1; i < 31; i++)
		pow[i] = pow[i-1] << 1;
	scanf("%d",&t);
	while(t--)
	{
		int n,k;
		scanf("%d%d",&n,&k);
		int p = pow[n+1] - pow[n];
		if( k && k >= pow[n]-1 && (k-pow[n]+1)%p == 0 )
		{
			printf("Case #%d: ON\n",cas++);
		}
		else
		{
			printf("Case #%d: OFF\n",cas++);
		}
	}
	return 0;
}
