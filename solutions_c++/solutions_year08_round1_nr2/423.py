#include<cstdio>
#include<vector>

using namespace std;

vector<pair<int,int> > l[500];
int main() {
	freopen("B-small.in","rt",stdin);
	freopen("B-small.out","wt",stdout);
	int c;
	scanf("%d",&c);
	for(int i=0;i<c;++i) {
		for(int j=0;j<500;++j)
			l[j].clear();
		int n,m;
		scanf("%d%d",&n,&m);
		for(int j=0;j<m;++j) {
			int t;
			scanf("%d",&t);
			for(int k=0;k<t;++k) {
				int t1,t2;
				scanf("%d%d",&t1,&t2);
				l[j].push_back(make_pair(t1-1,t2));
			}
		}
		
		int mres=10000;
		int v=0;
		for(int j=0;j<(1<<n);++j) {
			bool t=true;
			for(int k=0;k<m;++k) {
				bool b=false;
				for(int cc=0;cc<l[k].size();++cc) {
					//printf("%d %d %d %d\n",j,k,cc,(j>>l[k][cc].first)&1-l[k][cc].second);
					if (!(((j>>l[k][cc].first)&1)^l[k][cc].second)) {
						b=true;
						break;
					}
				}
				if (!b) {
					t=false;
					break;
				}
			}
			if (t) {
					int res=0;
					for(int k=0;k<n;++k)
						if ((j>>k)&1) res++;
					if (res<mres) {mres=res;v=j;}
			}
		}
		if (mres==10000) printf("Case #%d: IMPOSSIBLE\n",(i+1));
		else {
			printf("Case #%d:",(i+1));
			for(int j=0;j<n;++j)
				printf(" %d",(v>>j)&1);
			printf("\n");
		}
	}
}