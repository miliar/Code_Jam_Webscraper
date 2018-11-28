#include<iostream>
#include<vector>
using namespace std;
const int MXN=2010;
const int MXM=2010;
int n,m,v[MXN];
bool change;
vector<int> g[MXM],w[MXM];
bool check(int i)
{
	int j;
	for (j=0;j<g[i].size();++j) {
		if (w[i][j]==v[g[i][j]]) return true;
	}
	for (j=0;j<g[i].size();++j)
		if (w[i][j]) {
			v[g[i][j]]=1;
			change=true;
			return true;
		}
	return false;
}
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int t,T;
	scanf("%d",&t);
	for (T=1;T<=t;++T) {
		int i,j;
		scanf("%d%d",&n,&m);
		for (i=0;i<m;++i) {
			int q;
			scanf("%d",&q);
			g[i].clear();w[i].clear();
			for (j=0;j<q;++j) {
				int a,b;
				scanf("%d%d",&a,&b);
				g[i].push_back(a);
				w[i].push_back(b);
			}
		}
		memset(v,0,sizeof(v));
		bool find=true;
		do {
			change=false;
			for (i=0;i<m;++i)
				if (!check(i)) {
					find=false;
					break;
				}
			if (!find) break;
		} while (change);
		printf("Case #%d: ",T);
		if (find) {
			for (j=1;j<n;++j) printf("%d ",v[j]);
			printf("%d\n",v[n]);
		} else printf("IMPOSSIBLE\n");
	}
}
