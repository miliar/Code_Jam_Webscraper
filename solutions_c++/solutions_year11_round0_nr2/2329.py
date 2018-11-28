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
	int c, d, n;
	char ch;
	REP(tc, t )
	{
		S("%d", &c );
		VS comb(c);
		REP(i, c ) cin >> comb[i];
		S("%d", &d );
		VS opp(d);
		REP(i, d) cin >> opp[i];
		vector<char> Ans;
		S("%d", &n );
		int l = 0;
		bool fl;
		map< PII, bool > M;
		REP(i, d )
		{
			M[ MP( opp[i][0], opp[i][1] ) ] = true;
			M[ MP( opp[i][1], opp[i][0] ) ] = true;
		}
		REP(i, n )
		{
			S(" %c", &ch );
			Ans.PB( ch );

			fl = true;
			while( fl )
			{
				if( (l=SZ(Ans )) >= 2 )
				{
					bool test = false;
					REP(j, c )
					{
						if( (comb[j][0] == Ans[l-1] && comb[j][1] == Ans[l-2]) || ( comb[j][1] == Ans[l-1] && comb[j][0] == Ans[l-2] ) )
						{
							Ans.pop_back(); Ans.pop_back(); Ans.PB( comb[j][2] );
							test = true;
							break;
						}
					}
					l = SZ( Ans );
					if( !test )
					{
						//REP(j, l-1 )
						FORD(j, l-2, 0 )
						{
							if( M[ MP( Ans[j], Ans[l-1] ) ] )
							{
								Ans.clear();
								test = true;
								break;
							}
						}
					}
					fl = test;
				}
				else
				{
					fl = false;
				}
			}
		}

		P("Case #%d: [", tc+1 );
		l = SZ( Ans );
		REP(i, l-1 ) P("%c, ", Ans[i] );
		if( l > 0 )
		{
		P("%c]\n", Ans[l-1] );
		}
		else
		{
			P("]\n");
		}
	}
	return 0;
}
