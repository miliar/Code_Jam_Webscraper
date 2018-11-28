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

LL MOD=100003;

LL dp[550][550];
LL C[550][550];

LL go(int n, int val)
{
	LL &res=dp[n][val];
	if( res!=-1 ) return res;
	if( val==1 ) return res=1;
	res=0;
	for(int i=val-1; i>0; i--)
	{
		res=(res+C[n-val-1][val-i-1]*go(val, i))%MOD;
	}
	return res;
}

int main()
{
	int T, n;
	cin>>T;

	REP(i,550) REP(j,550) dp[i][j]=-1;

	C[0][0]=1;
	for(int i=1; i<550; i++)
	{
		C[i][0]=C[i][i]=1;
		for(int j=1; j<i; j++)
			C[i][j]=(C[i-1][j]+C[i-1][j-1])%MOD;
	}

	REP(index, T)
	{
		cin>>n;
		int cnt=0;
		for(int i=n-1; i>0; i--)
		{
			cnt=(cnt+go(n, i))%MOD;
		}
		//for(int i=1; i<n; i++) cout<<i<<": "<<dp[n][i]<<", "; cout<<endl;
		cout<<"Case #"<<index+1<<": "<<cnt<<endl;
	}
	return 0;
}
