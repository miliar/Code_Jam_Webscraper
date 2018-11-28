#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <algorithm>	// require sort next_permutation count __gcd reverse etc.
#include <cstdlib>	// require abs exit
#include <cstdio>	// require scanf printf
#include <functional>
#include <numeric>	// require accumulate
#include <cmath>
#include <climits>
#include <limits>
#include <cfloat>
#include <iomanip>	// require setw
#include <sstream>	// require stringstream 
#include <cstring>	// require memset
#include <cctype>	// require tolower, toupper
#include <fstream>	// require freopen
#include <ctime>
#define rep(i,n) for(int i=0;i<(n);i++)
#define ALL(A) A.begin(), A.end()
#define DEBUG 0

using namespace std;

typedef long long ll;
typedef pair<int, int> P;
const double INF = 1e100;

int main()
{
//	cut here before submit 
//	freopen ("testcase.A", "r", stdin );
	freopen ("A-small-attempt0.in", "r", stdin );
	int t;
	cin >> t;
	for (int Case = 1; Case <= t; Case++ ){
		int n, m;
		cin >> n >> m;
		vector<double> pa (n, 0.0 ); 
		rep (i, n ){
			cin >> pa[i];
		} // end rep
		double res = INF;
		for (int c = 0; c <= n+1; c++ ){
			double expect = 0.0;
			for (int i = 0; i < 1<<n; i++ ){
				double tp = 1.0;
				int last_bit = -1;
				for (int j = 0; j < n; j++ ){
					if (i&(1<<j) ){ // ビットが立っている所は間違っているところ
						tp *= (1. - pa[n-1-j] );
						last_bit = j;
					}else{
						tp *= pa[n-1-j];
					} // end if
				} // end for
#if DEBUG
				cout << "tp: " << tp << endl;
#endif
				int cnt = __builtin_popcount (i );
				double k1 = (double)((m-n) + 1 + (cnt == 0 ? 0 : m+1 ) );
				double k = 0;
				if (cnt == 0 ){
					k = (double)((m-n) + 1 + 2*c );
				}else{
					k = (double)((m-n) + 1);
					if (last_bit+1 <= c && cnt <= c ){
						k += (double)(2*c );
					}else{
						k += (double)(c + 1 + m + 1 );
					} // end if
/*
					if (cmp == i && (i & cmp ) == cmp && cnt <= c ){
						k += (double)(2*cnt);
					}else{
						k += (double)(c + 1 + m+1  );
					} // end if
*/
				} // end if
				double kn = (double)(1 + m + 1);
//				cout << "k1: " << k1 << endl;
//				cout << "kn: " << kn << endl;
//				switch (c ){
				if (c == 0 ){
#if DEBUG
					cout << "k1: " << k1 << endl;
#endif
					expect += k1*tp; 
				}else
				if (c == n+1 ){
#if DEBUG
					cout << "kn: " << kn << endl;
#endif
					expect += kn*tp;
				}else{
#if DEBUG
					cout << "k:  " << k << endl;
#endif
					expect += k*tp;
				} // end end if
			} // end for
#if DEBUG
			cout << "expect: " << expect << endl;
#endif
			res = min (res, expect );
		} // end for
							
//		cout << "Case #" << Case << ": " << res << endl;
		printf ("Case #%d: %0.8f\n", Case, res );
	} // end loop

//	cout << res << endl;	
		
	return 0;
}
