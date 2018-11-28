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

int tcase,N;

int main()
{
	getInt(tcase);
	FOR(t,1,tcase)
	{
		getInt(N);
		cout << "Case #" << t << ": ";
		char c;
		int x,globaltime = 0;
		int ans = 0;
		int posO = 1,posB = 1,tO = 0, tB = 0;
		REP(i,N)
		{
			cin >> c >> x;
			if(c == 'O')
			{
				tO = MAX(ans+1,tO+abs(posO-x)+1);
				posO = x;
				ans = MAX(tO,tB);
			}
			else
			{
				tB = MAX(ans+1,tB+abs(posB-x)+1);
				posB = x;
				ans = MAX(tO,tB);
			}
		}
		cout << ans << endl;
	}
	return 0;
}
