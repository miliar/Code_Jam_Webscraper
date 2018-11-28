#include<cstdio>
#include<cstring>
#include<string>
#include<iostream>

using namespace std;


int main()
{

	__int64 n,k,r;
	int t,j=0;


	freopen("A.in","r",stdin);
	freopen("B.in","w",stdout);
	scanf("%d",&t);

	while(t--)
	{
		scanf("%I64d%I64d",&n,&k);
		r=1<<n;
		k++;
		//printf("%I64d\n",r);
		if(k%r==0)
		{
			printf("Case #%d: ON\n",++j);
		}
		else
		{
			printf("Case #%d: OFF\n",++j);
		}
	}
		
	
	

	return 0;
}
