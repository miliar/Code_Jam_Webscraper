#include <iostream>
#include <cstdio>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <cstring>
#include <string.h>
#include <cstdlib>
#include <sstream>
#include <stack>
#include <queue>
#include <numeric>
#include <utility>
#include <cctype>
#include <list>
#include <limits.h>
#include <signal.h>
#include <map>
#include <set>

#define TR(c, i) for ( typeof((c).begin()) i = (c).begin(); i != (c).end(); i++ ) 
#define FOR(i, a, b) for ( i = a; i <= b; i++ )
#define ROF(i, a, b) for ( i = a; i >= b; i-- )
#define ALL(v) (v).begin(), (v).end()
#define SORT(v) sort( ALL(v) )
#define MAX(a, b) ((a) >= (b) ? (a) : (b))
#define MIN(a, b) ((a) <= (b) ? (a) : (b))
#define ABS(a) ((a) < (0) ? (a)*(-1) : (a))
#define SWAP(a, b) typeof(a) T; T=a; a=b; b=T;

using namespace std;

int main()
{
	int T;
	cin >> T;
	int test = 0;
	while(T--){
		test++;
		
		int n, l, h;
	        cin >> n >> l >> h;

		int *A = new int[n];
		for(int i = 0;i<n;i++)
			cin >> A[i];

		int f = 0;
		int ans = 0;
		for(int i=l;i<=h;i++){
			f = 1;
			for(int j=0;j<n;j++){
				if(i%A[j] == 0 || A[j]%i == 0)
					continue;
				f = 0;
			}
			if(f == 1){
				ans = i;
				break;
			}
		}
//		cout << ans<<"\n";

		printf("Case #%d: ", test);
//		cout <<"lll";
		if (ans){
			cout << ans << "\n";
		}
		else 
			cout << "NO\n"; 
	}
	return 0;
}
