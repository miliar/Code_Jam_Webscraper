#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>
#include <cstring>
#include <cmath>

typedef unsigned long long ULL;
typedef long long LL;
typedef unsigned long UL;
typedef unsigned int UI;
typedef unsigned short US;
typedef unsigned char UC;

#define rep(i,a,b) for(int i=a;i<b;i++)

using namespace std;

char m[600][600];
int R, C, D;

int ok(int r, int c, int k) {
	LL rsum = 0, csum = 0;
	
	rep(rr,0,k) {
		rep(cc,0,k) {
			if((rr==0 || rr==k-1) && (cc==0 || cc==k-1)) continue;
			int mm = m[r+rr][c+cc]-'0';
			rsum += mm * (2*rr-(k-1));
			csum += mm * (2*cc-(k-1));
		}
	}
	//cout << k << "," << r << "," << c << ":" << rsum << "," << csum << endl;
	return rsum==0 && csum==0;
}

int solve(int no)
{
	cin >> R >> C >> D;
	
	rep(r,0,R) {
		cin >> m[r];
	}
	
	int K = -1;
	
	rep(k,3,min(R,C)+1) {
		rep(r,0,R-k+1) {
			rep(c,0,C-k+1) {
				if(ok(r,c,k)) {
					K=k;
					goto nextk;
				}
			}
		}
nextk:;
	}
	
	if(K>=0) {
		cout << "Case #" << no << ": " << K << endl;
	} else {
		cout << "Case #" << no << ": IMPOSSIBLE" << endl;
	}
}

int main()
{
	int T;
	cin >> T;
	rep(no,0,T) {
		solve(no+1);
	}
	return 0;
}
