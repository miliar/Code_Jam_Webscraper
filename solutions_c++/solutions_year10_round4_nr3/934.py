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

int tcase,R,x11,x22,y11,y22;
bool d[110][110];

int main()
{
	getInt(tcase);
	FOR(t,1,tcase)
	{
		RESET(d,false);
		cout << "Case #" << t << ": ";
		getInt(R);
		bool ok = false;
		REP(i,R)
		{
			cin >> x11 >> y11 >> x22 >> y22;
			FOR(j,x11,x22)FOR(k,y11,y22)
			{
				d[j][k] = true;
				ok = true;
			}
		}
		int T = 0;
		bool temp[110][110];
		while(ok)
		{
			T++;
			ok = false;
			REP(i,110)REP(j,110)
			{
				int hasNorth = false;
				int hasWest = false;
				if(i-1 > 0 && d[i-1][j])hasNorth = true;
				if(j-1 > 0 && d[i][j-1])hasWest = true;
				if(d[i][j])
				{
					if(hasNorth || hasWest)temp[i][j] = true;
						else temp[i][j] = false;
				}
				else
				{
					if(hasNorth && hasWest)temp[i][j] = true;
						else temp[i][j] = false;
				}
				if(temp[i][j])ok = true;
			}
			REP(i,110)
			{
				REP(j,110)
				{
					d[i][j] = temp[i][j];
				}
			}
		}
		cout << T << endl;
	}
	return 0;
}
