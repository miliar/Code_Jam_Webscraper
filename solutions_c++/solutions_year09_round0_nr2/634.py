#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <complex>
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
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
int GG[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w+", stdout);
	int t;
	cin >> t;
	FOR(it,1,t+1)
	{
		int h, w;
		cin >> h >> w;
		VVI M(h,VI(w));
		REP(i,h)
			REP(j,w)
			{
				cin >> M[i][j];
			}
		VI C(h*w);
		REP(i,SZ(C))
			C[i] = i;
		VI Ma(h*w, 1);
		REP(i,h)
			REP(j,w)
			{
				PII goTo;
				int minVal = M[i][j];
				REP(k,4)
				{
					int ni = i+GG[k][0];
					int nj = j+GG[k][1];
					if (0 <= ni && ni < h && 0 <= nj && nj < w)
					{
						if (minVal > M[ni][nj])
						{
							minVal = M[ni][nj];
							goTo.X = ni;
							goTo.Y = nj;
						}
					}
				}
				if (minVal != M[i][j])
				{
					int iX = w*i+j;
					int iY = w*goTo.X+goTo.Y;
					while (C[iX] != iX)
						iX = C[iX];
					while (C[iY] != iY)
						iY = C[iY];
					if (Ma[iX] > Ma[iY])
						swap(iX, iY);
					Ma[iY] += Ma[iX];
					C[iX] = iY;
				}
			}
		cout << "Case #" << it << ":" << endl;
		map<int, int> so;
		REP(i,SZ(C))
		{
			int iX = C[i];
			while (iX != C[iX])
				iX = C[iX];
			if (so.find(iX) == so.end())
			{
				int si = SZ(so);
				so[iX] = si;
			}
			cout << char('a'+so[iX]);
			if ((i+1)%w == 0)
				cout << endl;
			else
				cout << ' ';
		}
	}
}
