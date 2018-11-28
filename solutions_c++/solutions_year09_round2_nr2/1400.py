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
	unsigned long long i;
	int runs;
	cin >>runs;
	int j=1;
	while(runs--)
	{
		
		char s[50];
		cin>>i;
		int n =sprintf(&s[1],"%lld",i);
		s[0]='0';
		s[n+1] =0;
		next_permutation(&s[0],&s[n+1]);
		if(s[0] == '0')
			cout<<"Case #"<<j<<": "<<&s[1]<<endl;
		else
			cout<<"Case #"<<j<<": "<<&s[0]<<endl;
		j++;
	}

	return 0;
}

