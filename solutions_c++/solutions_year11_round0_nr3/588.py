#include<iostream>
using namespace std;
int main()
{
	freopen("3.in","r",stdin);
	freopen("3.out","w",stdout);
	int cs,c,sum,tot,mi,k,i,n;
	cin>>cs;
	for (c=1;c<=cs;c++)
	{
		cin>>n;
		sum=0;
		tot=0;
		mi=1000000000;
		for (i=0;i<n;i++)
		{
			cin>>k;
			sum^=k;
			tot+=k;
			mi=min(mi,k);
		}
		if (sum==0) printf("Case #%d: %d\n",c,tot-mi);
		else  printf("Case #%d: NO\n",c);
	}
	return 0;
}
