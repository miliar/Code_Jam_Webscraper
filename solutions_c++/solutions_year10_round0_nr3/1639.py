#include <iostream>
#include <cstring>
#include <cstdio>
#include <queue>
#include <algorithm>
using namespace std;


void open(){
	freopen("clarge.in","r",stdin);
	freopen("clarge.out","w",stdout);
};
typedef long long ll;
int t,x,r,k,n,g[1001],next[1001],idx;
ll ans,sum[1001];

int main(){
	open();
	scanf("%d",&t);
	x=1;
	while (t--){
		ans=0;
		scanf("%d%d%d",&r,&k,&n);
		queue<int>q,q2;
		for (int i=0;i<n;i++){
			scanf("%d",&g[i]);
		}
		memset(sum,0,sizeof(sum));
		memset(next,0,sizeof(next));
		for (int i=0;i<n;i++){
			int j=i;
			ll tot=g[i];
			while (1){
				if (tot+g[(j+1)%n]<=(ll)k && (j+1)%n!=i){
					tot+=g[(j+1)%n];
					j++;
					if (j>=n){
						j%=n;
					}
				}
				else break;
			}
			sum[i]=tot;
			next[i]=(j+1)%n;
		}
		idx=0;
		for (int i=0;i<r;i++){
			ans+=sum[idx];
			idx=next[idx];
		}
		printf("Case #%d: ",x++);
		cout<<ans<<endl;
	}
	return 0;
}
