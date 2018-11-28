using namespace std;

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector> 

#define EPS 1e-11 
#define inf ( 1LL << 31 ) - 1
#define LL long long

#define _rep( i, a, b, x ) for( __typeof(b) i = ( a ); i <= ( b ); i += x )
#define rep( i, n ) _rep( i, 0, n - 1, 1 )
#define rrep( i, a, b ) for( __typeof(b) i = ( a ); i >= ( b ); --i )
#define xrep( i, a, b ) _rep( i, a, b, 1 )

#define abs(x) (((x)< 0) ? (-(x)) : (x))
#define all(x) (x).begin(), (x).end()
#define ms(x, a) memset((x), (a), sizeof(x))
#define mp make_pair
#define pb push_back
#define sz(k) (int)(k).size() 

typedef vector <int> vi;

char grid[55][55];
char ori[55][55];
bool used[55][55];

int main()
{
	freopen("d:/input.txt", "r", stdin);
	freopen("d:/output.txt", "w", stdout);
    int t, r, c;
    scanf("%d", &t);
    xrep(ncase,1,t)
    {

     bool ok = true;
     scanf("%d %d", &r, &c);
     rep(i,r) scanf("%s", grid[i]);
     rep(i,r) rep(j,c) ori[i][j] = grid[i][j];
     rep(j,c)
     {
		rep(i,r)
		if (grid[i][j] == '#')
		{
			grid[i][j] = '/';
			grid[i+1][j] = '\\';
			grid[i][j+1] = '\\';
			grid[i+1][j+1] = '/';
		}
	 }
	 rep(i,r) rep(j,c) used[i][j] = false;

	 
	 rep(j,c) if (ok) rep(i,r) 
	 {
		if (used[i][j]) continue;
		if (grid[i][j] == '#') 
		{
			ok = false;
			break;
		}
		if (grid[i][j] == '/')
		{
			if (j+1>=c) { ok = false; break; }
			if (grid[i][j+1] != '\\') { ok = false; break; }
			if (i+1>=r) { ok = false; break; }
			if (grid[i+1][j] != '\\') { ok = false; break; }
			if (grid[i+1][j+1] != '/') { ok = false; break; }
			used[i][j] = used[i+1][j] = used[i][j+1] = used[i+1][j+1] = true;
		}


	 }
	 
	 rep(i,r) rep(j,c)
	 {
		if (grid[i][j] == '/' && ori[i][j] != '#') ok = false;
		if (grid[i][j] == '\\' && ori[i][j] != '#') ok = false;
	 }
	 
	 printf("Case #%d:\n",ncase);	 
	 if (!ok) printf("Impossible\n");
	 else
	 {
		rep(i,r)
		{
			rep(j,c) printf("%c", grid[i][j]);
			printf("\n");
		}
	 }
	}
	 
}
