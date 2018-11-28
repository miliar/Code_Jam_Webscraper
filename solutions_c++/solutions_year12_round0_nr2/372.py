#include <cstdio>
#include <algorithm>
using std::sort;
int n,s,p,t[110];
int normal(int n) {
	if(n%3 == 0) return n/3;
	return n/3+1;
}
int surp(int n) {
	if(n == 0) return 0;
	if(n%3 == 2) return n/3+2;
	return n/3+1;
}
void work() {
	int ans = 0;
	scanf("%d %d %d",&n,&s,&p);
	for(int i = 0;i < n;i ++)
		scanf("%d",&t[i]);
	for(int i = 0;i < n;i ++) {
		int a = normal(t[i]);
		int b = surp(t[i]);
		if(a > 10) a = 0;
		if(b > 10) b = 0;
		if(a >= p) ans++;
		else if(b >=p && s) {
			ans ++;
			s --;
		}
	}
	printf("%d\n",ans);
}
int main() {
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i = 1;i <= T;i ++) {
		printf("Case #%d: ",i);
		work();
	}
}
