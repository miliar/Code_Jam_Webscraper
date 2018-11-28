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

int L;

bool f(string t, string s)
{
	int j=0;
	REP(i,L)
	{
		char a=t[i];
		map<char,int> mp;
		if(s[j]!='(') {mp[s[j]]=1;j++;}
		else 
		{
			j++;
			while(s[j]!=')')
			{
				mp[s[j]]=1; j++;
			}
			j++;
		}
		if( mp.count(a) == 0 ) return false;
	}
	return true;
}

int main()
{
	int D,N;
	cin >> L>>D>>N;
	vector<string> dict;
	REP(i,D) {string w; cin>>w; dict.PB(w);}
	int index=0;
	while(index<N)
	{
		string s;
		cin>>s;
		int ret=0;
		REP(i,D) if( f(dict[i], s) ) ret++;
		cout << "Case #" << ++index <<": " << ret << endl;
	}
	return 0;

}
