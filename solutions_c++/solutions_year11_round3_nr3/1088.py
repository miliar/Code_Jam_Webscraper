


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

ULL gcd(ULL a, ULL b)
{
	if(b == 0)
		return a;
	else
		return gcd(b, a% b);
}

ULL lcm(ULL a, ULL b)
{
	return (a * b) / gcd(a, b);
}

ULL lcmoflist(vector<ULL> v)
{
	if(v.size() == 2)
		return lcm(v[0], v[1]);
	else
	{
		vector<ULL> p(v.size() - 1);
		copy(v.BN + 1, v.ED, p.BN);
		return lcm(v[0], lcmoflist(p));
	}
}


int main()
{
	int cas;
	ULL n, l, h, least, ans;
	bool f, f2;
	cin >> cas;
	REP(x, cas)
	{

		cin >> n >> l >> h;
		vector<ULL> fq(n);
		REP(i, n)
			cin >> fq[i];

		cout << "Case #" << (x+1) << ": ";
		f2 = false;
		for(ULL i = l; i < h+1; i++)
		{
			f = true;	
			REP(j, n)
				if(i % fq[j] != 0 && fq[j] % i != 0)
				{
					f = false;
					break;
				}
			if(f)
			{
				f2 = true;
				cout << i << endl;
				break;
			}
		}
		if(!f2)
			cout << "NO" << endl;
	}
	return 0;
}
