#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <ctype.h>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <list>
#include <stack>
using namespace std;
#define PB			push_back
#define ALL(v)			(v).begin() , (v).end()
#define SZ(v)			( (int) v.size() )
#define Set(v,x)		memset(  v , x , sizeof(v))
#define two(n)			( 1 << (n) )
#define contain(S,i)		( (S) & two(i) ) 
#define SQR(v)			( (v) * (v) )
#define ABS(x)			( ( (x) >= 0 ) ? (x) : -(x) )
#define foreach(v,it)		for( typeof((v).begin()) it = (v).begin() ; it != (v).end() ; it++ )
#define MAX 1000100
int N,L, C, a[1010] , d[MAX];
long long t;

struct reg {
	int ind, dist;
	bool operator < (const reg &r) const {
		if (r.dist != dist)
			return dist > r.dist;
		return r.ind < ind;
	}
} w[MAX];
int nw;

void solve() {
	int i;
	long long res = 0;
	cin >> L >> t >> N >> C;
	for (i = 0 ; i < C ; i++)
		cin >> a[i];
	for (i = 0 ; i < N ; i++)
		d[i] = a[i%C];

	bool stop = false;
	for (i = 0 ; i < N ; i++) {
		if (res+d[i]*2 <= t )
			res += d[i]*2;
		else {
			stop = true;
			break;
		}
	}
	if (stop) {
	//	cout << " res = " << res << endl;
		t -= res;
		d[i] -= t/2;
		res += t;
		nw = 0;
		while (i < N ) {
			w[nw].ind = i;
			w[nw].dist = d[i];
			nw++;
			i++;
		}
		sort( w , w+nw);
	/*	printf("w: ");
		for (i = 0 ; i < nw ; i++) {
			printf("(%d,%d) ", w[i].dist, w[i].ind);
		}
		printf("\n");
		*/
		for (i = 0 ; i < L && i < nw; i++)
			res += w[i].dist;
		while (i< nw) {
			res += w[i].dist*2;
			i++;
		}
	}
	cout << res << endl;
}

int main() {
	int C , nc;
	
	scanf("%d\n", &C);
	for ( nc = 1 ; nc <= C ; nc++) {
		cout << "Case #" << nc << ": ";
		solve();
	}	
	return 0;
}
