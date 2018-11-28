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
const ld eps = 1e-9;
const ld pi = atan2(0.0, -1.0);
template<class T> T sqr(T a) { return a * a; }
i64 abs(i64 a) { return (a >= 0) ? a : -a; }

ofstream LOG("log.txt");

ifstream fin;
ofstream fout;

i64 lpow(i64 a, i64 b, i64 m)
{
	i64 res = 1;
	while (b > 0)
	{
		if (b & 1) res = (res * a) % m;
		a = (a * a) % m;
		b >>= 1;
	}
	return res;
}

i64 rev(i64 a, i64 p)
{
	return lpow(a, p-2, p);
}

int elgauss(vvi& A, i64 M, vector<int>& p = vector<int>())
{
	int n = SZ(A);
	int m = SZ(A[0]);
	p.resize(n);
	FOR(i, n) p[i] = i;
	int rank = 0;
	FOR(k, m)
	{
		int r = -1;
		FORD(i, rank, n-1)
		{
			if (A[i][k] != 0)
			{
				r = i;
				break;
			}
		}
		if (-1 == r) continue;
		if (r != rank) swap(A[rank],A[r]), swap(p[rank],p[r]);
		FOR(i, n)
		{
			if (i == rank) continue;
			i64 fct = A[i][k] * rev(A[rank][k],M) % M;
			FORD(j, k, m-1)
				A[i][j] = (A[i][j] - A[rank][j] * fct) % M;
		}
		++rank;
	}
	FOR(i, n) FOR(j, m) A[i][j] = (A[i][j] % M + M) % M;
	return rank;
}

int slaugauss(vvi A, vi b, i64 M, vi& x, int& rank)
{
	int n = SZ(A);
	FOR(i, n) A[i].push_back(b[i]);
	rank = elgauss(A, M);
	x.assign(n, 0);
	for(int i = 0, j = 0; i < rank; ++i)
	{
		while (A[i][j] == 0) ++j;
		x[j] = A[j][n] * rev(A[i][j],M) % M;
	}
	FORD(i, rank, n-1) if (x[i] != 0) return 2;
	return (rank < n) ? 1 : 0;
}

void resh(int n, vector<char>& p)
{
	p.assign(n+1, 1);
	p[0] = p[1] = 0;
	for (int i = 4; i <= n; i += 2) p[i] = 0;
	for (int i = 3; i * i <= n; i += 2)
	{
		if (!p[i]) continue;
		int ii = i+i;
		for (int j = i+ii; j <= n; j += ii)
			p[j] = 0;
	}
}

void primes(int n, vi& pr)
{
	pr.clear();
	vector<char> isp;
	resh(n, isp);
	pr.push_back(2);
	for (int i = 3; i <= n; i += 2) 
		if (isp[i]) pr.push_back(i);
}

void solve_case(int TN)
{
	int D, K;
	fin >> D >> K;

	bool same = true;

	vi a(K);
	FOR(i, K)
	{
		fin >> a[i];
		if (i > 0 && a[i] != a[i-1]) same = false;
	}
	
	i64 ans = -1;

	if (K > 1 && same)
	{
		ans = a[0];
	}
	else if (K > 2)
	{
		int L = 1;
		FOR(i, D) L *= 10;

		vi P;
		primes(L, P);

		vvi A(2, vi(2));
		A[0][0] = a[0];
		A[0][1] = 1;
		A[1][0] = a[1];
		A[1][1] = 1;

		vi b(2);
		b[0] = a[1];
		b[1] = a[2];

		i64 MAXN = *max_element(ALL(a));

		bool ok = true;

		FOR(i, SZ(P))
		{
			if (P[i] <= MAXN) continue;

			vi x;
			int rank;
			int r = slaugauss(A, b, P[i], x, rank);

			if (r != 0)
			{
				continue;
				ok = false;
				break;
			}

			bool fnd = true; 

			FOR(j, K-1)
			{
				if ((a[j] * x[0] + x[1]) % P[i] != a[j+1])
				{
					//ok = false;
					fnd = false;
					break;
				}
			}

			if (!fnd) continue;

			//if (!ok) break;

			if (ans == -1) ans = (a[K-1] * x[0] + x[1]) % P[i];

			if (ans != (a[K-1] * x[0] + x[1]) % P[i])
			{
				ok = false;
				break;
			}
		}

		if (!ok) ans = -1;
	}

	if (ans != -1)
	{
		fout << "Case #" << TN << ": " << ans << endl;
		cout << "Case #" << TN << ": " << ans << endl;
	}
	else
	{
		fout << "Case #" << TN << ": I don't know." << endl;
		cout << "Case #" << TN << ": I don't know." << endl;
	}
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
