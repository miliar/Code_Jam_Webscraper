#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

map <VPII, int> r;
map <VPII, bool> type;

queue <VPII> q;

vector <string> a;

bool check (VPII a)
{
	if (type.find (a)!=type.end())
		return type[a];

	int n = a.size ();
	VI u (n);
	u[0] = 1;

	REP (t, n)
		REP (i, n)
			if (u[i] == 1)
			{
				u[i] = 2;
				REP (j, n)
					if (!u[j] && abs(a[i].X-a[j].X) + abs (a[i].Y - a[j].Y) == 1)
						u[j] = 1;
			}

	bool res = true;

	REP (i, n)
		if (!u[i])
			res = false;

	type[a] = res;

	return res;
}

void go (VPII a, int v, bool from)
{
	int n = a.size ();
	UNIQUE(a);
	if (a.size ()!=n)
		return;

	if (r.find (a)!=r.end())
		return;

	if (!from && !check(a))
		return;

	r[a] = v;

	q.push (a);
}

VPII d;

int main()
{
	d.pb (PII (1, 0));
	d.pb (PII (-1, 0));
	d.pb (PII (0, 1));
	d.pb (PII (0, -1));

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w+", stdout);

    int tt;
    cin >> tt;
    REP (t, tt)
    {

    	r = map <VPII, int> ();
    	type = map <VPII, bool> ();
    	cout << "Case #" << t+1 << ": ";

    	int n, m;
    	cin >> n >> m;
    	a.resize (n);
    	REP (i, n)
			cin >> a[i];

    	VPII r1, r2;

    	q = queue <VPII>();

    	REP (i, n)
			REP (j, m)
			{
				if (a[i][j] == 'x' || a[i][j] == 'w')
					r2.pb (PII (i, j));
				if (a[i][j] == 'o' || a[i][j] == 'w')
					r1.pb (PII (i, j));
			}

    	go (r1, 0, false);

    	while (!q.empty())
    	{
    		VPII b = q.front();
    		/*REP (i, b.size ())
    		{
    			cout << b[i].X << " " << b[i].Y << ",    ";
    		}
    		cout << r[b]+1 << endl;*/
    		q.pop();
    		int v = r[b]+1;
    		bool from = check (b);

    		if (b == r2)
    		{
    			cout << r[b] << endl;
    			goto next;
    		}

    		REP (i, b.size ())
    		{
    			REP (j, 4)
    			{
    				int x = b[i].X - d[j].X;
    				int y = b[i].Y - d[j].Y;

    				if (x<0 || x>=n || y<0 || y>=m)
    					continue;
    				if (a[x][y]=='#')
    					continue;

    				REP (k, b.size ())
						if (b[k].X == x && b[k].Y == y)
							goto next2;

    				b[i].X += d[j].X;
    				b[i].Y += d[j].Y;


    				if (b[i].X >=0 && b[i].X<n && b[i].Y >= 0 && b[i].Y <m)
    					if (a[b[i].X][b[i].Y]!='#')
    						go (b, v, from);

    				b[i].X -= d[j].X;
    				b[i].Y -= d[j].Y;

    				next2:;
    			}
    		}
    	}

    	cout << -1 << endl;
    	next:;
    }



    return 0;
}
