// al.cpp : Defines the entry point for the console application.
//
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(c) (c).begin(),(c).end()
#define sz(a) int((a).size()) 
#define pb push_back 
typedef long long LL;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 

double readTime() {
  return double(clock()) / CLOCKS_PER_SEC;
}

int mymap[26][15];
string arr[5000];
int ans[500];
int main()
{
	int L,D,N;
	cin>>L;
	cin>>D;
	cin>>N;
	REP(i,D)
	{
		cin>>arr[i];
	}
	REP(i,N)
	{
		REP(t,26)
			REP(t2,15)
			mymap[t][t2] = 0;
		string pat;
		cin>>pat;
		int temp=0;
		int state=0;
		for(int j=0;j<pat.length();j++)
		{
			if(state == 0)
			{
				if(pat[j] !='(') {
					char ch = pat[j];
					mymap[ch-'a'][temp++] = 1;
				}
				else
				{
					state =1;
				}
				continue;
			}
			if(state == 1)
			{
				if(pat[j] !=')') {
					char ch = pat[j];
					mymap[ch-'a'][temp] = 1;
				}
				else
				{
					state = 0;
					temp++;
				}
				continue;
			}

		}
		for(int j=0;j<D;j++)
		{
			bool match=true;
			for(int k=0;k<L;k++)
			{
				if(mymap[arr[j][k]-'a'][k] == 0) 
				{
					match = false;
					break;
				}
			}
			if(match) ans[i]++;
		}
	
	}
	REP(i,N)
	{
		cout <<"Case #"<<i+1<<": "<<ans[i]<<endl;
	}
}



			

		
		
	


