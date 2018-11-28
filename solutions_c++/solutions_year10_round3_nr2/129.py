#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
int tt,l,p,c;
int main()
{
	cin>>tt;	
	for (int kk=1;kk<=tt;++kk)
	{
		cin>>l>>p>>c;
		double r=p*1.0/(l*1.0);
		int num=0;
		l*=c;
		while (l<p)
		{
			l*=c;
			num++;
		}
		int ans;
		if (num==0)
		{
			ans=0;
		}
		else
		{
			double r=num*1.0;
			ans=0;
			while (r>=1)
			{
				r/=2;
				ans++;
			}
		}
		printf("Case #%d: ",kk);
		cout<<ans<<endl;
	}	
	return 0;	
}