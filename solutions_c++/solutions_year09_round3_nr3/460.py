#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
vector<int> pr;
bool vis[102];
int main() {
	int t, P,Q,i,a;
	scanf("%d",&t);
	for(int x=1;x<=t;++x) {
		scanf("%d%d", &P,&Q);
		pr.clear();
		for(i=0;i<Q;++i) scanf("%d",&a), pr.push_back(a);
		sort(pr.begin(),pr.end());
		int res = 100000000;
		vis[0]=1, vis[P+1]=1;
		do {
			for(i=1;i<=P;++i)vis[i]=0;
			int tmp = 0;
			for(int v=0;v<pr.size();++v) {
				vis[pr[v]] = 1;
				i = pr[v]-1; while(!vis[i]) ++tmp, --i;
				i = pr[v]+1; while(!vis[i]) ++tmp, ++i;
			}
			if(tmp < res) res = tmp;
		} while(next_permutation(pr.begin(),pr.end()));
		printf("Case #%d: %d\n", x,res);
	}
	return 0;
}