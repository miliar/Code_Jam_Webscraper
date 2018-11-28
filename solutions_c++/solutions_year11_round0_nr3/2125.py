#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int t, n, num;
int ar[2000];
int a[2000], b[2000];
int sa[2000], sb[2000];
bool ok;

int main () {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tc = 0;
	int ans = 0;
    scanf("%d", &t);
	while(t--){
		ans = 0;
		ok = false;
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		memset(sa, 0, sizeof(sa));
		memset(sb, 0, sizeof(sb));
		
		scanf("%d", &n);
		for(int i = 0; i < n;i++){
			scanf("%d", &ar[i]);
		}
		sort(ar, ar+n);
		
		a[0] = ar[0];
		sa[0] = ar[0];
		for (int i = 1; i < n; i++) {
			a[i] = a[i-1] ^ ar[i];
			sa[i] = sa[i-1] + ar[i];
		}
		
		b[n-1] = ar[n-1];
		sb[n-1] = ar[n-1];
		for (int i = n - 2; i > 0; i--) {
			b[i] = b[i+1] ^ ar[i];
			sb[i] = sb[i+1] + ar[i];
		}
		
		for(int i = 0; i < n-1; i++){
			if(a[i] == b[i+1]){
				ok = true;
				ans = max(sa[i],sb[i+1]);
				break;
			}
		}
		
		if(ok){
			printf("Case #%d: %d\n", ++tc, ans);
		}
		else{
			printf("Case #%d: NO\n", ++tc);
		}
	}
    return 0;
}
