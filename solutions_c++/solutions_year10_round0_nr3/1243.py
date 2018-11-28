#include <stdio.h>
#include <string.h>

#define MAX 1024

int g[MAX];
int sum[MAX];
int next[MAX];

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;++test) {
		int r,k,n;
		scanf("%d%d%d",&r,&k,&n);
		for(int i=0;i<n;++i)
			scanf("%d",&g[i]);
		for(int j=0;j<n;++j) {
			int c=0;
			int head=j;
			for(int i=0;i<n;++i) {
				c+=g[head];
				if(c<=k) {
					++head;
					if(head>=n) head=0;
				}
				else {
					c-=g[head];
					break;
				}
			}
			sum[j]=c;
			next[j]=head;
		}
		int head=0;
		long long res=0;
		for(int h=0;h<r;++h) {
			res+=sum[head];
			head=next[head];
		}
		printf("Case #%d: %lld\n",test,res);
	}
	return 0;
}
