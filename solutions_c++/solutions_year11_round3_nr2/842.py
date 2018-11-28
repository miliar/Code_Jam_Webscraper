#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <deque>
#include <queue>
#include <hash_map>
#include <hash_set>
#include <algorithm>
#include <climits>
#include <stdlib.h>

using stdext::hash_map;
using stdext::hash_set;
using namespace std;

int gcd (int m, int n) { 
	while (n!=0) { int t = m % n; m=n; n=t; } 
	return m; 
} 


/* 
2 20 8 2 3 5
1 4 2 2 10 4

out << setiosflags(ios::fixed) << setprecision(7)
*/
typedef long long LONGINT;

LONGINT fun(int l, LONGINT t, int N, vector<int>& dist, int pos, LONGINT usedt, int useds)
{
	if (pos == N) return usedt;
	if ( useds < l )
	{
		if ( t > usedt )
		{
		  if (dist[pos] > (t-usedt)/2)
		  return min( fun(l,t,N,dist,pos+1, usedt+dist[pos]*2, useds),
			          fun(l,t,N,dist,pos+1, t - (t - usedt)/2 + dist[pos], useds+1) );
		  else
		  return fun(l,t,N,dist,pos+1, usedt+dist[pos]*2, useds);
		}
		else // t <= usedt
		{
			return min( fun(l,t,N,dist,pos+1, usedt+dist[pos]*2, useds),
			            fun(l,t,N,dist,pos+1, usedt+dist[pos], useds+1) );
		}
	}
	else
	{
		return fun(l,t,N,dist,pos+1, usedt+dist[pos]*2, useds);
	}
}

void calculate( istream& in, ostream& out )
{
	int l,N,c;
	LONGINT t;
	in >> l >> t >> N >> c;

	//memset(state, -1, sizeof(state));

	vector<int> dist;
	for (int i = 0; i < c; ++i)
	{
		dist.push_back(0);
		in >> dist.back();
	}

	int j = 0;
	for (int i = c; i < N; ++i, ++j)
	{
		dist.push_back(dist[j%c]);
	}

	out << fun(l,t,N,dist,0,0,0);

}

int main( int argc, char *argv[] )
{
	unsigned cases;
	cin >> cases;
	for ( unsigned i = 1; i <= cases; ++i )
	{
		cout << "Case #" << i << ": "; 
		calculate( cin, cout );
		cout << endl;
	}

	return EXIT_SUCCESS;
}
