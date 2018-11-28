#include <cstdio>
#include <vector>
#include <queue>

using namespace std;

int main() {
	freopen("C-small.in", "r", stdin);
	int r, k, n, sum, totalsum;
	int testcases;
	int i, j, g;

	scanf("%d", &testcases);
	
	for ( j = 0; j < testcases; j++ ) {
		queue<int> q;
		vector<int> v;

		scanf("%d %d %d", &r, &k, &n);
		
		for ( i = 0; i < n; i++ ) {
			scanf("%d", &g);
			q.push(g);
		}
		totalsum = 0;
		
		while(r) {
			sum = 0;
			v.clear();

			while ( !q.empty() ) {
				if ( sum + q.front() > k )
					break;
				
				sum += q.front();
				v.push_back(q.front());
				q.pop();
			}

			for ( i = 0; i < v.size(); i++ )
				q.push(v[i]);

			totalsum += sum;
			r--;
		}
		printf("Case #%d: %d\n", j+1, totalsum);
	}

	return 0;
}
