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

int tcase,R,C;
char conf[50][50];
int c[50][50];

int main()
{
	getInt(tcase);
	FOR(t,1,tcase)
	{
		cin >> R >> C;
		memset(c,0,sizeof(c));
		REP(i,R)REP(j,C)
		{
			cin >> conf[i][j];
			if(conf[i][j] == '#')c[i][j] = 1;
				else c[i][j] = 0;
		}
		int prev[50];
		memset(prev,0,sizeof(prev));
		bool ok = true;
		REP(i,R)
		{
			int now[50];
			memset(now,0,sizeof(now));
			REP(j,C)
			{
				if(prev[j] && !c[i][j])ok = false;
			}
			REP(j,C)
			{
				if(prev[j] && c[i][j])continue;
				int s = j;
				while(s < C && !prev[s] && c[i][s])
				{
					now[s] = 1;
					s++;
				}
				if(s != j && i == R-1)ok = false;
				if((s-j)%2 != 0)ok = false;
				j = s;
			}
			REP(j,C)prev[j] = now[j];
		}
		cout << "Case #" << t << ": " << endl;
		if(!ok)puts("Impossible");
			else
			{
				int vis[50][50];
				memset(vis,0,sizeof(vis));
				REP(i,R)REP(j,C)
				{
					if(!vis[i][j] && c[i][j])
					{
						vis[i][j] = 1;
						vis[i][j+1] = 2;
						vis[i+1][j] = 3;
						vis[i+1][j+1] = 4;
					}
				}
				REP(i,R)
				{
					REP(j,C)
					{
						if(!c[i][j])cout << '.';
							else if(vis[i][j] == 1)cout << '/';
							else if(vis[i][j] == 2)cout << '\\';
							else if(vis[i][j] == 3)cout << '\\';
							else cout << '/';
					}
					cout << endl;
				}
			}
	}
	return 0;
}
