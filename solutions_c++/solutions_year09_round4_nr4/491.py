//Code by Patcas Csaba
//Time complexity:
//Space complexity:
//Method:
//Implementation time: 

#include <vector>
#include <string> 
#include <set> 
#include <map> 
#include <queue> 
#include <bitset> 

#include <numeric> 
#include <algorithm> 

#include <cstdio>
#include <fstream>
#include <iostream> 
#include <sstream> 

#include <cctype>
#include <cmath> 
#include <ctime>
#include <cassert>

using namespace std;

#define VI vector <int>
#define VVI vector <VI>
#define VS vector <string>
#define VB vector <bool>
#define PII pair <int, int>
#define LL long long

#define FORN(i, n) for(int i = 0; i < (n); ++i)
#define FOR(i, a, b) for(int i = (a); i <= (b); ++i)
#define FORI(it, X) for(__typeof((X).begin()) it = (X).begin(); it !=(X).end(); ++it) 
#define REPEAT do{ 
#define UNTIL(x) }while(!(x)); 

#define SZ size()
#define BG begin() 
#define EN end() 
#define CL clear()
#define X first
#define Y second
#define RS resize
#define PB push_back
#define MP make_pair
#define ALL(x) x.begin(), x.end()

#define in_file "d.in"
#define out_file "d.out"
ifstream fin(in_file);
ofstream fout(out_file);

struct xyz
{
	int x, y, r;
};

int n;
vector <xyz> a;

inline double dist(int i1, int i2)
{
	return sqrt(double(a[i1].x - a[i2].x) * (a[i1].x - a[i2].x) + (a[i1].y - a[i2].y) * (a[i1].y - a[i2].y));
}

double Solve()
{
	if (n == 1) return a[1].r;
	if (n == 2) return max(a[1].r, a[2].r);
	double r1 = (dist(1, 2) + a[1].r + a[2].r) / 2;
	double r2 = (dist(1, 3) + a[1].r + a[3].r) / 2;
	double r3 = (dist(3, 2) + a[3].r + a[2].r) / 2;

	double ans = max(r1, double(a[3].r));
	ans = min(ans, max(r2, double(a[2].r)));
	ans = min(ans, max(r3, double(a[1].r)));

	return ans;
}

int main()
{
	//Read data
	int test;
	fin >> test;
	FORN(t, test)
	{
		fin >> n;
		a.CL, a.RS(n + 1);
		FOR(i, 1, n) fin >> a[i].x >> a[i].y >> a[i].r;
		fout << "Case #" << t + 1 << ": " << Solve() << endl;
	}
	fin.close();

	//Solve

	//Write data
	fout.close();

	return 0;
}