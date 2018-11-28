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
#include <stack>
#include <list>

#include <numeric> 
#include <algorithm> 

#include <cstdio>
#include <fstream>
#include <iostream> 
#include <sstream> 
#include <iomanip>

#include <cctype>
#include <cmath> 
#include <ctime>
#include <cassert>

using namespace std;

#define LL long long
#define PII pair <int, int>
#define VB vector <bool>
#define VI vector <int>
#define VD vector <double>
#define VS vector <string>
#define VPII vector <pair <int, int> >
#define VVI vector < VI >
#define VVB vector < VB >

#define FORN(i, n) for(int i = 0; i < (n); ++i)
#define FOR(i, a, b) for(int i = (a); i <= (b); ++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
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

#define IN_FILE "input.txt"
#define OUT_FILE "output.txt"

#define BASE 999983

ifstream fin(IN_FILE);
ofstream fout(OUT_FILE);

int test, n, best;
VI a;
set <PII> all;

void Solve()
{
	int xorsum = 0, sum = 0;
	best = -1;
	FOR(i, 1, n) 
	{
		xorsum ^= a[i];
		sum += a[i];
	}
	if (!xorsum) best = sum - *min_element(a.BG + 1, a.EN);
}

int main()
{
	//Read data
	fin >> test;
	FORN(t, test)
	{
		cout << t << endl;
		fin >> n;
		a.RS(n + 1);
		FORN(i, n) fin >> a[i + 1];
		Solve();
		fout << "Case #" << t + 1 << ": ";
		if (best == -1) fout << "NO" << endl;
		else fout << best << endl;
	}
	fin.close();

	//Solve

	//Write data
	fout.close();

	return 0;
}