#include <vector>
#include <algorithm>
#include <math.h>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <utility>
#include <numeric>
#include <fstream>

using namespace std;

#define		ALL(c)	(c).begin(),(c).end()
#define		SZ(c)	int((c).size())
#define		LEN(s)	int((s).length())
#define		FOR(i,n)	for(int i=0;i<(n);++i)
#define		FORD(i,a,b)	for(int i=(a);i<=(b);++i)
#define		FORR(i,a,b)	for(int i=(b);i>=(a);--i)
#define		MP	make_pair
#define		PB	push_back

typedef istringstream iss;
typedef ostringstream oss;
typedef long double ld;
typedef long long i64;
typedef pair<int,int> pii;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<vvvi> vvvvi;

int ddi[4] = { 0, -1,  1,  0};
int ddj[4] = { 1,  0,  0, -1};

int main()
{
	ifstream fin("C.in"); ofstream fout("C.out");
	int T;
	fin >> T;
	FOR(tt, T)
	{
		int W, Q;
		fin >> W >> Q;

		vector<string> A(W);
		FOR(i, W) fin >> A[i];

		int pls = (A[0][0] == '+' || A[0][0] == '-') ? 1 : 0;

		fout << "Case #" << tt+1 << ":" << endl;
		cout << "Case #" << tt+1 << ":" << endl;

		vi queries(Q), RQ(Q);
		vector<string> ans(Q, "zzz");
		FOR(i, Q) RQ[i] = i;

		FOR(i, Q)
			fin >> queries[i];

		vvvi f(600, vvi(W, vi(W, 0)));
		vvvi p(600, vvi(W, vi(W, 0)));
		vector<vector<vector<string> > > g(600, vector<vector<string> >(W, vector<string>(W,string())));
		FOR(i, W) FOR(j, W) if ((i+j+pls)%2==0) 
		{
			f[A[i][j]-'0'+300][i][j] = 1;
			p[A[i][j]-'0'+300][i][j] = -1;
			g[A[i][j]-'0'+300][i][j] = A[i][j];
			FOR(kiq, SZ(RQ))
			{
				int M = queries[RQ[kiq]];
				if (f[M+300][i][j] == 1)
					ans[RQ[kiq]] = min(ans[RQ[kiq]], g[M+300][i][j]);
			}
		}

		FOR(kiq, SZ(RQ))
		{
			if (ans[RQ[kiq]] != "zzz")
			{
				RQ[kiq] = RQ.back();
				RQ.pop_back();
				--kiq;
			}
		}

		while (!RQ.empty())
		{
			vvvi d = f;
			vector<vector<vector<string> > > pg = g;
			f.assign(600, vvi(W, vi(W, 0)));
			g.assign(600, vector<vector<string> >(W, vector<string>(W,string())));

			FOR(i, W) FOR(j, W)
			{
				if ((i+j+pls)&1) continue;

				FORD(s, 30, 570)
				{
					int bk = -1;
					FOR(k, 4) FOR(kk, 4)
					{
						int ii = i + ddi[k];
						int jj = j + ddj[k];
						if (ii < 0 || ii >= W || jj < 0 || jj >= W) continue;

						int ss = s;
						if (A[ii][jj] == '+') 
							ss -= A[i][j]-'0';
						else
							ss += A[i][j]-'0';

						int iii = ii + ddi[kk];
						int jjj = jj + ddj[kk];
						if (iii < 0 || iii >= W || jjj < 0 || jjj >= W) continue;
						if (d[ss][iii][jjj] == 0) continue;

						string ns = (pg[ss][iii][jjj] + A[ii][jj]) + A[i][j];

						if (bk == -1 || ns < g[s][i][j])
						{
							bk = k;
							f[s][i][j] = 1;
							p[s][i][j] = k;
							g[s][i][j] = ns;
						}
					}
				}

				FOR(kiq, SZ(RQ))
				{
					int M = queries[RQ[kiq]];
					if (f[M+300][i][j] == 1)
						ans[RQ[kiq]] = min(ans[RQ[kiq]], g[M+300][i][j]);
				}
			}

			FOR(kiq, SZ(RQ))
			{
				if (ans[RQ[kiq]] != "zzz")
				{
					RQ[kiq] = RQ.back();
					RQ.pop_back();
					--kiq;
				}
			}
		}

		FOR(i, Q)
		{
			fout << ans[i] << endl;
			cout << ans[i] << endl;
		}
	}
	return 0;	
}
