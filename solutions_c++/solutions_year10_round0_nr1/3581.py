#include<iostream>
using namespace std;
int main()
{
	int t;
	__int64 n,k;
	freopen("d:/in.txt","r",stdin);
	freopen("d:/out.txt","w",stdout);
	scanf("%d",&t);
	for(int a=1;a<=t;a++)
	{
		scanf("%I64d%I64d",&n,&k);
		k++;
		k=k%(1<<n);
		if(k==0)
		{
			printf("Case #%d: ON\n",a);
		}
		else
		{
			printf("Case #%d: OFF\n",a);
		}
	}
}