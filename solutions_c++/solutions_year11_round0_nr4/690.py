#include <cstdio>
#include <vector>
using namespace std;

const int MAXN=1000;

void run(int casenr) {
	int n; scanf("%d",&n);
	vector<int> start(n); for(int i=0;i<n;++i) { scanf("%d",&start[i]); --start[i]; }
	double ret=0;
	for(int i=0;i<n;++i) if(start[i]!=i) ++ret;
	printf("Case #%d: %.6lf\n",casenr,ret);
}

int main() {
	int n; scanf("%d",&n); for(int i=1;i<=n;++i) run(i);
	return 0;
}
