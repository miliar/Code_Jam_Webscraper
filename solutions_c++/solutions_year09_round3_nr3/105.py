#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <functional>

using namespace std;

int dp[120][120];
int z[121];
int a[121];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int zz;
	scanf("%d",&zz);
	for(int k=1;k<=zz;k++){
		int p,q,ans=1<<30,t;
		scanf("%d%d",&p,&q);
		int i,j;
		for(i=1;i<=q;i++)
			scanf("%d",&z[i]);
		sort(z+1,z+q+1);
		z[0]=0;
		z[q+1]=p+1;
		for(int f=2;f<=q+1;f++){
			for(i=0;i<=q+1-f;i++){
				t=1<<30;
				for(j=i+1;j<i+f;j++){
					t=min(t,z[j]-z[i]-1+z[i+f]-z[j]-1+dp[i][j]+dp[j][i+f]);
				}
				dp[i][i+f]=t;
			}
		}
		printf("Case #%d: %d\n",k,dp[0][q+1]);
	}

	return 0;
}
