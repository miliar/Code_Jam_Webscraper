#include <stdio.h>
#include <string.h>

int used[300],n;
char s[70];
long long ans,base,count;

int main() {
	int t,i,j,c=0;
	
	scanf("%d",&t);
	while(t--) {
		for(i=0;i<300;i++)
			used[i] = -1;
		base = 0;
		scanf("%s",s);
		n = strlen(s);
		
		printf("Case #%d: ",++c);
		if(n == 1) {
			puts("1");
			continue;
		}
		used[s[0]] = 1;
		for(i=1;i<n && s[i] == s[0];i++);
		used[s[i]] = 0;
		base = 2;
		for(;i<n;i++) {
			if(used[s[i]] == -1) {
				used[s[i]] = base;
				base++;
			}
		}
		
		ans = 0;
		for(i=n-1,count=1;i>=0;i--,count*=base) {
			ans += count*used[s[i]];
		}
		
		printf("%lld\n",ans);
	}
	
	return 0;
}
