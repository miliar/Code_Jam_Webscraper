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
#include <iostream>
#include <climits>
#include <cstring>
using namespace std;

#define forn(a, n) for(int a = 0; a<(n); ++a)
#define forsn(a,s,n) for(int a = (s); a<(n); ++a)
#define forall(a, all) for(typeof((all).begin()) a = (all).begin(); a != (all).end(); ++a)

#define dforn(a, n) for(int a = (n)-1; a>=0; --a)
#define dforsn(a,s,n) for(int a = (n)-1; a>=(s); --a)
#define dforall(a, all) for(typeof((all).rbegin()) a = (all).rbegin(); a != (all).rend(); ++a)

#define contains(mask, bit) ((mask & (1LL<<bit)) != 0LL)

typedef long long tint;
typedef long double ld;

ld rpi(ld WP, ld OWP, ld OOWP){
	return 0.25 * WP + 0.50 * OWP + 0.25 * OOWP;
}

ld wps[104], owps[104];
string match[104];

ld calcwp(int index, int no=-1){
	ld ret = 0.0, div = 0.0;
	
	forn(i, match[index].size())
		if(match[index][i] != '.' && i != no){
			div++;
			if(match[index][i] == '1')
				ret++;
		}
	return ret/div;
}

int main()
{
#ifdef _TAVO92_
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif

	int t;
	cin >> t;
	forn(p,t){
		printf("Case #%i:\n", p+1);
		int n;
		cin >> n;
		forn(i,n) cin >> match[i];
		forn(i,n){
			wps[i] = calcwp(i);
			double sum=0.0,div=0.0;
			
			forn(j, n) if(match[i][j] != '.'){
				div++;
				sum += calcwp(j, i);
			}
			owps[i] = sum/div;
		}
		
		forn(i, n){
			double sum=0.0,div=0.0;
			forn(j,n) if(match[i][j] != '.'){
				sum += owps[j];
				div++;
			}
//			cout << wps[i] << " " << owps[i] <<  " " << sum/div << endl;
//			printf("%.6f\n", double(rpi(wps[i], owps[i], sum/div)));
//			cout.precision(7);
			cout << rpi(wps[i], owps[i], sum/div) << endl;
		}
	}

	return 0;
}
