#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <queue>
#include <complex>
#include <queue>
#include <string.h>
#include <fstream>
using namespace std;

#define IT(c) typeof((c).begin())

#define For(i, a, b) for(int (i) =  int(a); i < int(b); ++i)
#define rep(x, n) For(x,0,n)
#define forit(c, i) for(IT(c) i = (c).begin(); i != (c).end(); ++i)

#define bound(num, lower, upper) (max(min((num),((upper)-1)),(lower)))
#define debug(x) cerr << #x << " = " << x << "\n"

#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define clear(c) memset(c, 0, sizeof(c));
#define mp make_pair

typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<string> vs;
typedef pair<int, int> ii;

/*==================================================================================================================*/

int main()
{
int numprob; cin >> numprob;
rep(probnum, numprob)
{
	cerr << "proc: " << (probnum + 1) << endl;
	long long d[500];
	for(int i = 1; i < 500; i ++)
	{
		int cost = 0;
		int w = 1;
		for(int r = 1; r < i; r++)
		{
			cost += w*2;
			w += 1;
		}
		cost += i;
		d[i] = cost;
		//cerr << i << " " << cost << endl;
	}
	
	
	int n; cin >> n;
	vector<vector<int> > v(2*n, vector<int>());
	
	For(i, 1, 2*n)
	{
		int spacerep = i <= n ? n - i : i - n;
		rep(k, spacerep)
			v[i].pb(-2);

		int rep = i <= n ? i : 2*n - i;
		rep(k, rep)
		{
			if(k) v[i].pb(-2);
			int t; cin >> t;
			v[i].pb(t);
		}

		rep(k, spacerep)
			v[i].pb(-2);
		rep(c, 2*n - 1)
			cerr << v[i][c] << " ";
		cerr << endl;
	}
	
	long long best = -1;

	rep(c, 2*n - 1)
	{
		bool valid = true;
		For(r, 1, 2*n)
		{
			for(int i = c, k = c; i >= 0 && k < 2*n - 1; i--, k++)
				if(v[r][i] != -2 && v[r][k] != -2 && v[r][i] != v[r][k])
				{
					valid = false;
				}
		}
		if(!valid) continue;
		
		//cout << "col " << c << endl;

		for(int r = 1; r < 2*n; r++)
		{
			valid = true;
			for(int i = r, k = r; i >= 1 && k < 2*n; i--, k++)		//!!!!!!!!!!!!!!!!
			{
				rep(tc, 2*n - 1)
				{
					if(v[i][tc] != -2 && v[k][tc] != -2  && v[i][tc] != v[k][tc]) valid = false;
				}
			}
			if(!valid) continue;

			cerr << "center: " <<  c << " " << r << endl;
			
			long long cost = 0;

			int newheight = (abs(c - (n-1)) + abs(r - n)) + n;

			cost = d[newheight] - d[n];
			
			if(cost < best || best == -1)
			{
				best = cost;
				cerr << r << " " << c << " " << newheight << endl;
			}
		}
	}

	printf("Case #%d: %lld", probnum + 1, best);

	cout << endl;
}
}
