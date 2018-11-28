#include <iostream>
using namespace std;

long long t,ca,n,pd,pg,x1,x2,y1,y2,d;

long long gcd(long long a,long long b)
{
	if (b==0) return a;
	else return gcd(b,a%b);
}

int main()
{
	freopen("in.in","r",stdin);
	freopen("ou.ou","w",stdout);
	cin>>t;
	while (t--)
	{
		ca++;
		cin>>n>>pd>>pg;
		cout<<"Case #"<<ca<<": ";
		if (pg==0&&pd!=0) 
		{
			cout<<"Broken"<<endl;
			continue;
		}
		else if (pg==0&&pd==0)
		{
			cout<<"Possible"<<endl;
			continue;
		}
		if (pd!=0)
		{
			d=gcd(pd,100);
			x1=pd/d; y1=100/d;
		} else
		{
			x1=0; y1=n;
		}
		d=gcd(pg,100);
		x2=pg/d; y2=100/d;
		if (y1>n||(x2==y2&&pd!=pg)) cout<<"Broken"<<endl;
		else cout<<"Possible"<<endl;
	}
}
		
	
