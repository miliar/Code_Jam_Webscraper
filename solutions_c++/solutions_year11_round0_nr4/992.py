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

int tab[1002];
int main(void) {
	int t;
	scanf("%d",&t);
	for (int tc=1; tc<=t; ++tc) {
					int n;
					scanf("%d",&n);
					for (int i=1; i<=n; ++i) {
									scanf("%d",tab+i);
					}
					int ret = 0;
					for (int i=1; i<=n; ++i) {
									for (int j=i; tab[j]!=j; ++ret) {
										int k=j;
										j = tab[j];
										tab[k] = k;
									}
					}
					printf("Case #%d: %.6lf\n",tc,(double)ret);
	}
	return 0;
}
