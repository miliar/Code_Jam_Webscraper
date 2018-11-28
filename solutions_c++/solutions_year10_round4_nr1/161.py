#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <numeric>
#include <functional>
#include <algorithm>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)
#define dforsn(i,s,n) for(int i=(n)-1;i>=(int)(s);i--)

#define forall(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define dforall(i,c) for(typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)
#define all(c) (c).begin(),(c).end()

#define DBG(x) cerr << #x << " = " << (x) << endl

#define esta(x,c) ((c).find(x) != (c).end())
#define zMem(c) memset((c),0,sizeof(c))

typedef long long tint;
typedef long double tdbl;

typedef pair<int,int> pint;
typedef pair<tint,tint> ptint;

typedef vector<int> vint;
typedef vector<vint> vvint;
typedef vector<string> vstr;

#define INF 1000000000

#define MAX 128

int v[MAX][MAX],k;

bool anda(int t)
{
	int tope = t-k+1;
	forn(x,tope)
	forn(y,tope)
	{
		bool anda = true;
		forn(i,k)
		forn(j,k)
		#define ANDA(a,b) (a < 0 || a >= k || b < 0 || b >= k || v[i][j] == v[a][b])
		if (!(	(ANDA(y+j-x,x+i-y)) 
				&& 
				(ANDA(t-1-(y+j)-x,t-1-(x+i)-y))
			))
			{
				anda = false;
				goto fuera;
			}
fuera:
		if (anda) return true;
	}
	return false;
}

int main()
{
	stdin = freopen("a.in","r",stdin);
	stdout = freopen("a.out","w",stdout);
	int totalCasos;
	cin >> totalCasos;
	forn(caso,totalCasos)
	{
		cin >> k;
		int x = 0,y=k-1,co = 0;
		forn(i,2*k)
		forn(j,k - abs(k-i))
		{
			cin >> v[x][y];
			x++;y++;
			if (x >= k || y >= k)
			{
				co++;
				x = max(0,co-k+1);
				y = max(0,k-co-1);
			}
		}
		int res = k;
		while (!anda(res)) res++;
		res = res*res-k*k;
		cout << "Case #" << caso + 1 << ": " << res << endl;
		cerr << "Case #" << caso + 1 << ": " << res << endl;
	}
	return 0;
}
