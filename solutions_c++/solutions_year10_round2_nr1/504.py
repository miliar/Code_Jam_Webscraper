// Jam_A_R1.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <map>
using namespace std;

map<string, long long> m;
int main()
{
	freopen("large.in", "r", stdin);
	freopen("large.out", "w", stdout);
	long long t;
	cin>>t;
	for(long long tt=1; tt<=t; tt++)
	{
		m.clear();
		long long t1, t2;
		cin>>t1>>t2;
		string s;
		for(long long i=0; i<t1; i++)
		{
			cin>>s;
			while(s.length()!=0)
			{
				m[s]=1;
				s=s.substr(0, s.find_last_of("/"));
			}
		}
		long long r, res=0;
		for(long long i=0; i<t2; i++)
		{
			cin>>s;
			r=0;
			while(s.length()!=0 && m[s]!=1)
			{
				m[s]=1;
				r++;
				s=s.substr(0, s.find_last_of("/"));
			}
			res+=r;
		}
		cout<<"Case #"<<tt<<": "<<res<<endl;


	}

	return 0;
}

