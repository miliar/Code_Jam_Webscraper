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

map<LL, int> mp;

bool f(LL n, int b)
{
	if(n==1) return true;
	if( mp.count(n) ) return false;
	mp[n]=1;
	LL t=0;
	LL m=n;
	while(m) { LL p=m%b; t+=p*p; m/=b; }
	return f(t, b);
}

int main()
{
	int T;
	cin >> T;
	int index=0;
	mp.clear();

	string line;
	getline(cin, line);

	while(index<T)
	{
		VI bases;
		int b;
		SS ss;
		getline(cin, line);
		ss << line;
		while(ss>>b) bases.PB(b);

		for(LL i=2; ; i++)
		{
			bool ok=true;
			for(int j=0; j<bases.sz; j++)
			{
				mp.clear();
				if( f(i, bases[j])==false ) { ok=false; break; }
			}
			if( ok )
			{
				cout << "Case #" << ++index <<": " << i  << endl;
				break;
			}
		}
	}
	return 0;

}
