#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int cnt[100];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int TT;scanf("%d",&TT);
	for(int cas=1;cas<=TT;++cas){
		int N;
		scanf("%d",&N);
		for(int i=1;i<=N;++i){
			cnt[i]=0;
			for(int j=1;j<=N;++j){
				int k;scanf("%1d",&k);
				if(k==1) cnt[i]=j;
			}
		}
		int ans=0;
		for(int i=1;i<=N;++i){
			if(cnt[i]<=i) continue;
			for(int j=i+1;j<=N;++j){
				if(cnt[j]<=i){
					for(int k=j;k>i;--k) swap(cnt[k],cnt[k-1]),++ans;
					break;
				}
			}
		}
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}
