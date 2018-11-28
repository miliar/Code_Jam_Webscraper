#include <stdio.h>
#include <string.h>

#define MAX 1001000

double a[MAX];

double ans[2][MAX];

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;++test) {
		int l,n,c;
		double t;
		scanf("%d%lf%d%d",&l,&t,&n,&c);
		for(int i=0;i<c;++i)
			scanf("%lf",&a[i]);
		memset(ans,0,sizeof(ans));
		int prev=0,next;
		for(int i=0;i<n;++i) {
			next=prev^1;
			double dist=a[i%c];
			for(int j=0;j<=l;++j) {
				ans[next][j]=ans[prev][j]+dist*2;
				if(j>0) {
					double r=t-ans[prev][j-1];
					if(r<=0) {
						double cur=ans[prev][j-1]+dist;
						if(cur<ans[next][j])
							ans[next][j]=cur;
					}
					else if(r>=2*dist) {
						double cur=ans[prev][j-1]+2*dist;
						if(cur<ans[next][j])
							ans[next][j]=cur;
					}
					else {
						double cur=ans[prev][j-1]+dist+r/2.0;
						if(cur<ans[next][j])
							ans[next][j]=cur;
					}
				}
			}
			prev=next;
		}
		long long anz=(long long)(ans[prev][l]+0.5);
		printf("Case #%d: %lld\n",test,anz);
	}
	return 0;
}
