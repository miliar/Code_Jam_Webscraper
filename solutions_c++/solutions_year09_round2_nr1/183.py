#define _CRT_SECURE_NO_WARNINGS
#include <ctime>
#include <cfloat>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <complex>

using namespace std;

#define pb push_back
#define L(s) (int)((s).end()-(s).begin())
#define rep(i,n) for(int (i)=0;(i)<(n);++(i))
#define all(s) (s).begin(),s.end()
#define pi 3.1415926535897932384626433832795
#define vi vector<int>
#define inf 1000000000
#define ll long long
#define C(a) memset((a),0,sizeof((a)))
#pragma comment(linker, "/STACK:16777216")
int test,tests;
set<string> ani;
int n,m,k;
double dfs(string s)
{
	int rez=1;
	int i1=0;
	while(s[i1]!='(')
		++i1;
	++i1;
	int i2=L(s)-1;
	while(s[i2]!=')')
		--i2;
	string t=s.substr(i1,i2-i1+1);
	istringstream iss(t);
	string s2="";
	double w;
	char ch;
	do
	{
		iss>>ch;
		if (ch!=')'&&!(ch>='a'&&ch<='z'))
			s2+=ch;
	}while(ch!=')'&&!(ch>='a'&&ch<='z'));
	istringstream iss2(s2);
	iss2>>w;
	string para="";
	if (ch==')')
		return w;
	do
	{
		para+=ch;
		iss>>ch;
	}while(ch>='a'&&ch<='z');
	t="";
	int bal=0;
	do
	{
		t+=ch;
		if (ch=='(')
			++bal;
		if (ch==')')
			--bal;
		iss>>ch;
	}while(bal!=0);
	if (ani.find(para)!=ani.end())
		return w*dfs(t);
	t="";
	do
	{
		t+=ch;
		if (ch=='(')
			++bal;
		if (ch==')')
			--bal;
		iss>>ch;
	}while(bal!=0);
	return w*dfs(t);
}
int main()
{	
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>tests;
	for(int test=1;test<=tests;++test)
	{
		string s;
		char ch;
		int bal;
		cin>>bal;
		bal=0;
		scanf("%c",&ch);
		do
		{
			scanf("%c",&ch);
			if (ch=='(')
				++bal;
			if (ch==')')
				--bal;
			if (ch!='\n')
				s+=ch;
		}while(bal!=0);
		cin>>m;
		string s2;
		printf("Case #%d:\n",test);
		for(int i=0;i<m;++i)
		{
			ani.clear();
			cin>>s2;
			cin>>k;
			for(int j=0;j<k;++j)
			{
				cin>>s2;
				ani.insert(s2);
			}
			cout.precision(8);
			printf("%0.8f\n",dfs(s));
		}
	}
	return 0;
}