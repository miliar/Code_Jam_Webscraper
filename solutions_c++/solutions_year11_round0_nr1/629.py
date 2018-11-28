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
	fin >> N;
	vector<int> A(N);
	vector<char> C(N);
	FOR(i, N) fin >> C[i] >> A[i];

	int Ocur = 1, Bcur = 1;
	int ans = 0;
	FOR(i, N)
	{
		int Odest = -1, Bdest = -1;
		FORD(j, i, N-1)
		{
			if (Bdest == -1 && C[j] == 'B') Bdest = A[j];
			if (Odest == -1 && C[j] == 'O') Odest = A[j];
			if (Odest != -1 && Bdest != -1) break;
		}
		if (C[i] == 'B')
		{
			int dt = abs(Bdest-Bcur) + 1;
			ans += dt;
			Bcur = Bdest;
			if (dt >= abs(Odest-Ocur))
				Ocur = Odest;
			else
				Ocur += (Odest > Ocur) ? dt : -dt;
		}
		else
		{
			int dt = abs(Odest-Ocur) + 1;
			ans += dt;
			Ocur = Odest;
			if (dt >= abs(Bdest-Bcur))
				Bcur = Bdest;
			else
				Bcur += (Bdest > Bcur) ? dt : -dt;
		}
	}

	fout << "Case #" << TN << ": " << ans << endl;
	cout << "Case #" << TN << ": " << ans << endl;
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
