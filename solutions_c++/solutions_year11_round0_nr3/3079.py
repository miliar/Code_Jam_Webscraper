
#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <queue>
#include <set>
#include <cstring>
#include <sstream>
#include <cassert>
#include <map>
#include <stack>

#define FOR(I,A,B) for(int I=(A);I<(B);I++)
#define REP(I,N) FOR(I,0,N)
#define ALL(A) (A).begin(),(A).end()

#define SQR(x) ((x)*(x))
#define PB(x) push_back(x)

#define PI (acos(-1.0))

using namespace std;

typedef vector<int> VI;
typedef vector< vector<int> > VVI;

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int testcase;
	cin >> testcase;
	for(int tc=1;tc<=testcase;tc++) {
		int N;
		cin >> N;
		int result = -1;
		int C[1000];
		REP(i,N) cin >> C[i];
		int allsum = 0;
		REP(i,N) allsum+=C[i];
		for(int bin = 1;bin<(1<<N)-1;bin++) {
			int seansum = 0;
			int pattsum = 0;
			int sum = 0;
			for(int bit = 0;bit<N;bit++) {
				if((bin >> bit) & 1) {
					seansum ^= C[bit];
					sum += C[bit];
				}
				else {
					pattsum ^= C[bit];
				}
			}
			if((seansum == pattsum)) {
				result = max(result,sum);
			}
		}
		if(result == -1) printf("Case #%d: NO\n",tc);
		else printf("Case #%d: %d\n",tc,result);
	}
}
