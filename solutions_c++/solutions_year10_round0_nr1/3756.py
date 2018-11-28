#include<iostream>
#include<algorithm>
#include<string.h>
#include<vector>
#include<math.h>
using namespace std;

int pp(int a,int b)
{
	int ans=1;
	int i;
	for(i=1;i<=b;i++)
	{
		ans*=a;
	}
	return ans;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("ans2.out","w",stdout);
	int t,n,k;
	int fengge;
	scanf("%d",&t);
	int i;
	for(i=1;i<=t;i++)
	{
		scanf("%d%d",&n,&k);
		fengge=pp(2,n);
		if (k%fengge==fengge-1)
			cout<<"Case #"<<i<<": ON"<<endl;
		else
			cout<<"Case #"<<i<<": OFF"<<endl;
	}
	return 0;
}