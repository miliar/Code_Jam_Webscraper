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

#define in_file "a.in"
#define out_file "a.out"
ifstream fin(in_file);
ofstream fout(out_file);

int l, n, m;
vector <string> dict;
vector <set <char> > valid;
string pattern;

int main()
{
	//Read data
	fin >> l >> n >> m;
	dict.RS(n + 1);
	FOR(i, 1, n) fin >> dict[i];
	FOR(t, 1, m)
	{
		cout << t << endl;
		fin >> pattern;
		valid.clear();
		valid.RS(l + 1);
		int j = 0;
		FOR(i, 1, l)
			if (pattern[j] == '(')
			{
				repeat
					++j;
					if (pattern[j] == ')') break;
					valid[i].insert(pattern[j]);
				until (0);
				++j;
			}
			else
			{
				valid[i].insert(pattern[j]);
				++j;
			}
		int sol = 0;
		FOR(i, 1, n)
		{
			bool ok = true;
			FOR(j, 1, l)
				if (!valid[j].count(dict[i][j - 1]))
				{
					ok = false;
					break;
				}
			if (ok) ++sol;
		}
		fout << "Case #" << t << ": " << sol << endl;
	}

	fin.close();

	//Solve

	//Write data
	fout.close();

	return 0;
}