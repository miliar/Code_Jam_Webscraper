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
	int cas, n, no, pO, pB, ans, cO, cB;
	char ch, cur;
	cin >> cas;
	REP(x, cas)
	{
		cin >> n;
		deque<int> O, B;
		deque<char> seq;
		REP(i, n)
		{
			cin >> ch;
			seq.PB(ch);
			cin >> no;
			if(ch == 'O')
				O.PB(no);
			else
				B.PB(no);
		}
		pO = 1, pB = 1, ans = 0;
		while( !seq.empty())
		{
			cur = seq.front();

			cO = O.front();
			O.FP();

			cB = B.front();
			B.FP();

			if(cur == 'O')
			{
				if(cO == pO)
				{
					seq.FP();
				}
				if(pO < cO)
				{
					O.PF(cO);
					pO++;
				}
				if(pO > cO)
				{
					O.PF(cO);
					pO--;
				}
				if(cB == pB)
				{
					B.PF(cB);
				}
				if(pB < cB)
				{
					B.PF(cB);
					pB++;
				}
				if(pB > cB)
				{
					B.PF(cB);
					pB--;
				}
			}
			else
			{
				if(cO == pO)
				{
					O.PF(cO);
				}
				if(pO < cO)
				{
					O.PF(cO);
					pO++;
				}
				if(pO > cO)
				{
					O.PF(cO);
					pO--;
				}
				if(cB == pB)
				{
					seq.FP();
				}
				if(pB < cB)
				{
					B.PF(cB);
					pB++;
				}
				if(pB > cB)
				{
					B.PF(cB);
					pB--;
				}
			}
			ans++;
		}
		printf("Case #%d: %d\n", x+1, ans);
	}
	return 0;
}
