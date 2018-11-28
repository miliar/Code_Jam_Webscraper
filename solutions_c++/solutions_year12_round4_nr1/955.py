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
#define FOREACH(it,c) for (__typeof ((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define RESET(A,v) memset(A, v, sizeof(A))
#define DEBUG(x) cout << #x << " = " << x << endl;

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

int tcase,N,D;
ll d[10010],l[10010];
ll ok[10010];
bool cinta;

int main()
{
	getInt(tcase);
	FOR(t,1,tcase)
	{
		cin >> N;
		REP(i,N)cin >> d[i] >> l[i];
		cin >> D;
		RESET(ok,-1);
		cinta = false;
		ok[0] = d[0];
		REP(i,N)FOR(j,i+1,N-1)
		{
			if(ok[i] != -1 && d[j]-d[i] <= ok[i])
			{
				ll temp = MIN(d[j]-d[i],l[j]);
				ok[j] = ok[j] == -1 ? temp : MAX(ok[j],temp);
			}
		}
		REP(i,N)if(ok[i] != -1 && D-d[i] <= ok[i])cinta = true;
		cout << "Case #" << t << ": " << (cinta ? "YES" : "NO") << endl ;
	}
	return 0;
}
