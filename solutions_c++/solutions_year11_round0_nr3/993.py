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

int bits[30];
int main(void) {
	int t;
	scanf("%d",&t);
	for (int tc=1; tc<=t; ++tc) {
					for (int i=0; i<30; ++i) bits[i] = 0;
					int n;
					scanf("%d",&n);
					int m=100000000;
					int s=0;
					while (n--) {
									int c;
									scanf("%d",&c);
									m = min(m,c);
									s += c;
									for (int i=0; c; ++i,c>>=1) {
													if (c&1) ++bits[i];
									}
					}
					bool no=false;
					for (int i=0; !no && i<30; ++i) {
									if (bits[i]&1) no = true;
					}
					printf("Case #%d: ",tc);
					if (no) {
									printf("NO\n");
					} else {
									printf("%d\n",s-m);
					}
	}
	return 0;
}
