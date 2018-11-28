
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

#define LET(x,a) __typeof(a) x(a)
#define IFOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define EACH(it,v) IFOR(it,v.begin(),v.end())
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

//int d[][2]={{-1,0},{1,0},{0,-1},{0,1}};

int main(int argc, char** argv)
{
	string A[100];
	int t; S("%d", &t );
	int d[][2] = { {0, 0}, {0, 1}, {1, 0}, {1,1} };
	REP(tc, t )
	{
		int n, m;
		S("%d%d", &n, &m );
		REP(i, n ) cin >> A[i];
		int hashct = 0;
		REP(i, n ) REP(j, m ) if( A[i][j] == '#' ) hashct++;
		P("Case #%d:\n", tc+1 );
		if( hashct%4 != 0 )
		{
			puts("Impossible");
		}
		else
		{
			vector<VB> vis(n, VB(m) );
			int ti, tj;
			bool fl = true;
			REP(i, n )
			{
				REP(j, m )
				{
					if( !vis[i][j] && A[i][j] == '#' )
					{
						REP(k, 4 )
						{
							ti = i+d[k][0];
							tj= j+d[k][1];
							if( ti>=0 && ti < n && tj >=0 && tj < m && A[ti][tj] == '#' )
							{
								vis[ti][tj] = true;
							}
							else
							{
								fl = false;
							}
						}
						if( fl )
						{
							A[i][j] = '/';
							A[i][j+1] = '\\';
							A[i+1][j] = '\\';
							A[i+1][j+1] = '/';
						}
					}
				}
			}
			if( fl )
			{
				REP(i, n ) cout << A[i] << endl;
			}
			else
			{
				puts("Impossible");
			}
		}
	}
	return 0;
}
