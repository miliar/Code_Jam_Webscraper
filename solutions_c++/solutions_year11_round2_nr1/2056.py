
/* headers & macros  */
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <climits>
#include <iomanip>
using namespace std;

#define REP(i,n) for (int i=0; i<(int)(n); ++i)
#define REPS(p,s) for (char * p = s; *p ; p++)
#define FOR(var,start,end) for (int var=(start); var<(int)(end); ++var)
#define RFOR(var,start,end) for (int var=(start); var>=(int)(end); --var) 
#define PB push_back
#define PF push_front
#define BP pop_back
#define FP pop_front
#define BN begin()
#define RN rbegin()
#define RD rend()
#define ED end()
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define IT(X) __typeof((X).BN)
#define RIT(X) __typeof((X).RN) 
#define REF(X) __typeof(__typeof(X)::reference) 
#define FORIT(it, X) for(IT(X) it = (X).BN; it != (X).ED; ++it)
#define FORITR(it, X) for(RIT(X) it = (X).RN; it != (X).RD; ++it) 
#define VV(X) vector < vector< X > >
#define PIB(X)  pair<IT(X),bool >  

typedef long long LL;
typedef unsigned long long ULL;
typedef istringstream ISS;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector< PII > VPII;	/*}}}*/


int main()
{
	int cas, n;
	double played, won;
	double twp, towp;
	cin >> cas;
	REP(x, cas)
	{
		cin >> n;
		vector<string> a(n), temp(n);
		REP(i, n)
			cin >> a[i];
		vector<double> wp(n), owp(n), oowp(n), rpi(n), p(n);
		REP(i, n)
		{
			played = 0.0;
			won = 0.0;
			REP(j, n)
			{
				if(a[i][j] != '.')
					played++;
				if(a[i][j] == '1')
					won++;
			}
			p[i] = played;
			wp[i] = won / played;
		}

		twp = 0.0;

		REP(i, n)
		{
			temp = a;
			owp[i] = 0.0;
			vector<bool> f(n);
			fill(f.BN, f.ED, true);
			REP(j, n)
			{
				if(temp[i][j] == '.')
					f[j] = false;
			}
			REP(j, n)
			{
				if(i == j)
					continue;
				temp[j][i] = '.';
				temp[i][j] = '.';
			}
			REP(j, n)			
			{
				if(j == i)
					continue;
				played = 0.0;
				won = 0.0;
				REP(k, n)
				{
					if(k == i)
						continue;
					if(temp[j][k] != '.')
						played++;
					if(temp[j][k] == '1')
						won++;
				}
				if(f[j])
					owp[i] += (won / played);
			}
			f[i] = false;
			owp[i] /= count(f.BN, f.ED, true);
		}

		REP(i, n)
		{
			oowp[i] = 0.0;
			temp = a;
			vector<bool> f(n);
			fill(f.BN, f.ED, true);
			REP(j, n)
			{
				if(i == j)
					continue;
				if(temp[i][j] == '.')
					f[j] = false;
			}
			REP(j, n)
			{
				if(i  == j)
					continue;
				if(f[j])
					oowp[i] += owp[j];
			}
			f[i] = false;
			oowp[i] /= count(f.BN, f.ED, true);
		}

		REP(i, n)
			rpi[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];

		cout << "Case #"<<x+1 << ":\n";
		REP(i, n)
			cout << setprecision(10) << rpi[i] << endl;

	}	
	return 0;
}
