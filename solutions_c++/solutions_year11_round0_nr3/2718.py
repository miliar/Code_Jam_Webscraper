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
	cin >> T;
	REP(index, T)
	{
		int N;
		cin>>N;
		vector<int> v;
		REP(i,N) {int tmp; cin>>tmp; v.PB(tmp); }
		sort(ALL(v));
		int tmp=0;
		REP(i,v.sz) tmp=(tmp^v[i]);
		if(tmp)
			cout<<"Case #"<<index+1<<": NO"<<endl;
		else
			cout<<"Case #"<<index+1<<": "<<accumulate(ALL(v),0)-v[0]<<endl;
	}

	return 0;
}
