#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <fstream>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> PI;
typedef vector<PI> VPI;
typedef unsigned long long ull;
typedef long long ll;

#define FOR(i, n) for(int i=0;i<(n);++i)
#define REP(i,s,n) for(int i=s;i<=n;++i)
#define SZ(x) ((int)(x).size())
#define LOOP(i,x) FOR(i,SZ(x))
#define IT(it,x) for(typeof((x).begin()) it = (x).begin();it!=(x).end();++it)
#define ALL(x) (x).begin(), (x).end()
#define ST first
#define ND second
#define MP make_pair
#define PB push_back

int case_number;
#define printg case_number++, printf("Case #%d: ",case_number), printf
#define gout case_number++, printf("Case #%d: ",case_number), cout

#define INF (1<<29)

void main2( void )
{
	int N, t;
	VI cd;
	cin >> N;
	int s = 0;
	FOR( i, N ) cin >> t, cd.PB( t ), s ^= t;
	if( s != 0 )
	{
		gout << "NO" << endl;
		return;
	}
	int i;
	sort( ALL( cd ) );
	long sm = 0;
	REP( i, 1, N - 1 ) sm += cd[ i ];
	gout << sm << endl;
}

int main()
{
	freopen( "C-large.in", "r", stdin );
	freopen( "C-large.out", "w", stdout );
	int T;
	scanf( "%d", &T );
	FOR( i, T ) main2();
	return 0;
}
