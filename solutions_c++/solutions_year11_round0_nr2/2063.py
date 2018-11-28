#include <fstream>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <cstring>
using namespace std;

#include <time.h>

#define sz(a) a.size()
#define vi vector<int>
#define vs vector<string>
#define vii vector< pair<int,int> >
#define all(a) a.begin(),a.end()
#define pb push_back

bool canCombine(string s, string& comRes, vector<string>& com)
{
	string s1 = s;
	reverse(s1.begin(),s1.end());

	for(int i=0;i<sz(com);i++)
	{
		string lhs = com[i].substr(0,2);
		if(lhs==s1||lhs==s)
		{
			comRes = com[i].substr(2);
			return true;
		}
	}

	return false;
}

bool canClear(string s, vector<string>& clear, int& sClear, int& eClear)
{
	for(int i=0;i<sz(clear);i++)
	{
		string c1 = clear[i];

		int a1 = s.find(clear[i][0]), a2 = s.find(clear[i][1]);
		if(a1!=string::npos&&a2!=string::npos)
		{
			sClear = a1<a2?a1:a2;
			eClear = a1<a2?a2:a1;
			return true;
		}
	}

	return false;
}

string doMagic(string base, vector<string>& com, vector<string>& clear)
{
	string res = "[";
	if(sz(base)==1)
		return "["+base+"]";

	for(int j=1;j<sz(base);j++)
	{
		string comRes = "";
		if(canCombine(base.substr(j-1,2), comRes, com))
		{
			base.replace(j-1,2,comRes);
			j--;
			continue;
		}

		int sClear=-1, eClear=-1;
		string temp = base.substr(0, j+1);
		if(canClear(temp, clear,sClear, eClear))
		{
			base.erase(0, sz(temp));
			j=0;
		}
	}

	int n = sz(base);
	for(int i=0;i<n;i++)
	{
		res+=base[i];
		if(i!=n-1)
		{
			res+=", ";
		}
	}

	return res+"]";
}

int main()
{
	ifstream in("B-large.in");
	ofstream out("MAGICA_LARGE.out");

	int n,c,t,d;
	in>>t;

	for(int i=1;i<=t;i++)
	{
		vector<string> com;
		vector<string> clear;
		string s;
		in>>c;
		for(int j=1;j<=c;j++)
		{
			in>>s;
			com.push_back(s);
		}

		in>>d;

		for(int j=1;j<=d;j++)
		{
			in>>s;
			clear.push_back(s);
		}

		in>>n>>s;
		out<<"Case #"<<i<<": "<<doMagic(s,com,clear)<<endl;
	}
	in.close();
	out.close();
	return 0;
}