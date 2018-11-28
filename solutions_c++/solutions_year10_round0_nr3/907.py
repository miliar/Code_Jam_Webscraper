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


LL dp[1500];
LL mem[1500];

int main()
{
	LL T, R,k,N;
	cin>>T;
	REP(index, T)
	{
		cin>>R>>k>>N;
		vector<int> v(N);
		REP(i,N) cin>>v[i];
		
		LL at=0;
		LL curR=0;
		LL ret=0;
		REP(i,1500) dp[i]=-1, mem[i]=-1;

		while(true)
		{
			if(mem[at]!=-1) break;
			
			mem[at]=curR; dp[at]=ret;

			LL total=0;
			LL tmp=at;

			while(total+v[at]<=k) { total+=v[at]; at=(at+1)%N; if(at==tmp) break; }

			ret+=total;

			curR++;

			if(curR>=R) break;
		}
		if(curR>=R)
		{
			cout<<"Case #"<<index+1<<": "<<ret<<endl;
			continue;
		}

		LL start=mem[at];
		LL cycle=curR-start;
		LL cost=ret-dp[at];
		LL ans=dp[at]+cost*((R-start)/cycle);
		R=(R-start)%cycle;
		
		REP(i,R)
		{
			LL total=0;
			LL tmp=at;

			while(total+v[at]<=k) { total+=v[at]; at=(at+1)%N; if(at==tmp) break; }

			ans+=total;
		}
		
		cout<<"Case #"<<index+1<<": "<<ans<<endl;

	




	}
	

	return 0;
}
