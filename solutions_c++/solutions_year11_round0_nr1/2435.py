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
	int t; S("%d", &t );
	char ch;
	int no;
	int bluepos, orngpos;
	int bluetime, orngtime;
	int tmp;
	
	REP(tc, t )
	{
		bluetime = orngtime = 0;
		bluepos = orngpos = 1;
		int n; S("%d", &n );
		REP(i, n )
		{
			S(" %c %d", &ch, &no );
			if( ch == 'B' )
			{
				tmp = abs( no - bluepos );
				bluetime = max( bluetime + tmp, orngtime );
				bluetime++;
				bluepos = no;
			}
			else
			{
				tmp = abs( no - orngpos );
				orngtime = max( orngtime + tmp, bluetime );
				orngtime++;
				orngpos = no;
			}
		}
		P("Case #%d: %d\n", tc+1, max( orngtime, bluetime ) );
	}
   return 0;
}
