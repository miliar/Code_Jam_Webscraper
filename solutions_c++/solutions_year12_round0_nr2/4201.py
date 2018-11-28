#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <set>
#include <vector>
#include <map>
using namespace std;

int main()
{
	char m[255];
	ifstream cin("input.txt");
	ofstream cout("out.txt");
	int T,Ti,i=0,p,n,s,a,r;
	cin>>T;
	for(Ti=1;Ti<=T;Ti++)
	{
		r=0;
		cin>>n>>s>>p;
		for(i=0;i<n;i++)
		{
			cin>>a;
			if(a%3==0)
			{
				if(a/3>=p)
					r++;
				else if(a>0&&a/3==p-1&&s)
					{r++;s--;}
			}
			else if(a%3==2)
			{
				if(a/3+1>=p)
					r++;
				else if(a/3+1==p-1&&s)
					{r++;s--;}
			}
			else
				if(a/3+1>=p)
					r++;
		}
		cout<<"Case #"<<Ti<<": "<<r<<'\n';
	}

}