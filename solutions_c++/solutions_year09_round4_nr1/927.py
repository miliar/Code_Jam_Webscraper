#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <climits>
#include <string>
#include <cstring>
using namespace std;

#define forn(a, n) for(int (a) = 0; (a) < (n); ++(a))
#define dforn(a, n) for(int (a) = (n); (a) >= 0; --(a))

#define forsn(a, s, n) for(int (a) = (s); (a) < (n); ++(a))
#define dforsn(a, s, n) for(int (a) = (s); (a) >= (n); --(a))

#define forall(a, b) for(typeof((b).begin()) (a) = (b).begin(); (a) != (b).end(); ++(a))
#define dforall(a, b) for(typeof((b).begin()) (a) = (b).rbegin(); (a) != (b).rend(); ++(a))
#define esta(a, b) (((a) & (1LL<<(b))) != 0)

typedef long long tint;
const int INF = INT_MAX-1000;

int t, n;
char mat[64][64];

void movmat(int i, int j)
{
	dforsn(k, j-1, i)
	{
		//swapeo k-1 con k
		forn(r, n) swap(mat[k+1][r], mat[k][r]);
	}
}

void print()
{
	forn(i, n)
	{
		forn(j, n) printf("%i ", mat[i][j]);
		printf("\n");
	}
}

int main()
{
#ifdef TAVO92
	freopen("A-large.in" , "r" , stdin);
	freopen("A-large.out", "w" , stdout);
#endif
	
	scanf("%i", &t);
	
	forn(p, t)
	{
		scanf("%i", &n);
		
		forn(i, n) scanf("%s", mat[i]);
		
		forn(i, n) forn(j, n) mat[i][j] -= '0';
		
		int ret = 0, sw;
		bool bad=false;
		
		forn(i, n)
		{
			bad = false;
			forsn(j, i+1, n) bad |= mat[i][j];
			
			if(!bad) continue;
			
			cerr << i << " ";
			
			sw=0;
			
			forsn(k, i+1, n)
			{
				bad = false;
				forsn(j, i+1, n) bad |= mat[k][j];
				
				if(!bad)
					{sw = k; break;}
			}
			
			cerr << sw << endl;
			movmat(i, sw);
//			print(); cout << endl;
			ret += sw-i;
			--i;
		}
		
		printf("Case #%i: %i\n", p+1, ret);
	}
	return 0;
}
