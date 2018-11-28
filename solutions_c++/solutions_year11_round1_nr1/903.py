#include<stdio.h>
#include<iostream>
#include <string.h>
#include<map>
using namespace std;
int main()
{
	long long t,x,y,z,a=0,b,c;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		cin>>x>>y>>z;
		for(long long i=x;i>=0;i--)
			if((y*i)-((y*i/100)*100)==0)
				{a=i;break;}
		if(a==0) {cout<<"Case #"<<j<<": Broken\n";continue;}
		else{ b=a*y/100;c=2;}
		while(a!=100000)
		{
			if(z==0&&y!=0||z==100&&y!=100){c=2;break;} 
			if((z*a)-((z*a/100)*100)!=0)
			a++;
			else {c=1;break;}
		}
		if(a==0||c==2) cout<<"Case #"<<j<<": Broken\n";
		else cout<<"Case #"<<j<<": Possible\n";
	}
}
