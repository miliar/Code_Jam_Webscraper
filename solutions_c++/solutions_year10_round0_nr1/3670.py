#include<iostream>
using namespace std;
int t;
int fun(int v)
{
	int temp=1;
	for(int i=1;i<=v;i++)
		temp*=2;
	return temp;
}
int main()
{
	//freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small.txt","w",stdout);

	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int n,k;
		scanf("%d%d",&n,&k);
        if(k%fun(n)==fun(n)-1)
			printf("Case #%d: ON\n",i);
		else 
			printf("Case #%d: OFF\n",i);
	}
	return 0;
}