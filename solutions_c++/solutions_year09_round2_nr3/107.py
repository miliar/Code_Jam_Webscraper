#include <iostream>
#include <string>
#include <queue>
#include <cctype>
#include <map>
#include <set>
using namespace std;
#define REP(i,n) for (int i=0; i<(n); ++i)
int t, w, q, target;
char g[32][32];
map<int,string> best[32][32];
set<int> vis;
string go() {
	REP(i,w) REP(j,w) best[i][j].clear();
	vis.clear();
	for (int i=0; i<w; ++i) for (int j=0; j<w; ++j) if (isdigit(g[i][j])) {
		vis.insert(g[i][j]-'0');
		best[i][j][g[i][j]-'0']="";
		best[i][j][g[i][j]-'0']+=g[i][j];
//		cerr << i <<  " " << j << g[i][j]-'0' << best[i][j][g[i][j]-'0'] << endl;
	}
	int l=1;
	int dx[4]={-1,0,1,0}, dy[4]={0,-1,0,1};
	while (vis.find(target)==vis.end()) {
		REP(i,w) REP(j,w) for(map<int,string>::iterator it=best[i][j].begin(); it!=best[i][j].end(); ++it) if ((it->second).length()==l) {
			int num=it->first;
			string cur=it->second;
//			cerr << i << " " << j << " " << num << " " << cur << endl;
			REP(dir,4) {
				int nx=i+dx[dir], ny=j+dy[dir];
				if (nx<0||ny<0||nx>=w||ny>=w) continue;
				string s=cur+g[nx][ny];
				if (g[nx][ny]=='+'||g[nx][ny]=='-') {
					if (best[nx][ny].find(num)==best[nx][ny].end()||(best[nx][ny][num].length()==l+1&&best[nx][ny][num]>s)) {
						best[nx][ny][num]=s;
					}
				} else {
					int val=num;
					if (g[i][j]=='+') val=val+g[nx][ny]-'0';
					else val=val-(g[nx][ny]-'0');
					if (best[nx][ny].find(val)==best[nx][ny].end()||(best[nx][ny][val].length()==l+1&&best[nx][ny][val]>s)) {
						best[nx][ny][val]=s;
					}
					vis.insert(val);
				}
			}
		}
			++l;
	}
	string ans;
	REP(i,w) REP(j,w) if (best[i][j].find(target)!=best[i][j].end()) {
		if (ans==""||ans>best[i][j][target]) ans=best[i][j][target];
	}
	return ans;
}
int main()
{
	freopen("C-small-attempt0 (1).in","r",stdin);
	freopen("C.out","w",stdout);
	cin >> t;
	for (int tc=1; tc<=t; ++tc) {
		scanf("%d%d", &w, &q);
		REP(i,w) scanf("%s", g[i]);
		printf("Case #%d:\n", tc);
		while (q--) {
			scanf("%d", &target);
			printf("%s\n", go().c_str());
		}
	}
}
