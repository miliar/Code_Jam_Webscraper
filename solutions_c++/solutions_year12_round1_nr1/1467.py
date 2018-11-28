#include <iostream>
using std::cout;
using std::cin;
using std::fixed;
#include <iomanip>
using std::setprecision;

int main()
{
	int cases,a,b;
	long double p[100010],temp,y;
	cin>>cases;
	p[0]=1;
	for(int kase=1;kase<=cases;kase++)
	{
		cin>>a>>b;
		cin>>p[1];
		for(int i=2;i<=a;i++)
		{
			cin>>temp;
			p[i]=p[i-1]*temp;
		}
		y=(b-a+1)*p[a]+(2*b-a+2)*(1-p[a]);
		if(b+2<y)
		{
			y=b+2;
		}
		for(int i=1;i<=a;i++)
		{
			temp=((b-a+2*i+1)*p[a-i])+((2*b-a+2*i+2)*(1-p[a-i]));
			if(temp<y)
			{
				y=temp;
			}
		}
		cout<<"Case #"<<kase<<": "<<fixed<<setprecision(6)<<y<<"\n";
	}
	return 0;
}