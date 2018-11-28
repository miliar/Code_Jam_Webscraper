#include<iostream>
#include<vector>
#include<cmath>
#define pb push_back

using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	int ct=0;
	while(t--)
	{
		int n;
		ct++;
		scanf("%d",&n);
		int a,b,c;
		if(n==2)
		{
			cin>>a>>b;
			int k=abs(b-a);
			int m=ceil(b*1.0/k);
			cout<<"Case #"<<ct<<": "<<m*k - b<<endl;
			
		}
		else
		{
			cin>>a>>b>>c;
			int k=__gcd(abs(a-b) , abs(c-b));
			int m=ceil(b*1.0/k);
			cout<<"Case #"<<ct<<": "<<m*k-b<<endl;
		}	
			
		
	}
	return 0;
}