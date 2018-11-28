#include <iostream>
using namespace std;

int testb(int n,int k)
{
	int i,b=1;
	for(i=0;i<n;i++)
	{
		b=1<<i;
		if(!(b&k)) return 0;
	
	}

	return 1;


}

int main()
{
	freopen("d:\\A-small-attempt0.in", "r", stdin);
	freopen("d:\\A-small-attempt0.out", "w", stdout);

	int t,n,k,i;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>n>>k;
		if (testb(n,k))
		printf("Case #%d: ON\n",i);
		else printf("Case #%d: OFF\n",i);
	
	}




	return 0;
}