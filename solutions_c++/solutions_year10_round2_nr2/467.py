#include <cstdio>
#define h 100

int T,n,k,b,t,i,j,p,c,x[h],v[h],ans;
bool fix[h];

int main() {
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &T);
	for(c=1;c<=T;c++) {
		scanf("%d%d%d%d", &n, &k, &b, &t);
		for(i=0;i<n;i++)
			fix[i] = false;
		for(i=0;i<n;i++)
			scanf("%d", &x[i]);
		for(i=0;i<n;i++)
			scanf("%d", &v[i]);
		for(i=0;i<n;i++)
			if(b - x[i] > v[i] * t)
				fix[i] = false;
			else
				fix[i] = true;
		ans = 0;
		for(i=n-1,j=0;i>=0 && j<k;i--)
			if(fix[i]) {
				j++;
				for(p=i;p<n;p++)
					if(!fix[p])
						ans++;
			}
		if(j == k)
			printf("Case #%d: %d\n", c, ans);
		else
			printf("Case #%d: IMPOSSIBLE\n", c);
	}
	return 0;
}