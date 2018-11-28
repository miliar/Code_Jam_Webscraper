#define _CRT_SECURE_NO_DEPRECATE
//
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <map>
#include <set>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

const double zero=1e-6;
const double limit=1e8;
#define SZ(x) (int(x.size()))

#define IFF_GUYING
#ifdef IFF_GUYING
	ifstream inf("in.txt");
#define cin inf
#endif

ofstream outf("out.txt");
#define cout outf

bool cmp(string &a,string &b)
{
	return  ( (a.size()==b.size() && a<b) || a.size()<b.size());
}

// ai - b
// 输入无前导0，且a>=b;
void de(string& a,string &b)
{
	int bn = SZ(b) -1;
	int an = SZ(a) -1;
	
	while(an >=0)
	{
		if(a[an] < '0')
		{
			a[an-1] -= 1;
			a[an] += 10;
		}

		if(bn >=0)
		{
			if(a[an] < b[bn])
			{
				a[an-1] -=1;
				a[an] += 10;
			}
			a[an] -= (b[bn]-'0');
		}
		an --;
		bn --;
	}
	while(a.size()>1 && a[0]=='0')
		a=a.substr(1);
}

// a对b取模
// 
string mod(string &a,string &b)
{
	// a<b;
	if(cmp(a,b))
		return a;
	if(a==b || b=="1")
		return string("0");

	int bn = SZ(b);
	int st = 0;
	string ta;
	while( st < SZ(a))
	{
		ta += a.substr(st,bn -st);
		st = bn ++;
		while(ta.size()>1 && ta[0]=='0')
			ta=ta.substr(1);
		while( !cmp(ta,b))
		{
			de(ta,b);
		}
	}
	return ta;
}
string gcd(string &a,string& b)
{ 
	if (b == "0")
		return a;
	else
		return gcd(b,mod(a,b));
}
int n;
string str[1000];

int main(int argc, char* argv[])
{
	int t;
	cin>>t;
	for(int it=0;it<t;it++)
	{
		cout<<"Case #"<<it+1<<": ";
		
		cin>> n;
		for(int i=0;i<n;i++)
		{
			cin>>str[i];
		}
		sort(str,str+n,cmp);
		string now = str[0];
		for(int i=1;i<n;i++)
			de(str[i],str[0]);
		string ret = str[1];
		for(int i=2;i<n;i++)
		{
			ret = gcd(ret,str[i]);
			if(ret == "1")
				break;
		}

		string before = mod(now,ret);
		if(before == "0")
			ret = before;
		else
			de(ret,before);
		cout<<ret<<endl;
	}
	return 0;
}
