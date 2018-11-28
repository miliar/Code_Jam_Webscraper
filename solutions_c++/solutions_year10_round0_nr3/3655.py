#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef long int ULONG;

// MACROS
#define PRunsigned(X, K) cout << "Case #" << X << ": " << K << endl;
#define FOR(i, a, b) for(ULONG i=(a); i<(b);++i)
#define FOREACH(T, I, J) for (T::iterator I = J.begin(); I != J.end(); ++I)
#define FOREACH_B(T, I, S, E) for (I = S; I != E; ++I)
#define FOREACH_CONST(T, I, J) for (T::const_iterator I = J.begin(); I != J.end(); ++I)
#define PRunsigned_COLLECTION(T, C) for(T::iterator it=C.begin(); it!=C.end(); ++it) cout << " " << *it;

#define MAX_R 100000000
#define MAX_K 1000000000
#define MAX_N 1000
#define MAX_G 10000000


int main() {

	
	ULONG t,T,R,r,k,N,n,m,gi,p,lim,in,inq,v; cin >> T;
	ULONG que[MAX_N];
	ULONG pos[MAX_N];
	ULONG val[MAX_N];
	FOR(t, 0, T) {
		cin >> R >> k >> N;
		FOR(n, 0, N) { cin >> gi; que[n] = gi; }
		memset(pos, 0, N);
		memset(val, 0, N);
		
		//cout << "K = " << k << "; R = " << R << endl;
		
		// get indexes
		FOR(n, 0, N) {
			p = n; lim = k; in = 0; v = 0;
			//cout << "Sequence (lim = " << lim << "):";
			while (lim >= 0 && in < N) {
				inq = (p++)%N;
				lim -= que[inq];
				if (lim >= 0) {
					v += que[inq];
					in++;
					//cout << " " << que[inq] << "(lim = " << lim << ")";
				}
			}
			pos[n] = in; val[n] = v;
			//cout << endl;
		}
		
		// START TEH ROLAR COSTAR
		p = 0; v = 0;
		FOR(r, 0, R) {
			v += val[p % N];
			p += pos[p % N];
		}
		cout << "Case #" << t+1 << ": " << v << endl;
		
	}

	return 0;
	
}

