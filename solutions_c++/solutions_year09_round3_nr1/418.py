// 1.cpp : Defines the entry point for the console application.
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


int main()
{
	int runs;
	cin>>runs;
	REP(i,runs)
	{
		vector<int> digits;
		string str;
		int num = '0';
		map<char,int> m;
		cin >>str;
		m[str[0]] = '1';
		for(int j=0;j<str.size();j++)
		{
			char ch = str[j];
			if(m[ch])
			{
				digits.push_back(m[ch]);
			}
			else
			{
				
				m[ch] = num;
				num++;
				if(num == '1') num++;
				digits.push_back(m[ch]);
				
			}
		}
		int base = m.size();
		if(base == 1) base++;
		unsigned long long res=0;
		for(int j=0;j<digits.size();j++)
		{
			res =res*base + digits[j]-'0';
		}
		cout<<"Case #"<<i+1<<": ";
		cout <<res<<"\n";

		
		
		
	}
}

