#include <cstdio>
#include <set>
#include <map>
using namespace std;

int M[1100];
int pr[11][1100];
bool m[11][1100];

int main() {
	int T,P;
	scanf("%d",&T);
	for(int t=0;t<T;++t) {
		memset(m, false, sizeof(m));
		scanf("%d",&P);
		set<pair<int,int> > q;
		for(int p=0;p<(1<<P);++p) {
			scanf("%d",M+p);
			q.insert(make_pair(M[p],p));
		}
		for(int p=0;p<P;++p){
			for(int i=0;i<(1<<(P-1-p));++i)
				scanf("%d",&pr[p][i]);
		}
		int count = 0;
		while(!q.empty()) {
			int team = q.begin()->second;
			q.erase(q.begin());
			int tm = team/2;
			for(int p=0;p<P-M[team];++p) {
				if(!m[P-p-1][tm>>(P-p-1)]) {
					m[P-p-1][tm>>(P-p-1)]=true;
					//printf("%d %d %d %d\n",pr[P-p-1][tm>>(P-p-1)],P-p-1,tm>>(P-p-1),team);
					count+=pr[P-p-1][tm>>(P-p-1)];
				}
			}
		}
		printf("Case #%d: %d\n",t+1, count);
	}
}