#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string.h>
#include<math.h>
#include<algorithm>

/////////////--------------stl library------------------///////////
#include<stack>

using namespace std;

typedef long long int int64;
typedef long double float64;
#define shift(x)  (1<<(x));
#define shift64(x) (((int64)(1))<<(x))

int gcd(int a, int b)
{
	if (b==0)
		return a;
	else
		return gcd(b,a%b);
}

int main()
{
	int ch;
	cin>>ch;
	for(int i=1;i<=ch;i++)
	{
		int64 n,pd,pg;
		int flag=0;
		cin>>n>>pd>>pg;
		int pd_den,pg_den;
		pd_den=100;
		pg_den=100;
		int x=gcd(pd_den,pd);
		int y=gcd(pg_den,pg);
		pd_den=pd_den/x;
		pg_den=pg_den/y;
		//cout<<pd_den<<" "<<pg_den;
		if(pd_den<=n)
		{
			flag=1;
				
		}
		if((pd==0 && pg!=0)||(pd!=0 && pg == 0))
			flag=0;
		if(pg>pd && pg ==100)
			flag=0;
			
		if(flag==1)
			cout<<"Case #"<<i<<": "<<"Possible\n";
		else
			cout<<"Case #"<<i<<": "<<"Broken\n";
		
	}
	return 0;
}
