#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <numeric>
#include <functional>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)
#define dforsn(i,s,n) for(int i=(n)-1;i>=(int)(s);i--)

#define DBG(x) cerr << #x << " = " << (x) << endl
#define RAYA cerr << "================" << endl

#define forall(it,c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)

#define all(c) (c).begin(),(c).end()

typedef long long tint;
typedef long double tdbl;
typedef pair<int,int> Pint;
typedef vector<int> vint;

typedef pair<int,int> Par;

const int MAX = 1024;

tint xAc[MAX][MAX], yAc[MAX][MAX], mAc[MAX][MAX];

tint v[MAX][MAX];

int main()
{
	freopen("entrada.in","r",stdin);
	freopen("salida.out","w",stdout);
	int TT; cin >> TT;
	forn(tt,TT)
	{
		int R,C,D; cin >> R >> C >> D;
		forn(i,R)
		forn(j,C)
		{
			char c; cin >> c;
			v[i][j] = c - '0';
		}
		forn(k,MAX)
			xAc[k][0] = xAc[0][k] =
			yAc[k][0] = yAc[0][k] =
			mAc[k][0] = mAc[0][k] = 0;
		forsn(i,1,R+1)
		forsn(j,1,C+1)
		{
			xAc[i][j] = xAc[i-1][j] + xAc[i][j-1] - xAc[i-1][j-1] + (2*i-1) * v[i-1][j-1];
			yAc[i][j] = yAc[i-1][j] + yAc[i][j-1] - yAc[i-1][j-1] + (2*j-1) * v[i-1][j-1];
			mAc[i][j] = mAc[i-1][j] + mAc[i][j-1] - mAc[i-1][j-1] + v[i-1][j-1];
		}
		int res = -1;
		dforsn(K,3,R+1)
		{
			bool funca = false;
			forn(x,R-K+1)
			forn(y,C-K+1)
			{
				tint M = mAc[x+K][y+K] - mAc[x][y+K] - mAc[x+K][y] + mAc[x][y];
				tint X = xAc[x+K][y+K] - xAc[x][y+K] - xAc[x+K][y] + xAc[x][y];
				tint Y = yAc[x+K][y+K] - yAc[x][y+K] - yAc[x+K][y] + yAc[x][y];
				X -= (2*x+1) * (v[x][y] + v[x][y+K-1]) + (2*(x+K-1)+1) * (v[x+K-1][y] + v[x+K-1][y+K-1]);
				Y -= (2*y+1) * (v[x][y] + v[x+K-1][y]) + (2*(y+K-1)+1) * (v[x][y+K-1] + v[x+K-1][y+K-1]);
				M -= v[x][y] + v[x+K-1][y] + v[x][y+K-1] + v[x+K-1][y+K-1];
				if (M * tint(2*x + K) == X &&
					M * tint(2*y + K) == Y)
				{
					funca = true;
					goto ajuira;
				}
			}
ajuira:;
			if (funca)
			{
				res = K;
				break;
			}
		}
		if (res == -1)
			cout << "Case #" << tt+1 << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << tt+1 << ": " << res << endl;
		if (res == -1)
			cerr << "Case #" << tt+1 << ": " << "IMPOSSIBLE" << endl;
		else
			cerr << "Case #" << tt+1 << ": " << res << endl;
	}
	return 0;
}
