#include <iostream>
#include <cstdio>
using namespace std;
int solve(int n,int k)
{
	int loop=1<<n;
	k%=loop;
	if(k+1==loop) return 1;
	else return 0;
}
int main()
{
	int t;
	scanf("%d",&t);
	int i;
	for(i=1;i<=t;i++)
	{
		int n,k;
		scanf("%d%d",&n,&k);
		int ans=solve(n,k);
		if(ans==0)
			printf("Case #%d: OFF\n",i);
		else
			printf("Case #%d: ON\n",i);
	}
	return 0;
}
