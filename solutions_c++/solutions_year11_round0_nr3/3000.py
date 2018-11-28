#include <stdio.h>
#include <string.h>

#define MAXN 16
#define Max(a, b) ((a>b)?(a):(b))
bool f[MAXN];
int s0, s1, p0, p1;
int n, a[MAXN];
int ans;

void dfs(int key) {
	if (key==n) {
		s0=s1=p0=p1=0;
		for (int i=0; i<n; i++)
			if (f[i]) s0=s0^a[i], p0+=a[i];
			else s1=s1^a[i], p1+=a[i];
		if (s0==s1&&s0!=0&&s1!=0) {
			ans=Max(ans, Max(p1, p0));
		}
		return;
	}
	f[key]=false;
	dfs(key+1);
	f[key]=true;
	dfs(key+1);
	return;
}
int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int cas, k;
	scanf("%d", &cas);
	for (k=1; k<=cas; k++) {
		scanf("%d", &n);
		for (int i=0; i<n; i++) scanf("%d", &a[i]);
		ans=-1;
		dfs(0);
		if (ans==-1) printf("Case #%d: NO\n", k); 
		else printf("Case #%d: %d\n", k, ans); 
	}
	return 0;
}
