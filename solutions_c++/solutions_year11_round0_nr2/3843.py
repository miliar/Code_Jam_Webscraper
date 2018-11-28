// Magicka.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>

#define REP(i,n) for(int i = 0; i < n; i++) 
#define FOR(i,s,e) for(int i = s; i < e; i++) 
#define ALL(v) v.begin(), v.end() 
#define OUT(x) cout<<#x<<" = "<<x<<endl; 

using namespace std;

int c, d, n;
char joins[50][3];
char splits[50][2];

string result(std::string s)
{

	char c_last = 0;
	std::string res = "";
	REP(i,n)
	{
		char c = s[i];
		res += c;
		
			while(res.length() >= 2)
			{
				bool was = false;
				REP(i,c)
				{
					if((joins[i][0] == res[res.length()-1] && joins[i][1] == res[res.length()-2]) || (joins[i][1] == res[res.length()-1] && joins[i][0] == res[res.length()-2]))
					{
						res = res.substr(0, res.length()-2);
						res += joins[i][2];
						was = true;
						break;
					}
				}
				if(!was)
					break;
			}

		REP(j,d)
		{
			if(res.find(splits[j][0]) != string::npos && res.find(splits[j][1]) != string::npos){

				res = "";
				c_last = 0;
				break;
			}			
		}
	}
	return res;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int t;
	cin>>t;
	REP(i,t)
	{
		char temp[10];
		cin>>c;
		REP(j,c)
		{
			cin>>temp;
			joins[j][0] = temp[0];
			joins[j][1] = temp[1];
			joins[j][2] = temp[2];
		}
		cin>>d;
		REP(j,d)
		{
			cin>>temp;
			splits[j][0] = temp[0];
			splits[j][1] = temp[1];
		}
		cin>>n;
		cin>>temp;
		std::string res = result(temp);
		cout<<"Case #"<<i+1<<": [";
		if(!res.empty())
		{
			for(int j = 0; j < res.length()-1; j++)
				cout<<res[j]<<", ";
			cout<<res[res.length()-1];
		}
		cout<<"]\n";
	}

	return 0;
}

