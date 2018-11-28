#include <stdio.h>
#include <stdlib.h>
#include <queue>
using namespace std;
struct Node {
	int x;
	int y;
}node;
int main() {

	int t, r, k, n, x, count, sum, icase=0;
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	scanf("%d", &t);
	while(t--) {
		scanf("%d%d%d", &r, &k, &n);
		queue<Node> q;
		for(int i=0; i<n; ++i) {
			scanf("%d", &node.x);
			node.y = -1;
			q.push(node);
		}
		count = sum = 0;
		for(int i=0; i<r; ++i) {
			node = q.front();
			while(node.x + count <= k && node.y < i) {
				node.y = i;
				count += node.x;
				q.push(node);
				q.pop();
				node = q.front();
			}
			sum += count;
			count = 0;
		}
		printf("Case #%d: %d\n", ++icase, sum);
	}
}
