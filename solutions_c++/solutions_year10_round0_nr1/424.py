#include<iostream>

using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++)
	{
		int n,k;
		cin>>n>>k;
		printf("Case #%d: %s\n",tt,((k&((1<<n)-1))-((1<<n)-1))?"OFF":"ON");
	}
	return 0;
}
