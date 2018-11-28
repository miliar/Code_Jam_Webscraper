#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <memory.h>
using namespace std;

#define fi first
#define sc second
#define mp make_pair
#define pb push_back
#define ALL(c) (c).begin(), (c).end()
#define RESET(a,b) memset( (a), b, sizeof(a) )
#define ren(a,b,c) for (int a=b; a<c; ++a)
#define red(a,b,c) for (int a=b; a>=c; --a)
#define repi(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)

const double eps = 1e-9;
typedef long long ll;
typedef pair <int,int> pii;

//lintaor1's template

void solve( int );

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int TT;
	cin >> TT; ++TT;
	ren (T,1,TT) solve( T );
	return 0;
}

//-----
void solve( int T )
{
	int n;
	cin >> n;
	
	pii i[n+3];
	ren (x,0,n) scanf("%*d");
	ren (x,0,n) scanf("%d", &i[x].fi), i[x].fi *= -1, i[x].sc = x;
	sort( i, i+n );
	
	printf("Case #%d:", T);
	ren (x,0,n) printf(" %d", i[x].sc);
	printf("\n");
}
