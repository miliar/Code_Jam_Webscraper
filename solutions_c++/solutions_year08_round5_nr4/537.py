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

	
int a[105][105];
int b[105][105];
int mod = 10007;

int main()
{
	freopen("xa2.in","rt",stdin);
    freopen("xa2.out","wt",stdout); 
	int T;
	cin >> T;
	forn(r,0,T)
	{
		int h,w,p,x,y;
		cin >> h >> w >> p;
		forn(i,1,h+1) forn(j,1,w+1) { a[i][j] = 0; b[i][j] = 0; } 
		forn(i,0,p) { cin >> x >> y; b[x][y] = 1; }
		a[1][1] = 1;
		forn(i,1,h+1) forn(j,1,w+1)
		{
			if ( b[i][j] ) continue;
			x = i - 2;
			y = j - 1;
			if ( x >= 1 && y >= 1 ) a[i][j] = (a[i][j] + a[x][y])%mod;
			x = i - 1;
			y = j - 2;
			if ( x >= 1 && y >= 1 ) a[i][j] = (a[i][j] + a[x][y])%mod;
		}
		//cout << "Case #" << r+1 <<": " << res << endl;
		printf("Case #%d: %d\n",r+1,a[h][w]);
	}
    return 0;
}