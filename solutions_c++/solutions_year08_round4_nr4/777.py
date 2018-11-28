#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
#include<cmath>
#include<iomanip>
#include<fstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
const ll Mod=1000000007;
ll A[600000];
//ll Ans[600000][600000];
ll Ans1[600000];
int k;
string word;
vector<int>Index;
vector<int>Begin;
string Per(string &tmp)
{
	string ans;
	string::size_type pos=0;
	while(pos<tmp.size())
	{
		string test;
		for(int j=0;j<k;j++)
		{
			test.push_back(tmp[pos]);
			pos++;
		}
		for(int j=0;j<k;j++)
		{
			ans.push_back(test[Index[j]-1]);
		}
	}
	return ans;
}
ll Cal(string &tmp)
{
	ll ans=0;
	ans++;
	string::size_type pos=1;
	char last=tmp[0];
	while(pos<tmp.size())
	{
		char th=tmp[pos];
		pos++;
		if(th!=last)
			ans++;
		last=th;
	}
	return ans;
}
int  main(){
	string filein;
	//filein="A-small.in";
	//filein="A-large.in";
	//filein="A-small(3).in";
	filein="A-small-attempt0.in";
	filein="D-small-attempt0.in";
	string fileout;
	//fileout="Anslarge.txt";
	fileout="Anstest.txt";
	//fileout="Anssmall.txt";
	freopen(filein.c_str(), "r", stdin);
	freopen(fileout.c_str(), "w", stdout);
	int  Case;
	cin>>Case;

	for(int  i=1;i<=Case;i++)
	{
		printf("Case #%d: ",i);
		cin>>k>>word;
		Index.clear();
		Begin.clear();
		for(int j=0;j<k;j++)
		{
			Index.push_back(j+1);
			Begin.push_back(j+1);
		}
		ll finans=1000000000000;
		while(1)
		{
			string tmp(word);

			string tmp2(Per(tmp));
			ll tmpans=Cal(tmp2);
			if(tmpans<finans)
				finans=tmpans;
			next_permutation(Index.begin(),Index.end());
			bool same=true;
			for(int l=0;l<k;l++)
			{
				if(Index[l]!=Begin[l])
				{
					same=false;
					break;
				}
			}
			if(same)
				break;
		}
		cout<<finans<<endl;
		
	}

	return 0;
}