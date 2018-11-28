#include<iostream>
#include<cstdio>
#include<queue>
#include<cstring>
#include<map>
#include<algorithm>
#include<cmath>
#include<set>
#include<sstream>
#include<map>
#include<utility>
#include<cmath>

#define S(n) scanf("%d",&n)
#define SL(n) scanf("%lld",&n)
#define SF(n) scanf("%Lf",&n)

#define REP(i,n) for(i=0; i<n; i++)
#define REPA(i,a,n) for(i=a; i<n; i++)
#define SOR(x) sort(x.begin(), x.end())
#define REV(x) reverse(x.begin(), x.end())
#define FOREACH(iter,var) for(__typeof((var).begin()) iter=(var).begin(); iter!=(var).end(); iter++)
#define PB push_back
#define VI vector<int>
#define SZ size()
#define VS vector<string>

#define MP make_pair
#define VVI vector< vector<int> >
#define INF 2000000000

#define CLR(var,val) memset(var,val,sizeof((var)))
#define S(n) scanf("%d",&n)
#define LL long long
#define LD long double
#define triple pair<int, pair<int,int> >
#define OFF 0
#define MOD
#define ISBITSET(n,i) ((n&(1<<i))>>i)
#define TOGGLEBIT(n,i) (n^(1<<i))
#define SETBIT(n,i) (n|(1<<i))
#define CLRBIT(n,i) (n & (n^(1<<i)))
#define FIN freopen("inp.in","r",stdin)
#define FOUT freopen("out.out", "w",stdout)
using namespace std;


int T, N, M;
set <string> dirs;
int main()
{
	FIN;
	FOUT;
	string s;	int i, j;
	cin >> T;
	int caseN = 1;
	LL ans = 0;
	while( T-- )
	{
		cin >> N >> M;
		dirs.clear();
		ans = 0;
		REP( i, N )
		{
			cin >> s;
			for( j = 1; j < s.SZ; j++ )
				if( s[j] == '/' )
				{
					dirs.insert(s.substr( 0, j ));
					//cout << "\tInserting \t" << s.substr( 0, j ) << endl;
				}
			dirs.insert(s);
			//cout << "\tInserting \t" << s<< endl;
		}
		REP( i, M )
		{
			cin >> s;
			if( dirs.find(s) != dirs.end() )	continue;
			for( j = 1; j < s.SZ; j++ )
				if( s[j] == '/' )
					if( dirs.find(s.substr( 0, j )) == dirs.end() )
					{
						dirs.insert(s.substr( 0, j ));
						//cout << "\tInserting \t" << s.substr( 0, j ) << endl;
						ans++;
					}
			dirs.insert(s);
			ans++;
		}
		cout << "Case #" << caseN << ": " << ans << endl;
		caseN++;
	}
}
