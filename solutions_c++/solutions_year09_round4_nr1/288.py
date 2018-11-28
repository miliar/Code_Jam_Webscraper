#include  <cstdio>
#include  <cstdlib>
#include  <string>
#include  <cmath>
#include  <inttypes.h>
#include  <ctype.h>
#include <algorithm>
#include <utility>
#include <iostream>
#include <vector>

using namespace std;

#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << "\n")

#define tr(it,s) for(typeof(s.begin())it=s.begin();it!=s.end();++it)
#define rep(i,n) for(int i=0; i<n; ++i)

const int INF = 0x3F3F3F3F;
const int NULO = -1;
const double EPS = 1e-10;

inline int cmp(double x, double y = 0, double tol = EPS) {
  return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1; }
  

main() {
	int T, N;
	string s;
	int P[100];
	
	cin >> T;
	
	rep(t,T) {
		cin >> N;
		rep(i,N) {
			cin >> s;
			P[i] = 0;
			rep(j,N) {
				if (s[j] == '1') P[i] = j;
			}
		}
		
		int ans = 0;
		
		rep(i,N) {
			int j = i;
			for(;(j<N) && (P[j]>i) ;++j);
			ans += j-i;
			int PP = P[j];
			for (int k = j; k > i; --k) P[k] = P[k-1];
			P[i] = PP; 
		}
		
		cout << "Case #" << t+1 << ": " << ans << endl;
		
		
		
	}
}
