#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	for(int c=0;c<t;c++) {
		int n;
		scanf("%d", &n);

		int lasto=0,lastot=0,lastbt=0,lastb=0,now=0;
		for(int i=0;i<n;i++) {
			int where;
			char who;
			scanf(" %c %d", &who, &where);
			if (who == 'O') {
				now = max(now, lastot + abs(where-lasto)) + 1;
				lasto = where;
				lastot = now;
			} else {
				now = max(now, lastbt + abs(where-lastb)) + 1;
				lastb = where;
				lastbt = now;
			}
		}
		printf("Case #%d: %d\n",c+1,now-1);
	}
	return 0;
}
