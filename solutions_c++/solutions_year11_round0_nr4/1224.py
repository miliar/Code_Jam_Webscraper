#include <stdio.h>
#include <string.h>

#define MAX 1100

int p[MAX];
bool was[MAX];

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;++test) {
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;++i) {
			scanf("%d",&p[i]);
			--p[i];
		}
		int ans=0;
		memset(was,0,sizeof(was));
		for(int i=0;i<n;++i)
			if(!was[i]) {
				int k=0;
				int j=i;
				do {
					++k;
					was[j]=true;
					j=p[j];
				}
				while(!was[j]);
				if(k>1) ans+=k;
			}
		printf("Case #%d: %d\n",test,ans);
	}
	return 0;
}
