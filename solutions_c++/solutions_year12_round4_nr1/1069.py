
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

typedef long long i8;

int vc, tgt;
vector< pair<int,int> > ver;
int cli[10111];
char ye[]="YES", no[]="NO";

char* solve() {
	
	scanf("%d", &vc);
	ver.clear();
	fill(cli,cli+vc,0);
	
	for (int v=0; v<vc; v++) {
		int a,b;
		scanf("%d%d", &a, &b);
		ver.push_back(make_pair(a,b));
	}
	cli[0]=ver[0].first;
	sort(ver.begin(),ver.end());
	scanf("%d",&tgt);
	
	bool get=false;
	for (int v=0; v<vc && !get; v++) if (cli[v]) {
		int c=cli[v], p=ver[v].first;
		for (int o=0; o<vc; o++) {
			int op=ver[o].first, os=ver[o].second;
			//printf("      chk o=%d op=%d os=%d\n", o, op, os);
			if (op>p && p+c>=op) {
				cli[o]=max(cli[o],min(os,op-p));
			}
		}
		//printf("   cli[%d]=%d\n", v, cli[v]);
		if (p+cli[v]>=tgt) get=true;
	}
	return get?ye:no;
}

main() {
	int tt;
	scanf("%d", &tt);
	for (int tc=1; tc<=tt; tc++) {
		printf("Case #%d: %s\n", tc, solve());
	}
}
