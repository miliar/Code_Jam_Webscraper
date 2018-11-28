#include<iostream>

using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	long long int ct=0;
	while(t--)
	{
		ct++;
		long long int n,k;
		cin>>n>>k;
		long long int sum=0;
		int i=0;
		
		string s="";
		while(k>0)
		{
			if(k%2)
			s+="1";
			else s+="0";
			k/=2;
			
		}
		if(s.size()<n) cout<<"Case #"<<ct<<": OFF"<<endl;
		else
		{
		string s1=s.substr(0,n);
		
		if(s1.find("0")!=string::npos)cout<<"Case #"<<ct<<": OFF"<<endl;
		else cout<<"Case #"<<ct<<": ON"<<endl;
		}
	}
return 0;
}	
		