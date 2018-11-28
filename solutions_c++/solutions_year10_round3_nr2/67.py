#include<iostream>
#include<cstdio>
using namespace std;
long long t,l,p,c,a,b,x;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("b.out","w",stdout);
	cin>>t;
	for (long long test=1;test<=t;test++)
	{
		cin>>l>>p>>c;
		a=c; x=1;
		while (l*a<p)
		{
			a*=c;	x++;
		}
		a=0;  b=1;
		while(b<x)
		{
			b<<=1;	a++;
		}
		cout<<"Case #"<<test<<": "<<a<<endl;
	}
	fclose(stdin);  fclose(stdout);
	return 0;
}

