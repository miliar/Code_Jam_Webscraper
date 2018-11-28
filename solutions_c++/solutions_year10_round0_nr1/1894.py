#include<iostream>
using namespace std;

int t,n,k;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.txt","w",stdout);
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%d %d",&n,&k);
		int m = (1<<n);
		printf("Case #%d: ",i);
		k %= m;
		if(k == m-1)
		{
			printf("ON\n");
		}
		else
		{
			printf("OFF\n");
		}
		
	}
	
}