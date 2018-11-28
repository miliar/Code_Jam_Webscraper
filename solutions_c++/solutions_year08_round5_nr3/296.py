#include <string>
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
using namespace std;

typedef long long 	i64;
typedef pair <int, int> pii;
typedef vector <int>		vi;
typedef vector <string>		vs;
int 	dx[] = { 0, 0, -1,-1};
int 	dy[] = {-1, 1, -1, 1};

const int MN = 11;

int 	cas, T;

int 	m, n;
char 	mp[15][15];

int 	st[15][1 << 11];
int 	bit[1 << 11];
int 	best;
int		posk[15], posj[15], add;

void	prt_case()
{		
	printf("Case #%d: %d\n", ++T, best);
}

bool 	ok(int 	sj, int sk, int om)
{
	int 	i, j, k;
	
	add = 0;
	memset(posk, 0, sizeof(posk));
	memset(posj, 0, sizeof(posk));
	for (i=0; i<n; i++)
	{
		if ((1<<i) & sk)
		{
			posk[i] = 1;
			add++;
		}
		if ((1<<i) & sj)	posj[i] = 1;
		
		if (posk[i] == 1 && mp[om][i] == 'x')	return false;
	}
	
	for (i=0; i<n; i++)
	{
		if (posk[i] == 0)	continue;
		
		if (i > 0 && posk[i-1] == 1)	return false;
		if (om != 0 &&  i > 0 && posj[i-1] == 1)	return false;

		if (i < n-1 && posk[i+1] == 1)	return false;		
		if (om != 0 && i < n-1 && posj[i+1] == 1)	return false;
	}
	return true;
}

int main()
{
	int 	i, j, k;
	
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C_s_22222222222.out", "w", stdout);

	
	for (scanf("%d", &cas); cas; cas--)
	{
		scanf("%d %d", &m, &n);
		for (i=0; i<m; i++)
			scanf("%s", mp[i]);
		
		memset(st, 0xff, sizeof(st));
		st[0][0] = 0;
		
		int 	sz = 1 << n;
		for (i=0; i<m; i++)
		{
			for (j=0; j<sz; j++)	// c_s
			{
				if (st[i][j] == -1)	continue;
					
				for (k=0; k<sz; k++)	// new_state
				{
					if (ok(j, k, i) == false)	continue;
					int 	temp = st[i][j] + add;
					
					st[i+1][k] = max(st[i+1][k], temp);
				}
			}
		}
		
		best = 0;
		for (i=0; i<sz; i++)
		{
			best = max(best, st[m][i]);
		}
		prt_case();
		
	}
	return 0;
}
