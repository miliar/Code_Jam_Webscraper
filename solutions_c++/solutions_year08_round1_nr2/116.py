#include<set>
#include<map>
#include<cmath>
#include<cstdio>
#include<vector>
#include<string>
#include<iostream>
#include<sstream>
#include<algorithm>
using namespace std;
#define FOR(i,a,b) for(int i=(a); i<(b); ++i)
#define FORE(i,a) for(typeof(a.begin()) i = a.begin(); i!= a.end(); ++i)
#define SET(x,v) memset(x,v,sizeof(x))
#define cs c_str()
#define sz size()
#define mp make_pair
#define pb push_back

typedef long long i64;

set<int> dat[2048];
int ans[2048];
bool isset[2048], checked[2048];
int main() {
    freopen("B.in","r",stdin);
    FILE *fp=fopen("B.out","w");
    int e = 0, T;
    int n, m, t;
    scanf("%d",&T);
    while (T--) {
		scanf("%d%d",&n,&m);
		FOR(i,0,m) {
			dat[i].clear();
			scanf("%d",&t);
			FOR(j,0,t) {
				int x, y;
				scanf("%d%d",&x,&y);
				if (y==0) {
					dat[i].insert(x);
				}
				else {
					dat[i].insert(-x);
				}
			}
		}
		bool impossible = false;
		bool cond = true;
		SET(ans, 0);
		SET(isset, 0);
		SET(checked, 0);
		while(cond) {
			cond = false;
			FOR(i,0,m) {
				if (dat[i].sz == 0) {
					impossible = true;
					break;
				} else if (dat[i].sz == 1 && !checked[i]) {
					checked[i] = true;
					int flavor = *(dat[i].begin());
					//printf("flavor %d is set by %d\n",flavor, i);
					if (flavor < 0) {
						if (isset[-flavor] && ans[-flavor] != 1) {
							impossible = true;
							break;
						}
						isset[-flavor] = true;
						ans[-flavor] = 1;
					} else {
						if (isset[flavor] && ans[flavor] != 0) {
							impossible = true;
							break;
						}
						isset[flavor] = true;
						ans[flavor] = 0;
					}
					FOR(j,0,m) {
						if (dat[j].find(-flavor) != dat[j].end()) {
							dat[j].erase(dat[j].find(-flavor));
						}
					}
					cond = true;
					break;
				}
			}
			if(impossible)break;

		}
		if(impossible) {
			printf("Case #%d: IMPOSSIBLE\n",++e);
		}
		else {
			printf("Case #%d:",++e);
			FOR(i,1,n+1)
				printf(" %d",ans[i]);
			printf("\n");
		}
    }
    fclose(fp);
    return 0;
}

