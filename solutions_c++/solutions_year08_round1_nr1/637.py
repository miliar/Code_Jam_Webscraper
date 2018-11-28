#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(int a, int b) {
	return a > b;
}

int main() {
	int cases, t = 1, n, i;
	long long ans;
	
	scanf("%d",&cases);
	while (cases--) {
		scanf("%d",&n);
		vector <int> x(n), y(n);
		
		for (i=0; i < n; i++)
			scanf("%d",&x[i]);
		for (i=0; i < n; i++)
			scanf("%d",&y[i]);
		
		sort(y.begin(),y.end());
		sort(x.begin(),x.end(),cmp);
		
		ans = 0;
		for (i=0; i < n; i++)
			ans += x[i]*y[i];
		
		printf("Case #%d: %lld\n",t++,ans);
	}
	
	return 0;
}
