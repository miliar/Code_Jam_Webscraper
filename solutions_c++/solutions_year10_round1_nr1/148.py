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
#define dforn(a, n) for(int (a) = (n-1); (a) >= 0; --(a))

#define forsn(a, s, n) for(int (a) = (s); (a) < (n); ++(a))
#define dforsn(a, s, n) for(int (a) = (s-1); (a) >= (n); --(a))

#define forall(a, b) for(typeof(b.begin()) a = b.begin(); a != b.end(); ++a)
#define dforall(a, b) for(typeof(b.rbegin()) a = b.rbegin(); a != b.rend(); ++a)
#define esta(a, b) (((a) & (1LL<<(b))) != 0)

typedef long long tint;
const int INF = INT_MAX-1000;

const int DX[8] = {1,-1,0,0,1,1,-1,-1};
const int DY[8] = {0,0,1,-1,1,-1,1,-1};

string tab[55], rot[55];
int n, k;

bool win(char c)
{
	forn(i, n) forn(j, n) if(rot[i][j] == c)
	forn(d, 8)
	{
		bool p = true;
		forn(kk, k)
		{
			int x = i+kk*DX[d], y = j+kk*DY[d];
			if(min(x, y) < 0 || x >= n || y >= n)
				p = false;
			else
				p &= rot[x][y] == c;
		}
		
		if(p) {return true;}
	}
	
	return false;
}

int main()
{
#ifdef TAVO92
	freopen("A-large.in" , "r" , stdin);
	freopen("A-large.out", "w" , stdout);
#endif
	
	int t; scanf("%i", &t);
	
	forn(p, t)
	{
		scanf("%i%i", &n, &k);
		
		forn(i, n) cin >> tab[i], rot[i] = string(n, '.');
		
		forn(i, n) forn(j, n)
			rot[j][i] = tab[n-i-1][j];
		
		forn(j, n) 
		{
			int nn = -1;
			dforn(i, n)
			{
				if(rot[i][j] == '.')
				{
					if(nn == -1) nn = i;
				}
				else if(nn != -1)
				{
					rot[nn][j] = rot[i][j];
					rot[i][j] = '.';
					--nn;
				}
			}
		}
		
/*		forn(i, n)
		{
			forn(j, n)
				cout << rot[i][j];
			cout << endl;
		}
		cout << endl;*/
		
		bool gr = win('R'), gb = win('B');
		
		if(gr && gb)
			printf("Case #%i: Both\n", p+1);
		else if(gr)
			printf("Case #%i: Red\n", p+1);
		else if(gb)
			printf("Case #%i: Blue\n", p+1);
		else
			printf("Case #%i: Neither\n", p+1);
		
	}
	
	return 0;
}
