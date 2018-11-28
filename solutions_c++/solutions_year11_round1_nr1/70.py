#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <utility>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <cmath>

using namespace std;

int main(void) {
	int t;
	scanf("%d",&t);
	for (int tc=1; tc<=t; ++tc) {
		long long n;
		int d,g;
		scanf("%lld%d%d",&n,&d,&g);
		bool ok = true;
		if (g==0 || g==100) {
			if (d != g) {
				ok = false;
			}
		} else {
			int nn = 100;
			for (int i=2; i<=d; ++i) {
				while (!(d%i)) {
					d /= i;
					if (!(nn%i)) {
						nn /= i;
					}
				}
			}
			if (nn > n) {
				ok = false;
			}
		}
		printf("Case #%d: %s\n",tc,ok?"Possible":"Broken");
	}
	return 0;
}
