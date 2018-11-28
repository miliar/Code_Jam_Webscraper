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

typedef vector<i64> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<vvvi> vvvvi;

vi pr;
int A, B, P;

class DSU
{
public:
	vector<int> pred, rank;

	void init(int n)
	{
		rank.assign(n, 0);
		pred.resize(n);
		FOR(i, n) pred[i] = i;
	}

	int findset(int a)
	{
		if (a == pred[a]) return a;
		return (pred[a] = findset(pred[a]));
	}

	void join(int a, int b)
	{
		int x = findset(a);
		int y = findset(b);
		if (x == y) return;
		if (rank[x] <= rank[y])
		{
			pred[x] = y;
			if (rank[x] == rank[y]) ++rank[y];
		}
		else
		{
			pred[y] = x;
		}
	}
};

void primes(i64 n, vector<i64> & vp)
{
	vp.clear();
	if (n < 2) return;
	vp.reserve((int)n / 40 + 4);
	vp.push_back(2);
	for (i64 k = 3; k <= n; k += 2)
	{
		int i;
		for (i = 0; (vp[i] * vp[i] <= k) && (k % vp[i] != 0); ++i);
		if(vp[i] * vp[i] > k) vp.push_back(k);
	}
}

bool commf(int a, int b)
{
	FORR(i, 0, SZ(pr)-1)
	{
		if (pr[i] < P) break;
		if (a%pr[i] == 0 && b%pr[i]==0) return true;
	}
	return false;
}

int main()
{
	primes(1100, pr);

	ifstream fin("b.in"); ofstream fout("b.out");
	int T;
	fin >> T;
	FOR(tt, T)
	{
		fin >> A >> B >> P;
		DSU dsu;
		dsu.init(B+1);
		FORD(i, A, B) FORD(j, A+1, B)
			if (commf(i, j)) dsu.join(i, j);

		set<int> s;
		FORD(i, A, B) s.insert(dsu.findset(i));

		fout << "Case #" << tt+1 << ": " << SZ(s) << endl;
	}
	return 0;	
}
