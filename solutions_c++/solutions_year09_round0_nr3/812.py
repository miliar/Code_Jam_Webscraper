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

#define in_file "c.in"
#define out_file "c.out"
ifstream fin(in_file);
ofstream fout(out_file);

int test;
string text, pattern = "#welcome to code jam";
vector <VI> dp;

int Solve()
{
	dp.clear();
	dp.RS(text.SZ + 1, VI(pattern.SZ + 1));
	FOR(i, 1, text.SZ)
		FOR(j, 1, pattern.SZ)
		{
			if (i < j) continue;
			if (text[i] != pattern[j]) continue;
			if (j == 1)
			{
				dp[i][j] = 1;
				continue;
			}
			FOR(k, 1, i - 1) dp[i][j] = (dp[i][j] + dp[k][j - 1]) % 10000;
		}
	int ans = 0;
	FOR(i, 1, text.SZ) ans = (ans + dp[i][pattern.SZ]) % 10000;
	return ans;
}

int main()
{
	//Read data
	fin >> test;
	char buf[505];
	fin.getline(buf,505);
	FORN(t, test)
	{
		fin.getline(buf,505);
		string s(buf);
		s = '#' + s;
		text = s;
		stringstream ss;
		ss << Solve();
		string sol;
		ss >> sol;
		while (sol.SZ < 4) sol = '0' + sol;
		fout << "Case #" << t + 1 << ": " << sol << endl;
	}
	fin.close();

	//Solve

	//Write data
	fout.close();

	return 0;
}