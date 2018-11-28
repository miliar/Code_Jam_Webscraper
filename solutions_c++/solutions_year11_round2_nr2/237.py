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


void solve_case(int TN)
{
	int N;
	i64 D;
	fin >> N >> D;
	D *= 2;
	vi P(N);
	vector<int> V(N);
	bool alok = true;
	FOR(i, N)
	{
		fin >> P[i] >> V[i];
		P[i] *= 2;
		if (V[i] > 1) alok = false;
	}
	FOR(i, N-1) if (P[i+1] - P[i] < D) alok = false;

	if (alok)
	{
		fout << "Case #" << TN << ": 0.0" << endl;
		cout << "Case #" << TN << ": 0.0" << endl;
		return;
	}

	i64 a = 0, b = (i64)1e15;
	while (a+1 < b)
	{
		i64 mid = (a+b) / 2;
		i64 x = P[0] - mid;
		alok = true;
		FOR(i, N)
		{
			if (P[i] - x > mid) x = P[i] - mid;
			FOR(j, V[i])
			{
				if (x - P[i] <= mid)
				{
					x += D;
				}
				else
				{
					alok = false;
					break;
				}
			}
			if (!alok) break;
		}
		if (alok)
			b = mid;
		else
			a = mid;
	}

	fout << fixed << setprecision(2) << "Case #" << TN << ": " << 0.5*b << endl;
	cout << fixed << setprecision(2) << "Case #" << TN << ": " << 0.5*b << endl;
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
