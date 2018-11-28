#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <string>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int, int> pii;
#define mp make_pair
#define pb push_back
#define iss istringstream
#define oss ostringstream
#define prv(vec) {for(int zz = 0; zz < vec.size(); ++zz) cout << vec[zz] << " "; cout << endl;}
#define sz(a) ((a).size())
#define len(a) ((a).length())
#define all(c) (c).begin(),(c).end() 
#define forn(i,a,n) for(int i = (int) a; i < (int)n; i++) 

vector <int> a;

int main()
{
	freopen("b2.in","rt",stdin);
    freopen("b2.out","wt",stdout); 
	int T,n,m,a;
	cin >> T;
	forn(t,0,T)
	{
		cin >> n >> m >> a;
		int solve = 0;
		forn(x2,0,n+1) forn(x3,0,n+1) forn(y2,0,m+1) forn(y3,0,m+1) if ( !solve )
		{
			if ( abs(x2*y3 - x3*y2) == a )
			{
					printf("Case #%d: %d %d %d %d %d %d\n",t+1,0,0,x2,y2,x3,y3);					
					solve = 1;
			}
		}
		if ( !solve ) printf("Case #%d: IMPOSSIBLE\n",t+1);					
	}
    return 0;
}