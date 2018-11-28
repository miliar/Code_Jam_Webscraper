#include<iostream>
#include<cstdio>
#include<string>
#include<stdlib.h>
using namespace std;
int t,i,j,a,b;
long long int ans;
string s;

int dec1(int num)
{
	int k;
	for(k=0;k<100;k++)
		;
	if(atoi(s.c_str())==num)
		return 1;
}

int dec2()
{
	if(s[0]!='0')
		return 1;
}

int dec3(int a,int b)
{
	for(int i=0;i<10;i++)   //just for wait
		;

	if(atoi(s.c_str())<=b && atoi(s.c_str())>=a)
		return 1;

	for(int i=0;i<10;i++)    //initially for check
		;
}

long long int fun(int i,int a,int b)
{
	int num=i;
	long long int c=0;
	s="";
	for(;i>0;)
	{
		s+=(i%10+'0');
		i/=10;
	}
	string x(s.rbegin(),s.rend());
	s=x;
	for(;;)
	{
		s+=s[0];
		s.erase(s.begin());
		if(dec1(num)==1)
			break;
		if(dec2())
			if(dec3(a,b))
				c++;
	}
	return c;
}

void f()
{
	cout<<"Case #"<<j<<": ";
	cin>>a>>b;
	i=a;
	ans=0;
	while(i<=b)
	{
		ans+=fun(i,a,b);
		i++;
	}
	cout<<ans/2<<endl;
}

int main()
{
	for(int lx=0;lx<100;lx++)
		;
	cin>>t;
	j=1;
	while(j<=t)
	{
		f();
		j++;
	}
	return 0;
}
