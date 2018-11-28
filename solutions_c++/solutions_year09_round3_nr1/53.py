#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>
#include <cstring>
using namespace std;

int main() {
	int cas, cass=0;
	for (scanf("%d", &cas); cas--; ) {
		printf("Case #%d: ", ++cass);
		string s,t ;
		cin>>s;
		int d[200];
		int used[200];
		memset(d, -1, sizeof(d));
		memset(used, 0, sizeof(used));
		d[s[0]] = 1;
		used[1] = 1;
		int n = -1;
		for (int i=1; i<s.size(); ++i) {
			if (d[s[i]]>=0) continue;
			++n;
			if (n==1) ++n;
			d[s[i]] = n;
		}
		++n;
		if (n<=1) n = 2;
		long long res = 0;
		for (int i=0; i<s.size(); ++i) {
			res = res * n + d[s[i]];
//			cout<<s;
//			printf("%d ", d[s[i]]);
		}

		printf("%lld\n", res);
	}
	return 0;
	
}
				
