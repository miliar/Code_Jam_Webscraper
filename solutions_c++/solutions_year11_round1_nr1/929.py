#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <stack>
using namespace std;

int gcd(int a, int b){
	if (b == 0)
		return a;
	return gcd(b, a%b);
}

int main(){

	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	int cas = 1;
	int pd, pg;
	long long N;

	scanf("%d", &T);
	while (T--){
		scanf("%lld%d%d", &N, &pd, &pg);
		if (pg == 0 && pd == 0)
			printf("Case #%d: Possible\n", cas++);
		else if (pg == 0 && pd != 0)
			printf("Case #%d: Broken\n", cas++);
		else if (pd != 100 && pg == 100)
			printf("Case #%d: Broken\n", cas++);
		else {
			bool flag = false;
			int gc = gcd(pd, 100);

			long long fen = (long long)(100 / gc);
			if (fen <= N)
				printf("Case #%d: Possible\n", cas++);
			else 
				printf("Case #%d: Broken\n", cas++);
		}

	}
	return 0;
}