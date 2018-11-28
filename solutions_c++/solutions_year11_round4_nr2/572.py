// GCJ 2011 R2
// wookayin

#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>

#define problem "B"

static int __threads = 4, __threadId = 0;

#define infile "input.txt"
#define outfile "output.txt"

#define REP(i, n) for(int i=0; i<(int)(n); ++i)
#define all(x) (x).begin(), (x).end()
using namespace std;

int n, m, D;

vector< vector<long long> > a;

long long s[501][501];
long long  px[501][501];
long long py[501][501];

inline long long getSum(int i, int j, int k, long long D[501][501])
{
	long long x = D[i+k-1][j+k-1] - (j>=1 ? D[i+k-1][j-1] : 0) - (i>=1 ? D[i-1][j+k-1] : 0) + (i>=1 && j>=1 ? D[i-1][j-1] : 0);
	return x;

}

pair<long long, long long> getS(int i, int j, int k)
{
	long long x = 0;
	long long y = 0;

	int i2 = i+k-1, j2 = j+k-1;
	x = getSum(i, j, k, px);
	y = getSum(i, j, k, py);

#define E(t) (2*t+1)
	x -= a[i][j] * E(i);	y -= a[i][j] * E(j); 
	x -= a[i2][j] * E(i2);	y -= a[i2][j] * E(j); 
	x -= a[i][j2] * E(i);	y -= a[i][j2] * E(j2); 
	x -= a[i2][j2] * E(i2);	y -= a[i2][j2] * E(j2); 
	return make_pair(x, y);

}
bool same(double x, double y)
{
	x -= y;
	const double EPS = 1e-9;
	return -EPS <= x && x <= EPS;
}
int go()
{
	REP(i, n) REP(j, m)
	{
		s[i][j] = (i>=1 ? s[i-1][j] : 0) + (j >= 1 ? s[i][j-1] : 0) - (i >= 1 && j >= 1 ? s[i-1][j-1] : 0) + a[i][j];
		px[i][j] = (i>=1 ? px[i-1][j] : 0) + (j >= 1 ? px[i][j-1] : 0) - (i >= 1 && j >= 1 ? px[i-1][j-1] : 0) + a[i][j] * (2*i+1);
		py[i][j] = (i>=1 ? py[i-1][j] : 0) + (j >= 1 ? py[i][j-1] : 0) - (i >= 1 && j >= 1 ? py[i-1][j-1] : 0) + a[i][j] * (2*j+1);
	}
		
	int st = min(n, m);

	for(int K = st ; K >= 3; K --)
	{
		for(int i = 0; i <= n - K; ++ i)
		{
			for(int j = 0; j <= m - K; ++ j)
			{
//#define BRUTE
#if 0
				double sx = 0, sy = 0;
				int w = 0;
				int c = 0;
				for(int x = i; x <= i+K-1; ++ x)
				{
					for(int y = j; y <= j+K-1; ++ y)
					{
						if(x == i && y == j) continue;
						if(x == i && y == j+K-1) continue;
						if(x == i+K-1 && y == j) continue;
						if(x == i+K-1 && y == j+K-1) continue;
						sx += a[x][y] * (x + 0.5); 
						sy += a[x][y] * (y + 0.5);
						w += a[x][y];
						c ++;
					}
				}
				sx /= w;
				sy /= w;
				if(same(sx, (i + 0.5 + (i+K-1) + 0.5)/2) && same(sy , (j + 0.5 + (j+K-1) + 0.5)/2) )
					return K;
#else

				// get center
				long long w = getSum(i, j, K, s);
				int i2 = i+K-1, j2 = j+K-1;
				w -= a[i][j];
				w -= a[i][j2];
				w -= a[i2][j];
				w -= a[i2][j2];
				int items = K*K - 2;
				pair<long long, long long> t =getS(i, j, K); 

				//if(t.first == (i+i2)/2 *  items)
				if(t.first * 2 == (E(i)+E(i2)) *  w &&
					t.second * 2 == (E(j)+E(j2)) *  w )
				{
//					printf("%d %d %d\n", i, j, K);
					return K;
				}
#endif

			}
		}
	}
	return -1;
}

int main(int argc, char *argv[])
{
	if(argc == 2) __threadId = atoi(argv[1]);
	else __threads = 1;

	freopen(infile, "r", stdin);
	freopen(outfile, "w", stdout);

	int T;
	scanf("%d", &T);
	for(int tt=1; tt<=T; ++tt) if(tt % __threads == __threadId)
	{
		fprintf(stderr, "%d/%d\n", tt, T);
		scanf("%d %d %d", &n, &m, &D);
		a.clear();
		a.resize(n, vector<long long>(m, 0) );

		REP(i, n) {
			char buf[512];
			scanf("%s", buf);
			REP(j, m) a[i][j] =  D + (buf[j] - '0');
		}

		printf("Case #%d: ", tt);
		int ans = go();
		if(ans >= 0) printf("%d\n", ans);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}