#include<cstdio>
#include<vector>

using namespace std;

vector<int> u(0);
vector<int> num(0);

int main() {
	freopen("C-small.in","rt",stdin);
	freopen("C-small.out","wt",stdout);
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;++i) {
		u.clear();
		num.clear();
		int K,n;
		scanf("%d%d",&K,&n);
		for(int j=0;j<K;++j) u.push_back(j);
		num.push_back(0);
		num.resize(K+1,0);
		int tp=-1;
		for(int j=1;j<=K;++j) {
			/*int tj=j;
			while (tj>0) {
				tp++;
				if (tp>=u.size()) tp=0;
				if (!u[tp]) tj--;
			}*/
			//u[tp]=true;
			tp=(tp+j)%u.size();
			num[u[tp]]=j;
			u.erase(u.begin()+tp);
			tp--;
		}
		
		printf("Case #%d:",(i+1));
		for(int j=0;j<n;++j) {
			int t;
			scanf("%d",&t);
			printf(" %d",num[t-1]);
		}
		printf("\n");
	}
	return 0;
}