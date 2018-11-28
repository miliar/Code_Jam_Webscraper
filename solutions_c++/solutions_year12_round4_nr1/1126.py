#include<stdio.h>
#include<string.h>
#include<string>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<math.h>
#include<set>
using namespace std;

int d[10010],L[10010];
int dp[10010];
int main() {
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int T,n,D,ri=1;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%d%d",&d[i],&L[i]);
		scanf("%d",&D);
		L[n]=1<<30;
		d[n]=D;
		//int len=L[0],now=d[0];
		//int flag=1;
		memset(dp,-1,sizeof(dp));
		dp[0]=d[0];
		for(int i=1;i<=n;i++){
			for(int j=0;j<i;j++){
				if(dp[j]>0&&dp[j]+d[j]>=d[i]){
					dp[i]=max(dp[i],d[i]-d[j]);
					dp[i]=min(dp[i],L[i]);
				}
			}
		}
		/*for(int i=1;i<n+1;){
			int left=i+1,right=n+1,mid,ans=-1;
			while(left<=right){
				mid=(left+right)/2;
				if(d[mid]<=len+now){
					ans=mid;
					left=mid+1;
				}
				else
					right=mid-1;
			}
			if(ans==-1){
				flag=0;
				break;
			}
			else{
				len=min(d[ans]-now,L[ans]);
				i=ans;
				now=d[ans];
				//printf("%d %d %d\n",now,i,len);

			}
		}*/
		if(dp[n]!=-1)
			printf("Case #%d: YES\n",ri++);
		else
			printf("Case #%d: NO\n",ri++);
	}

}
