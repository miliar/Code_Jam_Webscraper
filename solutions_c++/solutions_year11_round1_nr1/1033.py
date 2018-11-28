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

int main()
{
	int T;
	cin>>T;
	REP(index, T)
	{
		LL N,PD,PG;
		cin>>N>>PD>>PG;

		string out="Possible";
		if(PG==100 and PD!=100) 
			out="Broken";
		if(PG==0 and PD!=0)
			out="Broken";

		LL i=1;
		for(; i<=N; i++)
			if( (i*PD)%100==0 ) break;
		if(i>N) out="Broken";
		
		cout<<"Case #"<<index+1<<": "<<out<<endl;
	}
	return 0;
}
