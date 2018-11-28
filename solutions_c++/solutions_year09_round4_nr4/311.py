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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;

typedef long long ll;
typedef long double ld;
#define sz ((int)size())

int oo = (int)1e9;

#define SMALL
//#define LARGE

int x[41],y[41],r[41];

int main()
{
	freopen("a.txt","rt",stdin);
	#ifdef SMALL
	freopen("D-small-attempt0.in","rt",stdin);
	freopen("D-small.out","wt",stdout);
	#endif
	#ifdef LARGE
	freopen("D-large.in","rt",stdin);
	freopen("D-large.out","wt",stdout);
	#endif

	int t;
	scanf("%d ",&t);
	for (int i = 0; i < t; ++i) {
		printf("Case #%d: ",i+1);
		int n;
		scanf("%d",&n);
		int mxR = 0;

		for(int i = 0 ; i < n ; i++ ){
			cin >> x[i] >> y[i] >> r[i];
			mxR = max(mxR,r[i]);
		}
		if( n < 3 )
			cout << mxR << endl;
		else{
			double minR  = 1e9;
			minR = min(minR, max((hypot(x[0]-x[1],y[0]-y[1])+r[0]+r[1])/2.0, (double)r[2] ) );
			minR = min(minR, max((hypot(x[1]-x[2],y[1]-y[2])+r[1]+r[2])/2.0, (double)r[0] ) );
			minR = min(minR, max((hypot(x[0]-x[2],y[0]-y[2])+r[0]+r[2])/2.0, (double)r[1] ) );
			printf("%.6lf\n",minR);
		}
	}
	return 0;
}
