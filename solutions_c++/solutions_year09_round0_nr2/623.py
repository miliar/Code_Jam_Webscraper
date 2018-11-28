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

typedef istringstream iss;
typedef ostringstream oss;
typedef long double ld;
typedef long long i64;
typedef pair<int,int> pii;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<vvvi> vvvvi;

int ddi[4] = {-1,  0,  0,  1};
int ddj[4] = { 0, -1,  1,  0};

int main()
{
	ifstream fin("b.in"); ofstream fout("b.out");
	int T;
	fin >> T;
	FOR(tt, T)
	{
		int H, W;
		fin >> H >> W;

		vvi M(H, vi(W));
		FOR(i, H) FOR(j, W) fin >> M[i][j];

		vector<pair<int,pii> > A;
		FOR(i, H) FOR(j, W) A.push_back(make_pair(M[i][j],pii(i,j)));
		sort(A.rbegin(), A.rend());

		vvi U(H, vi(W, 0));
		int mark = 0;
		FOR(k, SZ(A))
		{
			int ii = A[k].second.first;
			int jj = A[k].second.second;
			if (U[ii][jj] > 0) continue;
			++mark;
			U[ii][jj] = mark;
			vector<pii> wfp;
			wfp.push_back(pii(ii,jj));
			while (1)
			{
				int bi = ii, bj = jj;
				FOR(s, 4)
				{
					int ni = ii + ddi[s];
					int nj = jj + ddj[s];
					if (ni < 0 || ni >= H || nj < 0 || nj >= W) continue;
					if (M[ni][nj] < M[bi][bj]) bi = ni, bj = nj;
				}
				if (bi == ii && bj == jj) break;
				if (U[bi][bj] > 0)
				{
					FOR(s, SZ(wfp)) U[wfp[s].first][wfp[s].second] = U[bi][bj];
					break;
				}
				ii = bi, jj = bj;
				U[ii][jj] = mark;
				wfp.push_back(pii(ii,jj));
			}
		}

		fout << "Case #" << tt+1 << ":" << endl;
		cout << "Case #" << tt+1 << ":" << endl;
		vector<char> mrk(20000, '#');
		char ch = 'a';
		FOR(i, H) 
		{
			FOR(j, W)
			{
				if (mrk[U[i][j]] == '#') mrk[U[i][j]] = ch++;
				if (j > 0) fout << ' ';
				fout << mrk[U[i][j]];
				if (j > 0) cout << ' ';
				cout << mrk[U[i][j]];
			}
			fout << endl;
			cout << endl;
		}
	}
	return 0;	
}
