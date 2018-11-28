
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int n, a[505];
vector< pair<int,int> > sums;

void out(int i) {
	for (int j=0; j<n; j++) if (i & (1<<j)) {
		printf("%d ",a[j]);
	}
	printf("\n");
}

void solve(int t) {
	printf("Case #%d:\n", t);
	
	scanf("%d",&n);
	for (int i=0; i<n; i++)
		scanf("%d", a+i);
	
	sums.clear();
	for (int i=1; i<(1<<n); i++) {
		int su=0;
		for (int j=0; j<n; j++) 
			if (i & (1<<j))
				su +=a[j];
		sums.push_back(make_pair(su,i));
	}
	
	sort(sums.begin(), sums.end());
	for (int i=0; i<sums.size(); i++) {
		int su=sums[i].first;
		for (int j=i+1; j<sums.size() && sums[j].first==su; j++)
			if ( !(sums[i].second & sums[j].second) ) {
				out(sums[i].second);
				out(sums[j].second);
				return;
			}
	}
	printf("Impossible\n");
}

main() {
	int tc;
	scanf("%d",&tc);
	for (int t=1; t<=tc; t++) 
		solve(t);
} 
