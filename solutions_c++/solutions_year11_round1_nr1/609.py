#include<iostream>
#include<cstring>
#include<map>
#include<algorithm>
#include<stack>
#include<queue>
#include<cmath>
#include<string>
#include<cstdlib>
#include<vector>
#include<cstdio>
#include<set>
#include<list>
#include<numeric>
#include<cassert>
#include<ctime>
#include<bitset>

using namespace std;

inline int gcd(long long  a, long long  b) 
{
	return b == 0 ? a : gcd(b, a % b);
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("in","r",stdin);
	freopen("out","w",stdout);
#endif

	int T, t= 1;
	cin>>T;
	for(long long pd,pg,n;T--; ){
		 cin>>n>>pd>>pg;
		printf("Case #%d: ", t++);
		long long p = 100 / gcd(pd, 100);
		if (p > n) {
			puts("Broken");
			continue;
		}
		if (pd != 0 && pg == 0) {
			puts("Broken");
			continue;
		}
		if (pd != 100 && pg == 100) {
			puts("Broken");
			continue;
		}
		puts("Possible");
	}
	return 0;
}