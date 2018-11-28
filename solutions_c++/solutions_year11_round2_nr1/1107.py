#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <deque>
using namespace std;

#define VAR(a, b) __typeof(b) a = b
#define FORAB(i, a, b) for(VAR(i, a); i != b; i++)
#define FOR(i, n) FORAB(i, 0, n)
#define RFOR(i, a, b) for(VAR(i, a); i != b; i--)
#define FOREACH(i, c) FORAB(i, (c).begin(), (c).end())
#define RFOREACH(i, c) FORAB(i, (c).rbegin(), (c).rend())
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REV(c) reverse(ALL(c))
#define MAXE(c) max_element(ALL(c))
#define MINE(c) min_element(ALL(c))
#define MP(a, b) pair<__typeof(a), __typeof(b)> (a, b)
#define PB(c) push_back(c)
#define BLAH(a) cerr << a << endl
#define DBG(x) BLAH(#x << ": " << (x))
#define X first
#define Y second
#define SQ(e) (e)*(e)

#define ARPRNT(r) FOREACH(it2, (r)) cerr << (*it2) << ' '; BLAH("");
#define GRPRNT(c) BLAH(#c); FOREACH(it1, ((c))) { ARPRNT((*it1)); } BLAH("");

#define gin int TTT; cin >> TTT; for(int gtest = 1; gtest <= TTT; gtest++)
#define gout cout <<"Case #" << gtest << ": "
#define gprintf(s, a...) printf(strcat("Case #%i: ", s), a)

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef pair<double, double> xy;
typedef long double LD;

typedef deque<int> DI;
typedef deque<DI> DDI;
typedef deque<string> DS;
typedef pair<int, int> PII;
typedef deque<PII> DPII;

int gcd(int a, int b)
{
	if(!b) return a;
	return gcd(b, a % b);
}

int main()
{
	double eps = 0.000000001;
	gin
	{
		int n; cin >> n;
		VVI m(n, VI(n, 0));
		vector<vector<bool> > hasMatch(n, vector<bool>(n, false));
		vector<double> wp(n, 0), owp(n, 0), oowp(n, 0);
		FOR(i, n)
		{
			FOR(j, n)
			{
				char c; cin >> c;
				m[i][j] = (int) (c - '0');
				hasMatch[i][j] = m[i][j] != '.' - '0';
			}
		}
		//wp
		FOR(i, n)
		{
			int total = 0;
			double sum = 0;
			FOR(j, n)
			{
				if(j == i) continue;
				if(m[i][j] == 1 || m[i][j] == 0) { sum += m[i][j]; total++; }
			}
			DBG(sum);
			wp[i] = sum/total;
		}
		//owp
		FOR(i, n)
		{
			int total2 = 0;
			FOR(j, n)
			{
				if(!hasMatch[i][j]) continue;
				total2++;
				int total = 0;
				double sum = 0;
				FOR(k, n)
				{
					if(k == i || k == j) continue;
					if(m[j][k] == 1 || m[j][k] == 0) { total++; sum += m[j][k]; }
				}
				owp[i] += sum/total;
			}
			owp[i] /= total2;
		}
		//oowp
		FOR(i, n)
		{
			int total = 0;
			FOR(j, n)
			{
				if(hasMatch[i][j])
				{
					total++;
					oowp[i] += owp[j];
				}
			}
			oowp[i] /= total;
		}
		gout << endl;
		FOR(i, n)
		{
			cout.precision(12);
			cout << (0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]) << endl;
		}
	}
}
