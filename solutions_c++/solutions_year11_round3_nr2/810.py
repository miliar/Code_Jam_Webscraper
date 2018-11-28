#include <iostream>
#include <cstdio>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <cmath>
#include <cstdlib>

//Hendri's Template
#define REP(i, n) for(int i = 0, _n = (n); i < _n; i++)
#define FOR(i, a, b) for(int i = (a), _b = (b); i <= _b; i++)
#define FORD(i, a, b) for(int i = (a), _b = (b); i >= _b; i--)
#define RESET(A,v) memset(A, v, sizeof(A))

#define MP make_pair
#define PB push_back
#define F first
#define S second

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

template<class T> inline T MIN(T a, T b){return a < b?a:b;}
template<class T> inline T MAX(T a, T b){return a > b?a:b;}

template<class T> inline void getInt(T& x)
{
	char c;
	int mul = 1;
	while((c = getchar()) != EOF)
	{
		if(c == '-')mul = -1;
		if(c >= '0' && c <= '9')
		{
			x = c-'0';
			break;
		}
	}
	if(c == EOF){x = EOF;return;}
	while(c = getchar())
	{
		if(c >= '0' && c <= '9')
		{
			x = (x<<1)+(x<<3)+(c-'0');
		}
		else break;
	}
	x *= mul;
}
//End of Hendri's Template

int tcase,N,L,C;
ll t;
int a[1000];
int dis[1000];
ll dp[1010][3];
int tot[1000];

int main()
{
	getInt(tcase);
	FOR(tt,1,tcase)
	{
		cout << "Case #" << tt << ": ";
		cin >> L >> t >> N >> C;
		REP(i,C)
		{
			cin >> a[i];
		}
		memset(tot,0,sizeof(tot));
		REP(i,N)
		{
			dis[i] = a[i%C];
			if(i == 0)tot[i] = dis[i];
				else tot[i] = tot[i-1]+dis[i];
		}
		memset(dp,0,sizeof(dp));
		FOR(i,1,N)
		{
			REP(j,L+1)
			{
				dp[i][j] = dp[i-1][j]+2*dis[i-1];
				if(j > 0)
				{
					ll xx;
					if(i > 1)
					{
						xx = MAX(0ll,t-tot[i-2]*2);
					}
					else
					{
						xx = t;
					}
					dp[i][j] = MIN(dp[i][j],dp[i-1][j-1]+xx+(dis[i-1]-xx/2));
				}
			}
			//cout << i << " " << L << " " << dp[i][L] << endl;
		}
		cout << dp[N][L] << endl;
	}
	return 0;
}
