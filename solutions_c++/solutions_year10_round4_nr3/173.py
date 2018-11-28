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

int v[MAX][MAX];

int main()
{
	stdin = freopen("c.in","r",stdin);
	stdout = freopen("c.out","w",stdout);
	int totalCasos;
	cin >> totalCasos;
	forn(caso,totalCasos)
	{
		int R; cin >> R;
		zMem(v);
		forn(i,R)
		{
			int x1,y1,x2,y2;
			cin >> x1 >> y1 >> x2 >> y2;
			x2++; y2++;
			forsn(x,x1,x2)
			forsn(y,y1,y2)
				v[x][y] = 1;
		}
		int res = -1;
		bool hay = true;
		while (hay)
		{
			res++; hay = false;
			dforn(i,MAX)
			dforn(j,MAX)
			if (v[i][j])
			{
				hay = true;
				v[i][j] = v[i-1][j] || v[i][j-1];
			}
			else v[i][j] = v[i-1][j] && v[i][j-1];
		}
		cout << "Case #" << caso + 1 << ": " << res << endl;
		cerr << "Case #" << caso + 1 << ": " << res << endl;
	}
	return 0;
}
