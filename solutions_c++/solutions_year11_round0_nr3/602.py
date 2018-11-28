#include <stdio.h>
#include <string.h>
#include <algorithm>

int n;
int s[1010];
int cnt[1010];

int main() {
	int t,c=0;
	
	scanf("%d",&t);
	while(t--) {
		memset(cnt,0,sizeof(cnt));
		scanf("%d",&n);
		for(int i=0;i<n;++i) {
			scanf("%d",&s[i]);
			int num = s[i];
			int p=0;
			while(num > 0) {
				cnt[p] += num%2;
				num /= 2;
				++p;
			}
		}
		
		bool fail = false;
		for(int i=0;i<30;++i)
			if(cnt[i]&1) {
				fail = true;
				break;
			}
		
		if(fail) {
			printf("Case #%d: NO\n",++c);
			continue;
		}
		
		//std::sort(s,s+n);
		
		int ans = 0;
		int ptr = -1;
		int ps;
		for(int i=0;i<n;++i) {
			int sum=0;
			for(int j=0;j<n;++j) 
				if(j != i)
					sum ^= s[j];
			//printf("%d %d\n",sum,s[i]);
			if(sum == s[i]) {
				if(ptr == -1) {
					ptr = i;
					ps=0;
					for(int j=0;j<n;++j)
						if(j != i)
							ps += s[j];
					if(ps > ans) {
						ptr = i;
						ans = ps;
					}
				} else {
					ps = 0;
					for(int j=0;j<n;++j)
						if(j != i)
							ps += s[j];
					if(ps > ans) {
						ptr = i;
						ans = ps;
					}
				}
			}
		}
		
		printf("Case #%d: %d\n",++c,ans);
	}
	
	return 0;
}
