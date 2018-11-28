#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <cctype>
#include <algorithm>
#include <functional>
#include <cmath>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define fo(i,n) for(i=0;i<(n);++i)

typedef vector<int> vi ;
typedef vector<string> vs ;
typedef vector<double> vd ;
#define sz(x) ((int)(x).size())
#define all(x) x.begin(),x.end()
#define pb(x) push_back(x)
typedef long long ll;

vector<string> dic;
vector<vector<bool> > ts;
int calc()
{
	int cnt = 0;
	for(int i = 0 ; i < sz(dic) ; i++)
	{
		bool f = 1;
		for(int j = 0 ; j < sz(dic[i]) ; j++)
			if(!ts[j][dic[i][j]-'a'])
			{
				f= 0;
				break;
			}
		if(f)cnt++;
	}
return cnt;
}
int main()
{
	int n,l,d;
	//freopen("inp.in","rt",stdin);

		freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);

	cin>>l>>d>>n;
	string t;
	for(int i = 0 ; i < d;  i++)
	{
		cin>>t;
		dic.push_back(t);
	}
	for(int i = 0 ; i < n ; i++)
	{
		ts.clear();
		cin>>t;
		bool in = false;
		ts.resize(l,vector<bool>(26,0));
		int c = -1;
		for(int j = 0 ; j < sz(t) ; j++)
		{
			if(t[j]==')'){in=false; continue;}
			if(t[j]=='('){in = true; c++; continue;}

			if(t[j]!=')'&&t[j]!='('&&!in)
				c++;
			ts[c][t[j]-'a']=1;
		}

		int res = calc();
		cout<<"Case #"<<i+1<<": ";
		cout<<res<<endl;
	}


	return 0;
}
