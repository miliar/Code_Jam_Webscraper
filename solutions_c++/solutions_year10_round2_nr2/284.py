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
int C,N,K,B,T;
int X[100],V[100];

int main()
{
	cin>>C;
	REP(index, C)
	{
		cin>>N>>K>>B>>T;
		REP(i,N) cin>>X[i];
		REP(i,N) cin>>V[i];

		int best=1<<29;

		REP(i,(1<<N))
		{
			VI v;
			REP(j, N) if( i&(1<<j) ) v.PB(j);
			if(v.sz!=K) continue;
			int cnt=0;
			bool ok=true;

			for(int j=K-1; j>=0; j--)
			{
				if( X[v[j]]+V[v[j]]*T<B ) { ok=false; break; }
				if( j==K-1 ) cnt+=N-1-v[j];
				else cnt+=v[j+1]-v[j]-1;
			}

			if(ok) best=min(best, cnt);
		}
		cout<<"Case #"<<index+1<<": ";
		if(best==1<<29) cout<<"IMPOSSIBLE";
		else cout<<best;
		cout<<endl;
	}

	return 0;
}
