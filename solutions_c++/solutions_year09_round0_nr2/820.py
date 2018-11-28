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
#define VB vector <bool>
#define PII pair <int, int>
#define LL long long

#define FORN(i, n) for(int i = 0; i < n; ++i)
#define FOR(i, a, b) for(int i = a; i <= b; ++i)
#define repeat do{ 
#define until(x) }while(!(x)); 

#define SZ size()
#define BG begin() 
#define EN end() 
#define X first
#define Y second
#define RS resize
#define PB push_back
#define MP make_pair
#define ALL(x) x.begin(),x. end()

#define in_file "b.in"
#define out_file "b.out"
ifstream fin(in_file);
ofstream fout(out_file);

int test, n, m, nSink;
vector <VI> a, memo;
vector <vector <char> > sol;
int dx[4] = {-1,0,0,1};
int dy[4] = {0,-1,1,0};

inline bool OnBoard(int x, int y)
{
	return (x >= 1 && x <= n && y >= 1 && y <= m);
}

int Solve(int x, int y)
{
	int &ref = memo[x][y];
	if (ref != -1) return ref;
	int iMin = -1;
	FORN(i, 4)
	{
		if (!OnBoard(x + dx[i], y + dy[i])) continue;
		if (iMin == -1 || a[x + dx[i]][y + dy[i]] < a[x + dx[iMin]][y + dy[iMin]]) iMin = i;
	}
	if (iMin == -1 || a[x + dx[iMin]][y + dy[iMin]] >= a[x][y])
	{
		++nSink;
		return ref = nSink;
	}
	return ref = Solve(x + dx[iMin], y + dy[iMin]);
}

int main()
{
	//Read data
	fin >> test;
	FORN(t, test)
	{
		cout << t << endl;
		fin >> n >> m;
		a.clear();
		a.RS(n + 1, VI(m + 1));
		FOR(i, 1, n)
			FOR(j, 1, m) fin >> a[i][j];
		memo.clear();
		memo.RS(n + 1, VI(m + 1, -1));
		nSink = 0;
		FOR(i, 1, n)
			FOR(j, 1, m) memo[i][j] = Solve(i, j);
		sol.clear();
		sol.RS(n + 1, vector <char> (m + 1, '#'));
		char letter = 'a' - 1;
		FOR(i, 1, n)
			FOR(j, 1, m)
				if (sol[i][j] == '#')
				{
					++letter;
					FOR(q, 1, n)
						FOR(w, 1, m)
							if (memo[q][w] == memo[i][j]) sol[q][w] = letter;
				}
			fout << "Case #" << t + 1 << ":" << endl;
			FOR(i, 1, n)
			{
				FOR(j, 1, m) fout << sol[i][j] << " ";
				fout << endl;
			}
	}
	fin.close();

	//Solve

	//Write data
	fout.close();

	return 0;
}