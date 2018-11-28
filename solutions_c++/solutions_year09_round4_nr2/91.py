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

int r[16][16][1<<8][1<<8];

priority_queue <pair <int, pair <PII, PII > > > q;

void go (int x, int y, int k1, int k2, int rr, bool qq)
{
	if (r[x][y][k1][k2]<=rr)
		return;
	r[x][y][k1][k2] = rr;
	if (qq)
	{
		q.push (make_pair(-rr, make_pair(PII(x,y), PII(k1, k2))));
	}
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w+", stdout);

    int tt;
    cin >> tt;

    REP (t, tt)
    {
    	cout << "Case #" << t+1 << ": ";
    	int n, m, f;
    	cin >> n >> m >> f;

    	int res = INF;

    	vector <string> a(n);
    	REP (i, n)
			cin >> a[i];

    	REP (i, n)
			REP (j, m)
				REP (k, 1<<m)
					REP (l, 1<<m)
						r[i][j][k][l] = INF;

    	r[0][0][0][0] = 0;


    	REP (i, n-1)
    	{
			REP (j, m)
				REP (k1, 1<<m)
					if (r[i][j][k1][0]<INF)
					{
						//cout << i << " " << j << " " << k1 << " " <<r[i][j][k1][0] << endl;
						q.push (make_pair(-r[i][j][k1][0], make_pair(PII (i, j), PII (k1, 0))));
					}

			while (!q.empty())
			{
				int rr = -q.top().X;
				int x = q.top().Y.X.X;
				int y = q.top().Y.X.Y;
				int k1 = q.top().Y.Y.X;
				int k2 = q.top().Y.Y.Y;
				q.pop();

				if (r[x][y][k1][k2]<rr)
					continue;

				if (a[x+1][y]=='.' || (k2&(1<<y)))
				{
					int xx = x+1;
					while (xx<n-1 && a[xx+1][y]=='.')
						xx++;
					if (xx-x<=f)
					{
						if (xx-x==1)
						{
							//if (xx==2 && y==2 && k2 == 12 && rr==4)
							//							{
							//								cout << "from1 " << x << " " << y << " " << k1 << " " << k2 << " " << rr << endl;
							//							}
							go (xx, y, k2, 0, rr, false);
						}
						else
						{
							go (xx, y, 0, 0, rr, false);

							//if (xx==n-1)
							//{
							//	cout << "from " << x << " " << y << " " << k1 << " " << k2 << " " << rr << endl;
							//}/
						}
					}

					continue;
				}

				if (y && (a[x][y-1]=='.' || (k1 & (1<<(y-1)))))
					go (x, y-1, k1, k2, rr, true);
				if (y<(m-1) && (a[x][y+1]=='.' || (k1 & (1<<(y+1)))))
					go (x, y+1, k1, k2, rr, true);
				if (y && (a[x][y-1]=='.' || (k1 & (1<<(y-1)))))
					go (x, y, k1, k2|(1<<(y-1)), rr+1, true);
				if (y<(m-1)&& (a[x][y+1]=='.' || (k1 & (1<<(y+1)))))
					go (x, y, k1, k2|(1<<(y+1)), rr+1, true);


			}
    	}

    	REP (j, m)
			REP (k1, 1<<m)
				REP (k2, 1<<m)
					res <?= r[n-1][j][k1][k2];

    	if (res < INF)
			cout << "Yes " << res << endl;
    	else
    		cout << "No" << endl;
    }

    return 0;
}

