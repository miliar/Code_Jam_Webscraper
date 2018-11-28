#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;
typedef unsigned long long ull;
int const N = 1000;

int 	r, k, n;
int 	g[N+1];
int 	v[N+1];
ull 	w[N+1];

pair<int,int> solve(int i)
{
	int s = 0;
	int q = 0;
	while( q < n && g[i] <= k - s )
	{
		++q;
		s += g[i];
		i = (i + 1)%n;
	}
	return make_pair(s, i);
}

int main()
{
	cout.sync_with_stdio(false);
	
	int T;
	scanf("%d", &T);
	for( int C = 1; C <= T; ++C )
	{
		scanf("%d %d %d", &r, &k, &n);
		for( int i = 0; i != n; ++i )
			scanf("%d", &g[i]);

		memset(v, 0, sizeof(v));
		memset(w, 0, sizeof(w));
		
		ull rv = 0;
		int i = 0;
		int t = 1;
		while( r > 0 && v[i] == 0)
		{
			v[i] = t++;
			w[i] = rv;
			--r;
			
			pair<int,int> sol = solve(i);
			rv += sol.first;
			i 	= sol.second;
		}
		//cerr << "First phase done" << endl;
		//cerr << "Iterations finished: " << t-1 << endl;
		if( r > 0 )
		{
			int cl = t  - v[i];
			ull dw = rv - w[i];

			//cerr << "Cycle length: " << cl << endl;
			rv += (r/cl)*dw;
			r %= cl;
		}
		
		//cerr << "Remaining iteratios: " << r << endl;
		while( r > 0 )
		{
			--r;
			
			pair<int,int> sol = solve(i);
			rv += sol.first;
			i 	= sol.second;
		}
		
		cout << "Case #" << C << ": " << rv << '\n';
	}
	return 0;
}
