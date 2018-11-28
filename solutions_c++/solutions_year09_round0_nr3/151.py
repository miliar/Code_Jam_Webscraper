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

int MOD=10000;

LL dp[20][505];

int n;

string p="welcome to code jam";

int main()
{
	int N;
	cin >> N;
	int index=0;
	string s;

	getline(cin,s);
	while(index<N)
	{
		getline(cin,s);
		n=s.sz;
		REP(i,n+1) dp[0][i]=1;
		REP(i,20) dp[i][0]=0;
		dp[0][0]=1;
		for(int i=1; i<20; i++)
		{
			for(int j=1; j<=n; j++)
			{
				if(p[i-1]==s[j-1])
				{
					dp[i][j]=(dp[i][j-1]+dp[i-1][j-1])%MOD;
				}
				else 
					dp[i][j]=dp[i][j-1];
			}
		}
		//REP(i,20) {REP(j,n+1) cout<<dp[i][j]<<" ";cout<<endl;}



		
		cout << "Case #" << ++index <<": " << setw(4) <<setfill('0') <<dp[19][n] << endl;
	}
	return 0;

}
