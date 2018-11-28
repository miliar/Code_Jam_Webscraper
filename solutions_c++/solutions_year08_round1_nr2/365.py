#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<string>
#include<cmath>
#include<vector>
#include<algorithm>
using namespace std;

const int maxn=1000;

int n,cas;
int m,t;
int p[maxn],mask[maxn];

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&cas);
	int lv,i,k,v,j,ans,cnt,tcnt;
	for(lv=1;lv<=cas;lv++) {
		scanf("%d%d",&n,&m);
		ans=0, cnt=n+10;
		for(i=0;i<m;i++) {
			scanf("%d",&t);
			p[i]=mask[i]=0;
			while(t--) {
				scanf("%d%d",&v,&j);
				p[i]|=(j<<(v-1));
				mask[i]|=(1<<(v-1));
			}
		}
		int top=(1<<n);
		for(i=0;i<top;i++) {
			for(j=0;j<m;j++) {
				if(((i&mask[j])^p[j])==0) break;
			}
			if(j>=m) { 
				tcnt=n;
				for(k=0;k<n;k++) {
					if(i&(1<<k)) tcnt--; 
				}
				if(tcnt<cnt) {
					cnt=tcnt;
					ans=i;
				}
			}
		}
		if(cnt<=n) {
			printf("Case #%d:",lv);
			fprintf(stderr,"Case #%d:",lv);
			i=ans;
			for(j=0;j<n;j++) {
				if(i&(1<<j)) {
					printf(" 0");
					fprintf(stderr," 0");
				} else {
					printf(" 1");
					fprintf(stderr," 1");
				}
			}
			printf("\n");
			fprintf(stderr,"\n");
		} else {
			fprintf(stderr,"Case #%d: IMPOSSIBLE\n",lv);			
			printf("Case #%d: IMPOSSIBLE\n",lv);			
		}
	}
	return 0;
}