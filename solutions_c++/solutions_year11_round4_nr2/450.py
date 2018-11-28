#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define bublic public
#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz size()
#define For(i, st, en) for(int i=(st); i<=(int)(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define forn(i, n) for(int i=0; i<(int)(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)

template <class _T> inline _T sqr(const _T& x) { return x * x; }
template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }

typedef long double ld;

// Constants
const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-11;

// Types
typedef signed   long long i64;
typedef unsigned long long u64;
typedef set < int > SI;
typedef vector < ld > VD;
typedef vector < int > VI;
typedef vector < bool > VB;
typedef vector < string > VS;
typedef map < string, int > MSI;
typedef pair < int, int > PII;

int qq, n, m;
int a[512][512];
int ay[512][512];
int sx[512][512];
int sx2[512][512];
int sy[512][512];
int s[512][512];
int s2[512][512];
char ss[1024];
bool okx[512][512];
bool oky[512][512];

void check1(int a[][512], bool ok[][512], int sy[][512], int s[][512], int n, int m, int k)
{
	int mid = (k+1)/2;
	forn(i, n-k+1)
	{
		int wx = 0;
		For(j, 1, k)
		{
			wx += (j - mid) * (sy[i+k][j] - sy[i][j]);
		}
		For(j, k, m)
		{
			int xx = wx;
			xx -= (k-mid) * a[i+1][j];
			xx -= (k-mid) * a[i+k][j];
			xx -= (1-mid) * a[i+1][j-k+1];
			xx -= (1-mid) * a[i+k][j-k+1];
			ok[i][j-k] = !xx;
/*			if (k == 5 && i == 1 && j == k+1)
			{
				cerr << xx << " " << wx << endl;
//				cerr << s[i+k][j] - s[i][j] - s[i+k][j-k] + s[i][j-k] << endl;
//				cerr << (sy[i+k][j+1] - sy[i][j+1]) * (k - mid) << endl;
//				cerr << (sy[i+k][j-k+1] - sy[i][j-k+1]) * (k - mid + 1) << endl;
			}*/
			wx -= s[i+k][j] - s[i][j] - s[i+k][j-k] + s[i][j-k];
			wx += (sy[i+k][j+1] - sy[i][j+1]) * (k - mid);
			wx += (sy[i+k][j-k+1] - sy[i][j-k+1]) * (k - mid + 1);
		}
	}
}

void check2(int a[][512], bool ok[][512], int sy[][512], int s[][512], int n, int m, int k)
{
	int mid = k + 1;
	forn(i, n-k+1)
	{
		int wx = 0;
		For(j, 1, k)
		{
			wx += (j*2 - mid) * (sy[i+k][j] - sy[i][j]);
		}
		For(j, k, m)
		{
			int xx = wx;
			xx -= (k*2-mid) * a[i+1][j];
			xx -= (k*2-mid) * a[i+k][j];
			xx -= (1*2-mid) * a[i+1][j-k+1];
			xx -= (1*2-mid) * a[i+k][j-k+1];
			ok[i][j-k] = !xx;
/*			if (k == 4 && i == 1 && j == k+1)
			{
				cerr << xx << " " << wx << endl;
//				cerr << s[i+k][j] - s[i][j] - s[i+k][j-k] + s[i][j-k] << endl;
//				cerr << (sy[i+k][j+1] - sy[i][j+1]) * (k - mid) << endl;
//				cerr << (sy[i+k][j-k+1] - sy[i][j-k+1]) * (k - mid + 1) << endl;
			}*/
			wx -= (s[i+k][j] - s[i][j] - s[i+k][j-k] + s[i][j-k]) * 2;
			wx += (sy[i+k][j+1] - sy[i][j+1]) * (k*2 - mid);
			wx += (sy[i+k][j-k+1] - sy[i][j-k+1]) * (k*2 - mid + 1*2);
		}
	}
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	scanf("%d", &qq);
	forn(ii, qq)
	{
		printf("Case #%d: ", ii+1);
		fprintf(stderr, "Case #%d:\n", ii+1);
		
		scanf("%d%d%*d", &n, &m);
		clr(a);
		clr(sx);
		clr(sx2);
		clr(sy);
		clr(s);
		clr(ay);
		clr(s2);
		forn(i, n)
		{
			scanf("%s", ss);
			forn(j, m)
			{
				a[i+1][j+1] = ss[j] - '0';
			}
		}
		For(i, 1, n)
		{
			For(j, 1, m)
			{
				sx[i][j] = sx[i][j-1] + a[i][j];
				sy[i][j] = sy[i-1][j] + a[i][j];
				s[i][j] = s[i][j-1] + sy[i][j];
				ay[j][i] = a[i][j];
				s2[j][i] = s[i][j];
				sx2[j][i] = sx[i][j];
			}
		}

		int ans = -1;
		Ford(k, min(n, m), 3)
		{
			if (k % 2 == 1)
			{
				clr(okx);
				clr(oky);
				check1(a, okx, sy, s, n, m, k);
				check1(ay, oky, sx2, s2, m, n, k);
				forn(i, n-k+1)
				{
					forn(j, m-k+1)
					{
						if (okx[i][j] && oky[j][i])
						{
							cerr << "! " << i << " " << j << endl;
							ans = k;
							break;
						}
					}
					if (ans == k) break;
				}
				if (ans == k) break;
			}
			if (k % 2 == 0)
			{
				clr(okx);
				clr(oky);
				check2(a, okx, sy, s, n, m, k);
				check2(ay, oky, sx2, s2, m, n, k);
				forn(i, n-k+1)
				{
					forn(j, m-k+1)
					{
						if (okx[i][j] && oky[j][i])
						{
							cerr << "! " << i << " " << j << endl;
							ans = k;
							break;
						}
					}
					if (ans == k) break;
				}
				if (ans == k) break;
			}
		}
		if (ans == -1) puts("IMPOSSIBLE");
		else printf("%d\n", ans);

		fflush(stdout);
	}

	return 0;
}
