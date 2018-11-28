#include <vector>
#include <algorithm>
#include <cmath>
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

typedef vector<ld> vd;
typedef vector<vd> vvd;

typedef vector<string> vs;

const i64 d18 = 1000000000000000000LL;
const ld eps = 1e-9;
const ld pi = atan2(0.0, -1.0);
template<class T> T sqr(T a) { return a * a; }
i64 abs(i64 a) { return (a >= 0) ? a : -a; }

ofstream LOG("log.txt");

ifstream fin;
ofstream fout;

int ddi[4] = {0,  0, 1, -1};
int ddj[4] = {1, -1, 0,  0};

int CanMove(vvi & C, vvi & F, int i1, int j1, int i2, int j2, int H)
{
	if (C[i2][j2] - H < 50 || C[i2][j2] - F[i2][j2] < 50) return -1;
	if (C[i2][j2] - F[i1][j1] < 50 || C[i1][j1] - F[i2][j2] < 50) return -1;
	if (H - F[i1][j1] >= 20) return 1;
	return 10;
}

void solve_case(int TN)
{
	int H, n, m;
	fin >> H >> n >> m;
	vvi F(n, m), C(n, m);
	FOR(i, n) FOR(j, m) fin >> C[i][j];
	FOR(i, n) FOR(j, m) fin >> F[i][j];

	vector<pii> Q;
	vvi W(n, vi(m, 0));
	W[0][0] = 1;
	Q.push_back(pii(0,0));
	for (int k = 0; k < SZ(Q); ++k)
	{
		int ii = Q[k].first;
		int jj = Q[k].second;
		if (ii == n-1 && jj == m-1)
		{
			Q.clear();
			break;
		}
		FOR(d, 4)
		{
			int ni = ii + ddi[d];
			int nj = jj + ddj[d];
			if (ni < 0 || ni >= n || nj < 0 || nj >= m) continue;
			if (W[ni][nj]) continue;
			if (CanMove(C, F, ii, jj, ni, nj, H) == -1) continue;
			Q.push_back(pii(ni, nj));
			W[ni][nj] = 1;
		}
	}

	if (Q.empty())
	{
		fout << "Case #" << TN << ": 0.0\n";
		cout << "Case #" << TN << ": 0.0\n";
		return;
	}

	int ans = 0;
	set<pair<int,pii> > V;
	set<pii> WW;
	FOR(i, SZ(Q)) V.insert(make_pair(0,Q[i]));
	while (!V.empty())
	{
		pii p = V.begin()->second;
		int t = V.begin()->first;
		if (p == pii(n-1,m-1))
		{
			ans = t;
			break;
		}
		int curH = max(0, H - t);
		V.erase(V.begin());
		if (curH > 0) 
			V.insert(make_pair(t+1,p));
		FOR(d, 4)
		{
			int ni = p.first + ddi[d];
			int nj = p.second + ddj[d];
			if (ni < 0 || ni >= n || nj < 0 || nj >= m) continue;
			int mv = CanMove(C, F, p.first, p.second, ni, nj, curH);
			if (mv == -1) continue;
			if (curH == 0 && WW.count(pii(ni,nj))) continue;
			V.insert(make_pair(t+mv*10,pii(ni,nj)));
			if (curH == 0) WW.insert(pii(ni,nj));
		}
	}

	fout << fixed << setprecision(2) << "Case #" << TN << ": " << 0.1 * ans << endl;
	cout << fixed << setprecision(2) << "Case #" << TN << ": " << 0.1 * ans << endl;
}

int main()
{
	fin.open("B.in"); 
	fout.open("B.out");

	int T; 
	fin >> T;
	FOR(tt, T)
	{
		solve_case(tt+1);
	}

	return 0;	
}
