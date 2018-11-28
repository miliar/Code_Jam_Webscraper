#include<iostream>
using namespace std;

int L,P,te,ans;
double c;

int main()
{
	freopen("Bl.in","r",stdin);
	freopen("Bl.txt","w",stdout);
	cin>>te;
	for(int ca=1;ca<=te;++ca)
	{
		cin>>L>>P>>c;
		ans=0;
		double x1,x2;
		while(1)
		{
			x1=(double)L*c;
			x2=(double)P/c;
			if(x2<=L&&x1>=P)
			{
				break;
			}
			c=c*c;
			ans++;
		}
		printf("Case #%d: %d\n",ca,ans);
	}
	return 0;
}
