#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <map>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <string>
#include <iostream>
#include <sstream>
#include <algorithm>
using namespace std;

int main() {
//	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("A-small.out","w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int i=1; i<=cas; ++i) {
		printf("Case #%d: ", i);
		int n, k;
		scanf("%d %d", &n, &k);
		int m = 1<<n;
		++k;
		if (k%m==0) puts("ON");
		else puts("OFF");
	}
	return 0;
}
