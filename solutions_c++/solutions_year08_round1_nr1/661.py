#include<cstdio>
#include<vector>
#include<algorithm>

using namespace std;

vector<__int64> x(0);
vector<__int64> y(0);
int main() {
	freopen("A-small.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
	int t;
	scanf("%d",&t);
	for(int j=0;j<t;++j) {
		x.clear();
		y.clear();
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;++i) {
			__int64 x1;
			scanf("%I64d",&x1);
			x.push_back(x1);
		}
		
		for(int i=0;i<n;++i) {
			__int64 y1;
			scanf("%I64d",&y1);
			y.push_back(y1);
		}
		
		sort(x.begin(),x.end());
		sort(y.begin(),y.end());
		
		int res=0;
		for(int i=0;i<n;++i)
			res+=x[i]*y[n-i-1];
		
		printf("Case #%d: %d\n",(j+1),res);
	}
}