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

struct vrtx
{
	vector<pii> b;
	int dst;

	vrtx() {}
	vrtx(vector<pii>& _b): b(_b) {}

	bool operator<(const vrtx& r)
	{
		FOR(i, SZ(b))
		{
			if (b[i] < r.b[i]) return true;
			if (b[i] > r.b[i]) return false;
		}
		return false;
	}

	bool operator==(const vrtx& r)
	{
		FOR(i, SZ(b)) if (b[i] != r.b[i]) return false;
		return true;
	}
};

int R, C;
set<vector<pii> > W;
vector<string> A, B, D;

bool isfin(vrtx& v)
{
	FOR(i, SZ(v.b)) 
		if (A[v.b[i].first][v.b[i].second] != 'x') 
			return false;
	return true;
}

int dist(pii& a, pii& b)
{
	return abs(a.first-b.first) + abs(a.second-b.second);
}

bool isstable(vector<pii>& b)
{
	vi q(SZ(b),0);
	q[0] = 1;
	FOR(i, SZ(b)) FOR(j, SZ(b))
		if (dist(b[i],b[j]) == 1 && q[i]+q[j]>0)
			q[i] = q[j] = 1;
	int s = 0;
	FOR(i, SZ(b)) s += q[i];
	return (SZ(b) == s);
}

int main()
{
	ifstream fin("A.in"); ofstream fout("A.out");
	int T;
	fin >> T;
	FOR(tt, T)
	{
		fin >> R >> C;
		A.resize(R);
		FOR(i, R) fin >> A[i];
		D = A;

		vrtx v;

		FOR(i, R) FOR(j, C)
		{
			if (A[i][j] == 'o')
			{
				v.b.PB(MP(i,j));
				A[i][j] = '.';
				D[i][j] = '.';
			}
			if (A[i][j] == 'w')
			{
				v.b.PB(MP(i,j));
				A[i][j] = 'x';
				D[i][j] = '.';
			}
			if (A[i][j] == 'x')
			{
				D[i][j] = '.';
			}
		}

		v.dst = 0;
		W.clear();
		deque<vrtx> deq;
		deq.PB(v);
		W.insert(v.b);

		vector<pii> npt;
		bool found = false;

		while (!deq.empty())
		{
			v = deq.front();
			deq.pop_front();

			B = D;
			FOR(i, SZ(v.b)) B[v.b[i].first][v.b[i].second] = 'o';

			if (isfin(v)) 
			{
				found = true;
				break;
			}

			FOR(i1, SZ(v.b)) FOR(k1, 4)
			{
				int r1 = v.b[i1].first + ddi[k1];
				int c1 = v.b[i1].second + ddj[k1];
				int r11 = v.b[i1].first + ddi[3-k1];
				int c11 = v.b[i1].second + ddj[3-k1];
				if (r1 < 0 || r1 >= R || c1 < 0 || c1 >= C) continue;
				if (B[r1][c1] != '.') continue;
				if (r11 < 0 || r11 >= R || c11 < 0 || c11 >= C) continue;
				if (B[r11][c11] != '.') continue;

				{
					npt = v.b;
					npt[i1] = MP(r1,c1); 

					if (isstable(npt) && (W.find(npt) == W.end()))
					{
						vrtx nv;
						nv.b = npt;
						nv.dst = v.dst+1;
						deq.PB(nv);
						W.insert(nv.b);
					}
				}

				B[r1][c1] = 'o';
				B[v.b[i1].first][v.b[i1].second] = '.';
		
				FOR(i2, SZ(v.b)) FOR(k2, 4)
				{
					int r2 = (i1 != i2) ? v.b[i2].first : r1;
					int c2 = (i1 != i2) ? v.b[i2].second : c1;
					int r22 = r2 + ddi[3-k2];
					int c22 = c2 + ddj[3-k2];
					r2 += ddi[k2];
					c2 += ddj[k2];
					if (r2 < 0 || r2 >= R || c2 < 0 || c2 >= C) continue;
					if (B[r2][c2] != '.') continue;
					if (r22 < 0 || r22 >= R || c22 < 0 || c22 >= C) continue;
					if (B[r22][c22] != '.') continue;

					npt = v.b;
					npt[i1] = MP(r1,c1); 
					npt[i2] = MP(r2,c2);

					if (isstable(npt) && (W.find(npt) == W.end()))
					{
						vrtx nv;
						nv.b = npt;
						nv.dst = v.dst+2;
						deq.PB(nv);
						W.insert(nv.b);
					}
				}

				B[r1][c1] = '.';
				B[v.b[i1].first][v.b[i1].second] = 'o';
			}
		}

		int ans = (found) ? v.dst : -1;

		fout << "Case #" << tt+1 << ": " << ans << endl;
		cout << "Case #" << tt+1 << ": " << ans << endl;
	}
	return 0;	
}
