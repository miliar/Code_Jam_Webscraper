#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;
typedef long long ll;
typedef long double ld;

int N;

#define SMALL
#define LARGE
int main() {
	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("B-small-attempt0.in","rt",stdin);
	freopen("B-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
#endif

	cin >> N;
	for(int ii = 1 ; ii <= N ; ii++ ) {
		//cin>>c>>n;
		//for(int i = 0 ; i < n; i++)
		//	cin>>arr[i];
		ll n,k,b,t;
		cin >> n >> k >> b >> t;
		vector<ll> loc(n);
		for (int i = 0; i < n; ++i) {
			cin >> loc[i];
		}
		vector<ll> vel(n);
		for (int i = 0; i < n; ++i) {
			cin >> vel[i];
		}
		ll swaps = 0, slow = 0;
		for(int i = n-1 ;k > 0 &&  i>= 0 ; i-- ){
			cerr << t*vel[i] << endl;
			if( (b-loc[i]) <= t*vel[i] )
			{
				swaps += slow;
				k--;
			}else{
				slow++;
			}
		}
		printf("Case #%d: ", ii);
		if( k != 0 )
			printf("IMPOSSIBLE");
		else
			printf("%d",(int)swaps);
		printf("\n");
	}
	return 0;
}
