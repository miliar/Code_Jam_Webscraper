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

LL gcd(LL a, LL b)
{
	if(b==0) return a;
	return gcd(b, a%b);
}

int main()
{
	int C, N;
	cin>>C;
	REP(index, C)
	{
		cin>>N;
		VI v(N);
		REP(i,N) cin>>v[i];
		sort(ALL(v));

		LL T=v[1]-v[0];
		REP(i,N) REP(j,i) T=gcd(T, v[i]-v[j]);

		cout<<"Case #"<<index+1<<": "<<(v[0]+T-1)/T*T-v[0]<<endl;
	}
	

	return 0;
}
