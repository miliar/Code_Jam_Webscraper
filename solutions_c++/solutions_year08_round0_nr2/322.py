#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <complex>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()

#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())

#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()

typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef vector<double> VD;
typedef vector<PII> VPI;
typedef vector<VPI> VVPI;
typedef set<string> SET;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef vector<PII> VPI;
typedef vector<int> VI;
typedef vector<string> VS;

int toInt(string s, int t)
{
	replace(ALL(s), ':', ' ');
	istringstream in(s);
	int h, m;
	in >> h >> m;
	return 60*h+m+t;
}

int main()
{
    freopen("q2.in", "r", stdin);
    freopen("q2.out", "w+", stdout);
	int n;
	cin >> n;
	REP(it,n)
	{
		int t;
		cin >> t;
		int na, nb;
		cin >> na >> nb;
		VPI NA, NB;
		REP(i,na)
		{
			string s1, s2;
			cin >> s1 >> s2;
			NA.pb(PII(toInt(s1, 0), toInt(s2, t)));
		}
		REP(i,nb)
		{
			string s1, s2;
			cin >> s1 >> s2;
			NB.pb(PII(toInt(s1, 0), toInt(s2, t)));
		}
		VI SA, EA, SB, EB;
		REP(i,SZ(NA))
		{
			SA.pb(NA[i].X);
			EA.pb(NA[i].Y);
		}
		REP(i,SZ(NB))
		{
			SB.pb(NB[i].X);
			EB.pb(NB[i].Y);
		}
		sort(ALL(SA));
		sort(ALL(EA));
		sort(ALL(SB));
		sort(ALL(EB));
		int rA = 0;
		int rB = 0;
		int bA = 0;
		int bB = 0;
		int iSA = 0;
		int iSB = 0;
		int iEA = 0;
		int iEB = 0;
		while (iEA != SZ(EA) || iEB != SZ(EB))
		{
			int fSA = INF;
			int fSB = INF;
			int fEA = INF;
			int fEB = INF;
			if (iSA < SZ(SA))
				fSA = SA[iSA];
			if (iSB < SZ(SB))
				fSB = SB[iSB];
			if (iEA < SZ(EA))
				fEA = EA[iEA];
			if (iEB < SZ(EB))
				fEB = EB[iEB];
			int mi = min(min(fSA, fSB), min(fEA, fEB));
			if (fEA == mi)
			{
				bB++;
				iEA++;
			} else if (fEB == mi)
			{
				bA++;
				iEB++;
			} else if (fSA == mi)
			{
				bA--;
				iSA++;
				if (bA < 0)
				{
					rA -= bA;
					bA = 0;
				}
			} else if (fSB == mi)
			{
				bB--;
				iSB++;
				if (bB < 0)
				{
					rB -= bB;
					bB = 0;
				}
			}
		}
		cout << "Case #" << it+1 << ": "<< rA <<" " << rB << endl;
	}
}
