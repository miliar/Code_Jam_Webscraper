#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <cmath>
using namespace std;
int main() {
	int T;
	scanf("%d",&T);
	for(int cn=1;cn<=T;++cn) {
		int N, xs = 0, s = 0, m = INT_MAX;
		scanf("%d",&N);
		for(int i=0;i<N;++i) {
			int a;
			scanf("%d",&a);
			xs ^= a;
			if(a < m) m = a;
			s += a;
		}
		printf("Case #%d: ",cn);
		if(xs) printf("NO\n");
		else printf("%d\n",s-m);
	}
}
