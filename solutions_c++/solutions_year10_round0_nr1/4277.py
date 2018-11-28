#include<iostream>
#include<fstream>
using namespace std;

struct snap
{
	bool p;
	bool on;
	snap()
	{
		p=false;
		on=false;
	}
};

void change(snap s[35],int n)
{
	for(int i=0;i<n;i++)
	{
		if(s[i].p)
		{
			if(s[i].on)
				s[i].on=false;
			
			else s[i].on=true;
		}
	}

	for(int i=0;i<n-1;i++)
	{
		if(s[i].p && s[i].on)
		{
			s[i+1].p=true;
		}
		if(!s[i].on)
		{
			s[i+1].p=false;
		}
	}
}

int main()
{
	ifstream cin("A-small-attempt0.in");
	ofstream cout("a.txt");

	
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		snap s[35];
		int n,k;
		
		s[0].p=true;
		cin>>n>>k;

		for(int q=1;q<=k;q++)
		{
			change(s,n);
		}

		if(s[n-1].p && s[n-1].on)
			cout<<"Case #"<<i+1<<": "<<"ON\n";
		else cout<<"Case #"<<i+1<<": "<<"OFF\n";

	}



	return 0;
}