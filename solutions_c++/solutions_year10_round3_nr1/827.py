#include <stdio.h>
#include <string.h>
#include <algorithm>

int n;
struct node {
	int A,B;
	
	bool operator < (const node &t) const {
		return A < t.A;
	}
	
	void get() {
		scanf("%d%d",&A,&B);
	}
} s[1010];

int main() {
	int t,c=0;
	
	scanf("%d",&t);
	while(t--) {
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			s[i].get();
		std::sort(s,s+n);
		int ans = 0;
		for(int i=0;i<n;i++)
			for(int j=i+1;j<n;j++)
				if(s[i].B > s[j].B)
					ans++;
		printf("Case #%d: %d\n",++c,ans);
	}
	
	return 0;
}
