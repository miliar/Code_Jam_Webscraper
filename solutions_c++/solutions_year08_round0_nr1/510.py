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

map<string, int> dic;
int dat[1024];
int dyn[1024][128];

string have_it_clear(string x) {
	while (x.sz > 0 && (x[x.sz-1]==10 || x[x.sz-1]==13))
		x[x.sz - 1] = 0;
	return x;
}
int main() {
	freopen("A-small.in","r",stdin);
	FILE *fo=fopen("output.txt","w");
	int T, S, Q, e = 0, ans;
	scanf("%d",&T);
	while (T--) {
		dic.clear();
		scanf("%d ",&S);
		FOR(i,0,S) {
			char buff[1024];
			gets(buff);
			string tmp = have_it_clear(buff);
			//printf("S [%s]\n",tmp.cs);
			dic[tmp] = i+1;
		}
		scanf("%d ",&Q);
		FOR(i,0,Q) {
			char buff[1024];
			gets(buff);
			string tmp = have_it_clear(buff);
			int k = dic[tmp];
			//printf("Q%3d[%s] %d/%d\n",i,tmp.cs,k,dic.sz);
			if (k<1 || k>S) {
				printf("\n\ncrap ([%s] not found)\n\n", tmp.cs);
				return 0;
			}
			dat[i] = k;
		}
		ans = 0;
		FOR(q,0,Q) {
			FOR(s,1,S+1) {
				dyn[q][s] = 1048576;
			}
		}
		FOR(s,1,S+1) {
			dyn[0][s] = dat[0]==s ? 1048576 : 0;
		}
		FOR(q,1,Q) {
			FOR(s,1,S+1) {
				FOR(t,1,S+1) {
					int x = dat[q];
					if (s==t) {
						// don't switch
						dyn[q][s] = min(dyn[q][s], s == x ? 1048576 : dyn[q-1][s]);
					} else {
						// switch
						dyn[q][s] = min(dyn[q][s], s == x ? 1048576 : dyn[q-1][t]+1);
					}
				}
			}
		}
		if (Q== 0) ans = 0;
		else{
			ans = 1048576;
			FOR(s,1,S+1)
				ans=min(dyn[Q-1][s],ans);
		}
		fprintf(fo,"Case #%d: %d\n",++e, ans);
	}
	fclose(fo);
	return 0;
}