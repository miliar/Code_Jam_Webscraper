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

#define in_file "c.in"
#define out_file "c.out"
ifstream fin(in_file);
ofstream fout(out_file);

int n, k, best;
VVI a, g;
//VI was, ss;
VI dp, nrOne;

inline bool Touch(int i1, int i2)
{
	FOR(i, 1, k - 1)
	{
		if (a[i1][i] == a[i2][i] || a[i1][i + 1] == a[i2][i + 1]) return true;
		int v1 = a[i1][i] - a[i2][i], v2 = a[i1][i + 1] - a[i2][i + 1];
		if (v1 < 0 && v2 > 0 || v1 > 0 && v2 < 0) return true;
	}
	return false;
}

//void Back(int sp, int sol, int last)
//{
//	if (sol >= best) return;
//	if (sp == n + 1) 
//	{
//		best = sol; 
//		return;
//	}
//	FOR(i, 1, n)
//		if (!was[i])
//		{
//			was[i] = true;
//			ss[sp] = i;
//			bool check = false;
//			FOR(j, last, sp - 1)
//				if (!g[i][ss[j]])
//				{
//					check = true;
//					break;
//				}
//			if (!check)	Back(sp + 1, sol, last);
//			else Back(sp + 1, sol + 1, sp);
//			was[i] = false;
//		}
//}

int Solve()
{
	g.CL, g.RS(n + 1, VI(n + 1));
	FOR(i, 1, n - 1)
		FOR(j, i + 1, n)
			if (Touch(i, j)) g[i][j] = 0, g[j][i] = 0;
			else g[i][j] = 1, g[j][i] = 1;
	//best = n;
	//was.CL, was.RS(n + 1);
	//ss.CL, ss.RS(n + 1);
	//Back(1, 1, 1);
	nrOne.CL, nrOne.RS(1 << n);
	FOR(i, 1, (1 << n) - 1) nrOne[i] = (i & 1) + nrOne[i >> 1];
	dp.CL, dp.RS(1 << n, n);
	dp[0] = 0;
	FOR(i, 1, (1 << n) - 1)
	{
		if (nrOne[i] == 1) 
		{
			dp[i] = 1;
			continue;
		}
		int csavo = 0;
		while (!(i & (1 << csavo))) ++csavo;
		int aux = i - (1 << csavo);
		dp[i] = dp[aux] + 1; //Egyedul a csavo
		for(int j = aux; j; j = aux & (j - 1)) 
		{
			//Megprobal a j csapatban jatszani
			bool can = true;
			FORN(k, n)
				if ((j & (1 << k)) && (!g[csavo + 1][k + 1]))
				{
					can = false;
					break;
				}
			//cout << i << " " << j << endl;
			if (can) dp[i] = min(dp[i], dp[j] + dp[aux - j]);
		}
	}
	return dp[(1 << n) - 1];
}

int main()
{
	//Read data
	int test;
	fin >> test;
	FORN(t, test)
	{
		cout << t << endl;
		fin >> n >> k;
		a.CL, a.RS(n + 1, VI(k + 1));
		FOR(i, 1, n)
			FOR(j, 1, k) fin >> a[i][j];
		fout << "Case #" << t + 1 << ": " << Solve() << endl;
	}
	fin.close();

	//Solve

	//Write data
	fout.close();

	return 0;
}