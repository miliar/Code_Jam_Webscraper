
/***** Author : Kunal *****/
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

#include <cmath>
#include <cstdio>
#include <queue>
#include <list>
#include <stack>
#include <utility>
#include <numeric>
#include <map>
#include <cctype>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <cassert>
#include <iomanip>
#include <set>
#include <fstream>

using namespace std;

#define F(a,b) for(int a=0;a<b;a++)
#define REP(a,b) for(int a=0;a<b;a++)
#define FOR(a,b,c) for(int a=b;a<c;a++)
#define FORD(a,b,c) for(int a=b;a>=c;a--)

#define S scanf
#define P printf

#define LEN(x) ((int)x.length())
#define SZ(x) ((int)x.size())
#define ALL(x) x.begin(), x.end()
#define MP(x,y) make_pair(x,y)
#define PB(x) push_back(x)
#define INF 1000000000

typedef long long LL;
typedef pair<int,int> PII;
typedef pair<int, PII> PIII;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<string> VS;

//int d[][2]={{-1.0},{1,0},{0,-1},{0,1}};

char A[100][100];
char tmp[100][100];
int n, m;
int _K;

int chk( int _n, int _m,  char test[100][100])
{
	bool fl1 = false, fl2 = false;
	int ctr1, ctr2;
	REP( i, _n ) 
	{
		ctr1 = ctr2 = 0;
		REP(j, _n)
		{
			if( test[i][j] == 'R' && ctr2 == 0 ) ctr1++;
			else if( test[i][j] == 'R' ) { ctr1 = 1; ctr2 = 0; }
			else if( test[i][j] == 'B' && ctr1 == 0 ) ctr2++;
			else if( test[i][j] == 'B' ) { ctr2 = 1; ctr1 = 0; }
			if( ctr1 == _K ) fl1 = true;
			if( ctr2 == _K ) fl2 = true;
		}
	}
	REP( j, _n ) 
	{
		ctr1 = ctr2 = 0;
		REP(i, _n)
		{
			if( test[i][j] == 'R' && ctr2 == 0 ) ctr1++;
			else if( test[i][j] == 'R' ) { ctr1 = 1; ctr2 = 0; }
			else if( test[i][j] == 'B' && ctr1 == 0 ) ctr2++;
			else if( test[i][j] == 'B' ) { ctr2 = 1; ctr1 = 0; }
			if( ctr1 == _K ) fl1 = true;
			if( ctr2 == _K ) fl2 = true;
		}
	}
	REP( i, _n ) 
	{
		REP(j, _n)
		{
		ctr1 = ctr2 = 0;
			REP(k, _K)
			{
				if( i+k>=0 && i+k<_n && j+k>=0 && j+k<_m )
				{
					if( test[i+k][j+k] == 'R' && ctr2 == 0 ) ctr1++;
					else if( test[i+k][j+k] == 'R' ) { ctr1 = 1; ctr2 = 0; }
					else if( test[i+k][j+k] == 'B' && ctr1 == 0 ) ctr2++;
					else if( test[i+k][j+k] == 'B' ) { ctr2 = 1; ctr1 = 0; }
					if( ctr1 == _K ) fl1 = true;
					if( ctr2 == _K ) fl2 = true;
				}
				else break;
			}
		}
	}
	REP( i, _n ) 
	{
		REP(j, _n)
		{
		ctr1 = ctr2 = 0;
			REP(k, _K)
			{
				if( i-k>=0 && i-k<_n && j+k>=0 && j+k<_m )
				{
					if( test[i-k][j+k] == 'R' && ctr2 == 0 ) ctr1++;
					else if( test[i-k][j+k] == 'R' ) { ctr1 = 1; ctr2 = 0; }
					else if( test[i-k][j+k] == 'B' && ctr1 == 0 ) ctr2++;
					else if( test[i-k][j+k] == 'B' ) { ctr2 = 1; ctr1 = 0; }
					if( ctr1 == _K ) fl1 = true;
					if( ctr2 == _K ) fl2 = true;
				}
				else break;
			}
		}
	}
	if( fl1 && fl2 ) return 3;
	if( fl1 ) return 1;
	if( fl2 ) return 2;
	return 0;
}

void rotate90()
{
	REP( i, m ) REP(j,n ) tmp[i][j] = '.';
	int i1, j1;
	j1 = 0;
	FORD(i, m-1, 0 )
	{
		i1 = n-1;
		FORD(j,n-1, 0 )
		{
			if( A[i][j] != '.' )
			{
				tmp[i1--][j1] = A[i][j];
			}
		}
		j1++;
	}
	int x =  chk( m, n, tmp ); 
	if( x == 0 ) P("Neither\n");
	if( x == 1 ) P("Red\n");
	if( x ==2 ) P("Blue\n");
	if( x==3) P("Both\n");
}

void rotate180()
{
	REP(i,n) REP(j,m) tmp[i][j] = '.';
	int i1 = 0, j1 = 0;
	FORD(i, m-1, 0)
	{
		j1 = 0;
		FORD(j, n-1, 0 )
		{
			if( A[i][j] != '.' )
			{
				tmp[i1][j1++] = A[i][j];
			}
		}
		i1++;
	}
}

void rotate270()
{
	REP( i, m ) REP(j,n ) tmp[i][j] = '.';
	int i1, j1;
	j1 = 0;
	FORD(i, m-1, 0 )
	{
		i1 = n-1;
		FOR(j,0, n-1)
		{
			if( A[i][j] != '.' )
			{
				tmp[i1--][j1] = A[i][j];
			}
		}
		j1++;
	}
	int x =  chk( m, n, tmp ); 
	if( x == 0 ) P("Neither\n");
	if( x == 1 ) P("Red\n");
	if( x ==2 ) P("Blue\n");
	if( x==3) P("Both\n");
}


int main()
{
	int t; S("%d", &t);
	REP(tc,t)
	{
		S("%d%d", &n, &_K);
		m = n;
		REP(i,n) S("%s", A[i]);
		P("Case #%d: ", tc+1);
		rotate90();
	}
	return 0;
}
