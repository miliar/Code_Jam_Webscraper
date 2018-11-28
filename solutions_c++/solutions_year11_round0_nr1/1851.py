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

ifstream fin(IN_FILE);
ofstream fout(OUT_FILE);

int test, n, ttime;
vector <PII> a;

void Solve()
{
	ttime = 0;
	VI where(2, 1);
	FORN(i, a.SZ)
	{
		++ttime;
		VI next(2, -1);
		FOR(j, i, a.SZ - 1)
			if (a[j].X == 0)
			{
				next[0] = a[j].Y;
				break;
			}
		FOR(j, i, a.SZ - 1)
			if (a[j].X == 1)
			{
				next[1] = a[j].Y;
				break;
			}
		int dist = abs(where[a[i].X] - a[i].Y), other = 1 - a[i].X;
		ttime += dist;
		if (dist >= abs(where[other] - next[other])) where[other] = next[other];
		else
			if (where[other] > next[other]) where[other] = where[other] - dist - 1;
			else where[other] = where[other] + dist + 1;
		where[a[i].X] = a[i].Y;
	}
}

int main()
{
	//Read data
	fin >> test;
	FORN(t, test)
	{
		fin >> n;
		a.CL, a.RS(n);
		FORN(i, n)
		{
			char ch;
			fin >> ch;
			a[i].X = ch == 'O';
			fin >> a[i].Y;
		}
		Solve();
		fout << "Case#" << t + 1 << ": "  << ttime << endl;
	}
	fin.close();

	//Solve

	//Write data
	fout.close();

	return 0;
}