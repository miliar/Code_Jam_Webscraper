#include<cstdio>
#include<vector>
#include<cstring>

using namespace std;


int main() {
	int t,n,m,c,F[2005],a,b;
	vector<vector<pair<int,int> > > G(2005);
	scanf("%d\n",&t);
	for(int ii=1;ii<=t;++ii) {
		scanf("%d\n%d\n",&n,&m);
		G.clear();
		G.resize(m);
		for(int i=0;i<m;++i) {
			scanf("%d ",&c);
			for(int j=0;j<c;++j) {scanf("%d %d",&a,&b);G[i].push_back(pair<int,int>(a-1,b));}
		}
		memset(F,0,sizeof(F));
		int mm = 0;
		while(1) {
			bool ff = true;
			for(int i=0;i<m;++i) {
				bool found = false;
				for(int j=0;j < G[i].size();++j) if(F[G[i][j].first] == G[i][j].second) {found = true;break;}
				if(!found) {
					found = false;
					ff = false;
					for(int j=0;j < G[i].size();++j) if(F[G[i][j].first] == 0) {
						F[G[i][j].first] = 1;
						found = true;
						break;
					}
					if(!found) {
						mm = n + 1;
						goto L;
					}
				}
			}
			if(ff) break;
		}
L:
		if(mm == n + 1) {
			printf("Case #%d: IMPOSSIBLE\n",ii);
//			for(int i=0;i<n-1;++i) printf("%d ",F[i]);
//			printf("%d\n",F[n-1]);
		}
		else {
			printf("Case #%d: ",ii);
			for(int i=0;i<n-1;++i) printf("%d ",F[i]);
			printf("%d\n",F[n-1]);
		}
	}
	return 0;
}
