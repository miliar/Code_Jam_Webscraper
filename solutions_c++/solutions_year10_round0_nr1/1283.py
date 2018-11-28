#define DEBUG 1

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

#define _rep(i, a, b, x) for(int i(a), _b(b); i <= _b; i += x )
#define rep(i, n) _rep( i, 0, n - 1, 1 )
#define rrep(i, a, b) for(int i(a),_b(b); i >= (_b); --i)
#define xrep( i, a, b ) _rep(i, a, b, 1)
#define foreach(type, v, it) for(type::iterator it = v.begin(); it!=v.end(); ++it)

#define abs(x) (((x)< 0) ? (-(x)) : (x))
#define all(x) (x).begin(), (x).end()
#define ms(x, a) memset((x), (a), sizeof(x))
#define mp make_pair
#define pb push_back
#define sz(k) (int)(k).size()

#define dbg(x) if(DEBUG) cerr << __LINE__ << ": " << #x << " -> " << (x) << "\t";
#define dbge(x) if(DEBUG) cerr << __LINE__ << ": "<<#x << " -> " << (x) << endl;


typedef vector <int> vi;

// She
// May be the reason I survive
// The why and wherefore I'm alive
// The one I'll care for through the rough in ready years

//...

int main()
{
	freopen("f:/data/A-large.in.txt","r",stdin);
	freopen("f:/data/aout.txt","w",stdout);
	int t;
	int n,k;
	scanf("%d", &t);
	
	xrep(ca,1,t)
	{
		
		scanf("%d %d",&n,&k);
		
		LL mod = (1LL<<n);
		LL r = ((LL)k) % mod;
		printf("Case #%d: ",ca);
		if (r == mod-1) printf("ON");
		else printf("OFF");
		printf("\n");
		
	}
	
	
	
	
	
	
	return 0;
}
