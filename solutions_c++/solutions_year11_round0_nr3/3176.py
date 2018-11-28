

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
	int a[100] , m[100] = {0}, cas, n, v1, v2, s1, s2, msum;
	cin >> cas;
	REP(x, cas)
	{
		cin >> n;
		msum = -1;
		REP(i, n)
		{
			cin >> a[i];
			m[i] = 0;
		}
		REP(i, (n+1) / 2)
		{
			REP(j, n)
				m[j] = 0;
			FOR(j, i+1, n)
				m[j] = 1;
			
			do
			{
				v1 = 0, v2 = 0, s1 = 0, s2 = 0;
				REP(i, n)
				{
					if(m[i] == 1)
					{
						v1 ^= a[i];
						s1 += a[i];
					}
					else
					{
						v2 ^= a[i];
						s2 += a[i];
					}
				}
				if(v1 == v2 && (v1 != 0 || v2 != 0))
				{
					msum = max(msum, max(s1, s2));
				}
			}
			while(next_permutation(m, m + n));
		}
		printf("Case #%d: ", x+1);
		if(msum == -1)
			cout << "NO" << endl;
		else
			cout << msum << endl;
	}
	return 0;
}
