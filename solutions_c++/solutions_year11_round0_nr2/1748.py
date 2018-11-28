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

int test;
int n, m, k;
VVI comb, opp;
string s, sol;

void Solve()
{
	sol = "";
	FORN(i, n)
	{
		if (sol.SZ && comb[sol[sol.SZ - 1]][s[i]] != -1) 
		{
			char aux = comb[sol[sol.SZ - 1]][s[i]];
			sol.erase(sol.SZ - 1);
			sol += aux; 
			continue;
		}
		if (sol.SZ)
		{
			bool found = false;
			FORN(j, sol.SZ)
				if (opp[sol[j]][s[i]])
				{
					found = true;
					break;
				}
			if (found)
			{
				sol = "";
				continue;
			}
		}
		sol += s[i];
	}
}

int main()
{
	//Read data
	fin >> test;
	FORN(t, test)
	{
		comb.CL, comb.RS(100, VI(100, -1));
		opp.CL, opp.RS(100, VI(100, 0));
		fin >> m;
		FORN(i, m)
		{
			string aux;
			fin >> aux;
			comb[aux[0]][aux[1]] = aux[2];
			comb[aux[1]][aux[0]] = aux[2];
		}
		fin >> k;
		FORN(i, k)
		{
			string aux;
			fin >> aux;
			opp[aux[0]][aux[1]] = 1;
			opp[aux[1]][aux[0]] = 1;
		}
		fin >> n >> s;
		Solve();
		fout << "Case #" << t + 1 << ":";
		fout << "[";
		if (sol.SZ)
		{
			FORN(i, sol.SZ - 1) fout << sol[i] << ", ";
			fout << sol[sol.SZ - 1] << "]" << endl;
		}
		else fout << "]" << endl;
	}
	fin.close();

	//Solve

	//Write data
	fout.close();

	return 0;
}