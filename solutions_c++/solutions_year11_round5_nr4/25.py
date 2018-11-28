#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("../../output.txt");
ifstream fin("../../input.txt");

bool issquare(long long x)
{
	long long a  = sqrt((double)x);
	a--;
	if(a*a==x)
		return true;
	a++;
	if(a*a==x)
		return true;
	a++;
	if(a*a==x)
		return true;
	a++;
	if(a*a==x)
		return true;
	a++;
	if(a*a==x)
		return true;
	a++;
	return false;
}
	

long long toint(string s)
{
	long long ans = 0;
	for(int i=0; i<s.size(); i++)
	{
		ans*=2;
		if(s[i]=='1')
			ans++;
	}
	return ans;
}
	


string solve(string s)
{
	int n =0;
	int i,j,k;
	for(i=0; i<s.size(); i++)
	{
		if(s[i]=='?')
			n++;
	}
	
	for(k=0; k<(1<<n); k++)
	{
		j= 0;
		string t = s;
		for(i=0; i<s.size(); i++)
		{
			if(s[i]=='?')
			{
				if( (k&(1<<j))>0)
				{
					t[i]='1';
				}
				else {
					t[i]='0';
				}
				j++;
			}
		}
		long long x = toint(t);
		if(issquare(toint(t)))
		{
			cout << x << endl;
			return t;
		}
	}
	return s;
}
		




int main(void)
{
	int ttt;
	fin >> ttt;
	int ct = 0;
	string s;
	
	while(ttt>0)
	{
		ct++;
		ttt--;
		int n,i,j,k;
		
		int ans = 0;
		string s;
		fin >> s;
		
		string t=  solve(s);
		cout << "Case #" << ct << ":" << " " << t << endl;
		fout << "Case #" << ct << ":" << " " << t << endl;
		
		
		
	}
	
	
	return 0;
}

