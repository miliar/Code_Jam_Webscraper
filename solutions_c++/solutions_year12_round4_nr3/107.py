#include <cstdio>
#include <cstring>
using namespace std;

int delta[110][15];
int ans[2010],h[2010];
int T,n;

int main(){
	scanf("%d",&T);
	for (int cases=0;cases<T;++cases){
		scanf("%d",&n);
		for (int i=1;i<n;++i) scanf("%d",&h[i]);
		bool t=false;
		for (int i=1;i<n;++i){
			if (h[i]<=i){
				printf("Case #%d: Impossible\n",cases+1);
				t=true;
			}
		}
		if (t) continue;
		int cur=0;
		memset(delta,0,sizeof(delta));
		for (int i=1;i<n;++i){
			for (int k=i+1;k<=n;++k){
				if (k==h[i]) continue;
				int j=h[i];
				delta[cur][j]=k-i;
				delta[cur][i]=j-k;
				delta[cur][k]=i-j;
				cur++;
			}
		}
		//for (int i=0;i<cur;++i){
		//	for (int j=1;j<=n;++j) printf("%d ",delta[i][j]);
		//	printf("\n");
		//}
		memset(ans,0,sizeof(ans));
		int cnt=0;
		while (true){
			bool t=true;
			for (int i=0;i<cur;++i){
				int tmp=0;
				for (int j=1;j<=n;++j) tmp+=ans[j]*delta[i][j];
				if (tmp<=0){
					t=false;
					for (int j=1;j<=n;++j) ans[j]+=delta[i][j];
				}
			}
			if (t) break;
			if (++cnt>10000) break;
		}
		printf("Case #%d:",cases+1);
		if (cnt>10000){
			printf(" Impossible\n");
			continue;
		}
		int min=0;
		for (int i=1;i<=n;++i) if (ans[i]<min) min=ans[i];
		for (int i=1;i<=n;++i) printf(" %d",ans[i]-min);
		printf("\n");
	}
	return 0;
}
