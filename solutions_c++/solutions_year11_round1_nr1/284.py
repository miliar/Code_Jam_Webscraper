
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
	LL n;
	int a, b;
	int t; S("%d", &t );
	REP(tc, t )
	{
		cin >> n >> a >> b;
		bool fl = true;
		P("Case #%d: ", tc+1 );
		if( n > 100 )
		{
		}
		else
		{
			bool xyz = false;
			FOR(i, 1, n+1 )
			{
				if( (i*a)%100 == 0 )
				{
					xyz = true;
					break;
				}
			}
			if( !xyz ) fl = false;
		}
		if( fl && b == 100 && a < 100 )
		{
			fl = false;
		}
		if( fl && b == 0 && a > 0 )
		{
			fl = false;
		}
		if( fl )
		{
			puts("Possible");
		}
		else
		{
			puts("Broken");
		}
	}
	return 0;
}
