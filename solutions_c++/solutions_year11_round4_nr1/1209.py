
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

PIII A[1500000];
int main(int argc, char** argv)
{
	int t; S("%d", &t );
	int X, W, R, tym, N;
	REP(tc, t ) {
		P("Case #%d: ", tc+1 );
		S("%d%d%d%d%d", &X, &W, &R, &tym, &N);
		REP(i, N) S("%d%d%d", &A[i].first, &A[i].second.first, &A[i].second.second);
		sort(A, A+N);
		long double Ans = 0;
		long double lefttym = tym;
		int pos = 0;
		long double dl = 0;
		priority_queue< PII, vector<PII>, greater<PII> > PQ;
		REP(i, N) {
			if( pos != A[i].first ) {
				PQ.push( MP( 0, A[i].first - pos ) );
				pos = A[i].first;
				i--;
			}
			else {
				PQ.push( MP( A[i].second.second, A[i].second.first - A[i].first ));
				pos = A[i].second.first;
			}
		}
		if( X != pos ) {
			PQ.push( MP( 0,X - pos) );
		}
		while( !PQ.empty() ) {
			int speed = PQ.top().first;
			dl = PQ.top().second;
			PQ.pop();
			if( lefttym > 0 && dl/(R+speed) <= lefttym ) {
				lefttym -= dl/(R + speed);
				Ans += dl/(R + speed);
			}
			else {
				if( lefttym != 0 ) {
					dl = dl - (R+speed)*lefttym;
				}
				Ans += lefttym + dl/(W +speed);
				lefttym = 0;
			}
		}
		P("%.9Lf\n", Ans);
	}
	return 0;
}
