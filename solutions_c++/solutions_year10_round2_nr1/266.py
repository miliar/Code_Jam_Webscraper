#include <cstdio>
#include <numeric>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <cmath>
#include <iomanip>

using namespace std;

typedef vector <int> VI;
typedef vector <string> VS;
typedef long long LL;
typedef stringstream SS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(int i=(a); i<(b); i++)
#define FORE(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define PB push_back
#define sz size()
#define MP make_pair
#define two(x) (1<<(x))


/////////////////////////////////////////////////////////////////////////////////
int T,N,M;
string ex[200];
string need[200];

string f(string s)
{
	for(int i=s.sz-2; i>=0; i--)
		if(s[i]=='/') return s.substr(0, i+1);
}

int main()
{
	cin>>T;
	string line;
	getline(cin,line);
	REP(index, T)
	{
		cin>>N>>M;
		getline(cin,line);
		REP(i,N) getline(cin, ex[i]);
		REP(i,M) getline(cin, need[i]);

		map<string,int> mp;
		REP(i,N)
		{
			string s=ex[i]+'/';
			while(s!="/") { mp[s]++; s=f(s); }			
		}

		int cnt=0;
		REP(i,M)
		{
			string s=need[i]+'/';
			while(s!="/" and mp.count(s)==0) { mp[s]++; cnt++; s=f(s); }
		}

		cout<<"Case #"<<index+1<<": "<<cnt<<endl;

	}

	return 0;
}
