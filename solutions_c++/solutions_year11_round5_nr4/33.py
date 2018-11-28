#ifdef DEBUG
	#define D(x...) fprintf(stderr,x);
#else
	#define D(x...) 0
#endif
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

char S[80];
long long ans;

void tryIt(int upto, long long val) {
	if (upto == strlen(S)) {
		long long lo = 1;
		long long hi = 1;
		while (hi*hi < val) hi *= 2;
		while (lo != hi) {
			// (lo-1)^2 < val <= hi^2
			long long mid = (lo+hi)/2;
			if (mid*mid >= val) {
				hi = mid;
			} else {
				lo = mid+1;
			}
		}
		if (hi*hi == val) ans = val;
		return;
	}
	if (S[upto] != '1') tryIt(upto+1,val*2);
	if (S[upto] != '0') tryIt(upto+1,val*2+1);
}

int main() {
	int nTests;
	scanf("%d ",&nTests);
	for (int test=1;test<=nTests;test++) {
		if (1) fprintf(stderr,"Case %d/%d\n",test,nTests);
		
		scanf("%s ",S);
		tryIt(0,0);

		vector<int> st;
		while (ans != 0) {
			st.push_back(ans%2);
			ans /= 2;
		}
		
		printf("Case #%d: ",test);
		for (int i = st.size()-1; i >= 0; i--) printf("%d",st[i]);
		printf("\n");
	}
}
