#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <utility>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <cmath>

using namespace std;

int main(void) {
	int t;
	scanf("%d",&t);
	for (int tc=1; tc<=t; ++tc) {
					int n;
					int ret = 0;
					scanf("%d",&n);
					int position[2];
					position[0] = position[1] = 1;
					int  waiting[2];
					waiting[0] = waiting[1] = 0;
					while (n--) {
									char r[10];
									int p;
									scanf("%s%d",r,&p);
									int robot = (int)(*r == 'O');
									int tx = max(0,abs(position[robot]-p)-waiting[robot])+1;
									ret += tx;
									waiting[1-robot] += tx;
									position[robot] = p;
									waiting[robot] = 0;
					}
					printf("Case #%d: %d\n",tc,ret);
	}
	return 0;
}
