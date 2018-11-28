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

int X[105];
int main()
{
	freopen("d:/input.txt", "r", stdin);
	freopen("d:/output.txt", "w", stdout);

    int t, n, l, h;
    scanf("%d", &t);
    xrep(ncase,1,t)
    {

     scanf("%d %d %d", &n, &l, &h);

	 int ans;
	 rep(i,n)
		scanf("%d", &X[i]);	
	 bool ok = false;
	 xrep(i,l,h)
	 {
		bool  flag = true;
		rep(j,n) if ((i % X[j]) && (X[j] % i)) { flag = false; break; }
		if (flag)
		{
			ok = true;
			ans = i;
			break;
		}
	 }	 
	 
	 	printf("Case #%d: ",ncase);	 
	 if (!ok) printf("NO\n");
	 else
	 {
			printf("%d\n", ans);
	 }
	}
	 
}
