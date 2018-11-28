#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int n, n2=0;
	scanf("%d\n",&n);
	while (n--) {
		int s;
		scanf("%d\n",&s);
		vector<int> a,b;
		for (int i=0; i<s; i++) {
			int t;
			scanf("%d\n",&t);
			a.push_back(t);
		}
		for (int i=0; i<s; i++) {
			int t;
			scanf("%d\n",&t);
			b.push_back(t);
		}
		sort(a.begin(),a.end());
		sort(b.begin(),b.end(),greater<int>());
		int R = 0;
		for (int i=0; i<s; i++) {
			R += a[i]*b[i];
		}
		// print result
		printf("Case #%d: %d\n",++n2,R);
	}
	return 0;
}

