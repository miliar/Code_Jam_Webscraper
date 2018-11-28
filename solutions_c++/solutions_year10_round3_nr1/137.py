#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

pair<int,int>p[1010];
int n;

#define size 10010
class TreeArray{
public:
	int c[size];
	void init(){memset(c,0,sizeof(c));}
	int getsum(int end)	{
		int sum = 0;
		while(end > 0)
		{
			sum += c[end];
			end -= end & (-end);
		}
		return sum;
	}
	void update(int end,int i,int n){
		while(end <= n){
			c[end] += i;
			end += end & (-end);
		}
	}
};

TreeArray tree;
int solve() {
	int ans = 0;
	sort(p,p + n);
	tree.init();
	for(int i = 0;i < n;++i) {
		ans += tree.getsum(10001) - tree.getsum(p[i].second);
		tree.update(p[i].second,1,10001);
	}
	return ans;
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,cas(1);
	scanf("%d",&T);
	while(T--) {
		scanf("%d",&n);
		int a,b;
		for(int i = 0;i < n;++i) {
			scanf("%d%d",&a,&b);
			p[i] = pair<int,int>(a,b);
		}
		printf("Case #%d: %d\n",cas++,solve());
	}	
	return 0;
}
