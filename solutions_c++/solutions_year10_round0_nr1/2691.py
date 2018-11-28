#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int t;
	int n;
	int f=1;
	long long int k;
	long long int two_power;
	long long int ans;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&n,&k);
		two_power=1<<n;
		ans=two_power-1;
		k=k%two_power;
		//printf("%d %d\n",k,ans);
		if(k!=ans)
		{
			printf("Case #%d: OFF\n",f);
		}
		else
		{
			printf("Case #%d: ON\n",f);
		}
		f++;
	}
	return 0;
}
