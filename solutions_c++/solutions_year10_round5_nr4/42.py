#include <stdio.h>
#include <string.h>

#define P 1000000007

#define MAX 110

int x[MAX];

int n,b,ans;

bool intersect(int x,int y) {
	while(x>0 && y>0) {
		if((x%b) == (y%b))
			return true;
		x/=b, y/=b;
	}
	return false;
}

void go(int s,int k,int m) {
	if(s==n) {
		++ans;
		return;
	}
	for(int c=m;c<=n-s;++c) {
		bool ok=true;
		for(int i=0;i<k;++i) {
			if(intersect(x[i],c)) {
				ok=false;
				break;
			}
		}
		if(ok) {
			x[k]=c;
			go(s+c,k+1,c+1);
		}
	}
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;++test) {
		scanf("%d%d",&n,&b);
		ans=0;
		go(0,0,1);
		printf("Case #%d: %d\n",test,ans);
	}
	return 0;
}
