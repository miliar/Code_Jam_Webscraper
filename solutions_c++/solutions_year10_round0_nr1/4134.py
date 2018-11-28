#include<iostream>
#include<cstdio>
using namespace std;
long long t,n,k,bitowe;
int main()
{
	scanf("%lld",&t);
	for(int i=1;i<=t;i++)
	{
		bitowe=0;
		scanf("%lld%lld",&n,&k);
		for(int q=0;q<n;q++)bitowe+=(1<<q);
		if(k%(bitowe+1)==bitowe && k>=bitowe)printf("Case #%d: ON\n",i);
		else printf("Case #%d: OFF\n",i);
	}
	return 0;
}