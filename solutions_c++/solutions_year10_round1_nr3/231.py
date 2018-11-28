#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <algorithm>
#include <cmath>
#include <sstream>
using namespace std;

#define vi vector<int>
#define pb push_back
#define forn(i,a,b) for(int i = (int)a; i < (int)b; i++)
#define forn1(i,a,b) for(int i = (int)a; i >= (int)b; i--)
#define sz(a) (int)(a).size()
#define all(c) c.begin(), c.end()

int a[1000][1000];
int b[2000000],c[2000000],d[20000000];

int f ( int i, int j)
{
	if ( i < j ) swap(i,j);
	if ( j <= 0 ) return 1;
	if ( a[i][j] != -1 ) return a[i][j];
	int k = i;
	while ( k > 0 )
	{
		k -= j;
		if ( f(k,j) == 0 ) { a[i][j] = 1; return 1;	}
	}
	a[i][j] = 0;
	return 0;
}

int main()
{
	freopen("E:\\5.txt","rt",stdin);
	freopen("E:\\6.txt","wt",stdout);	
	int a1,a2,b1,b2,tr = 0;
	b[0] = 0;
	b[1] = 2;
	c[0] = 1;
	c[2] = 1;
	forn(i,2,1000001)
	{
		if ( c[i] ) { b[i] = b[i-1] + 2; d[ b[i] ] = i; d[ b[i] - 1] = i - 1; }
		else { b[i] = b[i-1] + 1; d[ b[i] ] = i; }
		c[ b[i] ] = 1;
	}
	d[2] = 1;
	//forn(i,1,100) cout << i <<" " << d[ i ] <<" " << b[i] << endl;
	int T;
	cin >> T;
	forn(numt,1,T+1)
	{
		cin >> a1 >> a2 >> b1 >> b2;
		long long ts = 0;
		forn(i,a1,a2+1) 
		{
			int l = d[i];
			int r = b[i];
			if ( b1 <= l && b2 <= l ) ts += b2 - b1 + 1;
			else if ( b1 <= l && b2 >= r ) ts += (l - b1 + 1) + (b2 - r + 1);
			else if ( b1 <= l ) ts += ( l - b1 + 1);
			else if ( b1 < r && b2 < r ) ts += 0;
			else if ( b1 < r && b2 >= r ) ts += (b2 - r + 1);
			else if ( b1 >= r ) ts += (b2 - b1 + 1);
		}
		cout <<"Case #" << numt << ": " << ts << endl;
	}
	return 0;
} 
