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

int n;
VS a;
VVI opp;
VD owp;

double Wp(VS a, int team)
{
	int nGames = 0, nWins = 0;
	FORN(i, a[team].SZ)
	{
		if (a[team][i] != '.') ++nGames;
		if (a[team][i] == '1') ++nWins;
	}
	return double (nWins) / nGames;
}

double Owp(VS a, VVI opp, int team)
{
	if (owp[team] != -1) return owp[team];
	FOR(i, 1, n) 
	{
		opp[i].erase(opp[i].BG + team - 1);
		a[i].erase(team - 1, 1);
	}
	double sum = 0;
	int nOpp = 0;
	FORN(i, a[team].SZ)
		if (a[team][i] != '.')
		{
			sum += Wp(a, opp[team][i]);
			++nOpp;
		}
	if (nOpp) return owp[team] = sum / nOpp;
	else return owp[team] = 0;
}

double Oowp(VS a, VVI opp, int team)
{
	double sum = 0;
	int nOpp = 0;
	FORN(i, a[team].SZ)
		if (a[team][i] != '.')
		{
			sum += Owp(a, opp, opp[team][i]);
			++nOpp;
		}
	if (nOpp) return sum / nOpp;
	else return 0;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	cin >> test;
	FOR(t, 1, test)
	{
		cin >> n;
		a.CL, a.RS(n + 1);
		opp.CL, opp.RS(n + 1, VI (n));
		owp.CL, owp.RS(n + 1, -1);
		FOR(i, 1, n)
			FOR(j, 1, n) 
			{
				opp[i][j - 1] = j;
				char ch;
				cin >> ch;
				a[i] += ch;
			}
		//FOR(i, 1, n) cout << Wp(a, i) << endl;
		//cout << "-----" << endl;
		//FOR(i, 1, n) cout << Owp(a, opp, i) << endl;
		//cout << Oowp(a, opp, 1) << endl;
		cout << "Case #" << t << ": " << endl;
		FOR(i, 1, n)
		{
			double aux = 0.25 * Wp(a, i) + 0.5 * Owp(a, opp, i) + 0.25 * Oowp(a, opp, i);
			cout << aux << endl;
		}
	}
	return 0;
}