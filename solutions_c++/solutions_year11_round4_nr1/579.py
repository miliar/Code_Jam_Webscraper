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

typedef vector<i64> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;

typedef vector<ld> vd;
typedef vector<vd> vvd;

typedef vector<string> vs;

const i64 d18 = 1000000000000000000LL;
const ld eps = 1e-12;
const ld pi = atan2(0.0, -1.0);
template<class T> T sqr(T a) { return a * a; }
i64 abs(i64 a) { return (a >= 0) ? a : -a; }

ofstream LOG("log.txt");

ifstream fin;
ofstream fout;


void solve_case(int TN)
{
	// solution...
	ld S, R, t;
	int N, X;
	fin >> X >> S >> R >> t >> N;
	vector<pair<pii,int> > A(N);
	FOR(i, N) fin >> A[i].first.first >> A[i].first.second >> A[i].second;
	sort(ALL(A));

	vector<pair<int,pii> > B;
	if (A[0].first.first > 0) B.push_back( make_pair(0, pii(0, A[0].first.first)) );
	if (A[N-1].first.second < X) B.push_back( make_pair(0, pii(A[N-1].first.second, X)) );
	FOR(i, N) B.push_back( make_pair(A[i].second, A[i].first) );
	FOR(i, N-1) if (A[i].first.second < A[i+1].first.first)
	{
		B.push_back( make_pair(0, pii(A[i].first.second, A[i+1].first.first)) );
	}
	sort(ALL(B));

	ld ans = 0;
	FOR(i, SZ(B))
	{
		ld vel = B[i].first;
		ld aa = B[i].second.first;
		ld bb = B[i].second.second;
		if (t < eps)
		{
			ans += (bb-aa) / (vel + S);
			continue;
		}
		ld spendt = (bb-aa) / (vel + R);
		if (spendt <= t)
		{
			ans += spendt;
			t -= spendt;
			continue;
		}
		ans += t;
		ans += (bb-aa - t * (vel + R)) / (vel + S);
		t = 0;
	}

	fout << fixed << setprecision(10) << "Case #" << TN << ": " << ans << endl;
	cout << fixed << setprecision(10) << "Case #" << TN << ": " << ans << endl;
}

int main()
{
	fin.open("A.in"); 
	fout.open("A.out");

	int T; 
	fin >> T;
	FOR(tt, T)
	{
		solve_case(tt+1);
	}

	return 0;	
}
