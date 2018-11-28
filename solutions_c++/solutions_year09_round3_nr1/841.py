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

// She
// May be the reason I survive
// The why and wherefore I'm alive
// The one I'll care for through the rough in ready years

//...
LL bp[38][65];

void pc()
{
		rep(i, 37) bp[i][0] = 1;
	xrep(k, 2, 37) xrep(i, 1, 62) bp[k][i] = bp[k][i-1]*k;	
}

int main()
{
	int t;
	string x;
	freopen("f:/data/basel.txt", "r", stdin);
	freopen("f:/data/baseo2.txt", "w", stdout);
	pc();
	cin>>t;

	xrep(T,1, t)
	{
		cin>>x;
		int n = sz(x);
		map<char, int> value;
		value[x[0]] = 1;
		int b = 0;
		rep(i, n)
		{
			if (value.find(x[i]) != value.end()) continue;
			value[x[i]] = b;
			b++;
			if (b == 1) b++;
		}
		
		LL num = 0;
		if (b == 0) b = 2;
		rep(i, n) num += bp[b][n - i - 1] * (value[x[i]]);
		cout<<"Case #"<<T<<": ";
		printf("%I64d\n", num);
	}

	return 0;
}
