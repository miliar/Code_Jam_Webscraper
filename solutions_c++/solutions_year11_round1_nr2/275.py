
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
	int n,m;
	REP(tc, t )
	{
		S("%d%d", &n, &m );
		vector<string> dict(n);
		REP(i, n ) cin >> dict[i];
		string Ans = "";
		string inp;
		string ans;
		REP(i, m )
		{
			int pl = -1;
			cin >> inp;
			ans = "-1";
			//ans = dict[0];
			REP(x, n )
			{
				int pointlose = 0;
				set<string> Words;
				int l = LEN(dict[x]);
				REP(j, n )
				{
					if( LEN(dict[j]) == l ) Words.insert(dict[j] );
				}
				REP(j, 26 )
				{
					char c = inp[j];
					string tmp;
					bool used, used1;
					used = used1 = false;
					vector<string> toRemove;
					EACH(it, Words) 
					{
						tmp = *it;
						REP(k, l )
						{
							if( tmp[k] == c ) used = true;
							if( dict[x][k] == c && tmp[k] != c )
							{
								toRemove.PB( tmp );
								break;
							}
							if( tmp[k] == c && dict[x][k] != c )
							{
								toRemove.PB( tmp );
								break;
							}
						}
					}
					REP(k, l )
					{
						if( dict[x][k] == c ) used1 = true;
					}
					if( used && !used1 ) pointlose++;
					REP(j, SZ(toRemove) ) Words.erase( toRemove[j] );
					if( SZ(Words) == 1 ) break;
				}
				if( pl < pointlose )
				{
					pl = pointlose;
					ans = dict[x];
				}
			}
			//char str[10];
			//sprintf(str, "%d", pl );
			if( i < m-1 )
			{
				Ans+= ans + " ";
			}
			else
			{
				Ans += ans;
			}
		}
		P("Case #%d: ", tc+1 );
		cout << Ans << endl;
	}
	return 0;
}
