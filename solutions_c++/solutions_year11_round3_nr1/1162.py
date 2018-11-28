

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
using namespace std;

#define REP(i,n) for (int i=0; i<(int)(n); ++i)
#define REPS(p,s) for (char * p = s; *p ; p++)
#define FOR(var,start,end) for (int var=(start); var<(int)(end); ++var)
#define FORD(var,start,end) for (int var=(start); var>=(int)(end); --var) 
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
	int cas, r, c ;
	bool f, f2;
	cin >> cas;
	REP(x, cas)
	{
		cin >> r >> c;
		vector<string> v(r);
		REP(i, r)
			cin >> v[i];
		f2 = true;
		f = true;
		cout << "Case #" << (x+1) << ":\n";
		REP(i, r - 1)
		{
			REP(j, c - 1)
			{
				if(v[i][j] == '#')
				{
					if(v[i][j+1] == '#' && v[i+1][j] == '#' && v[i+1][j+1] == '#')
					{
						v[i][j] = '/';
						v[i][j+1] = '\\';
						v[i+1][j] = '\\';
						v[i+1][j+1] = '/';
					}
					else
					{
						cout << "Impossible\n";
						f = false;
						break;
					}
				}
			}
			if(!f)
			{
				f2 = false;
				break;
			}
		}
		REP(i, r)
			if(find(v[i].BN, v[i].ED, '#') != v[i].ED)
			{
				f2 = false;
				break;
			}
		if(f2)
			REP(i, r)
				cout << v[i] << endl;
		else
			if(f)
				cout << "Impossible" << endl;
	}
	return 0;
}
