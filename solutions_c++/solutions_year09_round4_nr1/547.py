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

#define in_file "a.in"
#define out_file "a.out"
ifstream fin(in_file);
ofstream fout(out_file);

VS a;
int n;

bool ok(VS a)
{
	FOR(i, 1, n - 1)
		FOR(j, i + 1, n)
			if (a[i][j - 1] == '1') return false;
	return true;
}

int Solve()
{
	queue <pair <int, VS> > l; 
	set <VS> was;
	if (ok(a)) return 0;
	was.insert(a);
	l.push(MP(0, a));
	while (1)
	{
		VS head = l.front().Y;
		int level = l.front().X;
		FOR(i, 1, n - 1)
		{
			VS aux = head;
			swap(aux[i], aux[i + 1]);
			if (!was.count(aux))
			{
				if (ok(aux)) return level + 1;
				was.insert(aux);
				l.push(MP(level + 1, aux));
			}
		}
		l.pop();
	}
}

int main()
{
	//Read data
	int test;
	fin >> test;
	FORN(t, test)
	{
		cout << t << endl;
		fin >> n;
		a.CL, a.RS(n + 1);
		FOR(i, 0, n) getline(fin, a[i]);
		fout << "Case #" << t + 1 << ": " << Solve() << endl;

	}
	fin.close();

	//Solve

	//Write data
	fout.close();

	return 0;
}