#include <stdio.h>
#include <algorithm>
using namespace std;

typedef long long LL;
LL gcd(LL x, LL y){
	if(y==0) return x;
	return gcd(y, x%y);
}

long long dp[1000000];
int s[1000000];
LL r[105];

bool cmp(int x,int y){
	return dp[x]!=-1 && dp[y]==-1 || dp[x] < dp[y];
}

int main(void)
{
	int n;
	int T, cs;
	scanf("%d",&T);
	int i, j, k;
	LL L;
	for(cs=1;cs<=T;cs++){
		scanf("%I64d%d",&L,&n);
		long long g=0;
		for(i=0;i<n;i++){
			scanf("%I64d",&r[i]);
			g = gcd(r[i], g);
		}
		if(L%g!=0){
			fprintf(stderr, "Case #%d: IMPOSSIBLE\n", cs);
			printf("Case #%d: IMPOSSIBLE\n", cs);
			continue;
		}
		L/=g;
		for(i=0;i<n;i++)
			r[i]/=g;
		
		sort(r, r+n);
		memset(dp, -1, sizeof(dp));
		dp[0] = 0;
		for(i=0;i<r[n-1];i++)
			s[i]=i;
		for(i=0;i<n-1;i++){
			sort(s, s+r[n-1], cmp);
			/*for(j=0;j<r[n-1];j++)
				fprintf(stderr,"%d ",s[j]);
			fprintf(stderr,"\n");*/
			for(k=0;k<r[n-1];k++){
				j = s[k];
				if(dp[j]!=-1)
				while(1){
					if(dp[ ((j+r[i]>=r[n-1])? (j+r[i]-r[n-1]): (j+r[i])) ]== -1 ||
  					   dp[ ((j+r[i]>=r[n-1])? (j+r[i]-r[n-1]): (j+r[i])) ] >
						  dp[j] + ((j+r[i]<r[n-1])?1LL:0LL)){

						dp[ ((j+r[i]>=r[n-1])? (j+r[i]-r[n-1]): (j+r[i])) ] = dp[j] +((j+r[i]<r[n-1])?1LL:0LL);
						j = ((j+r[i]>=r[n-1])? (j+r[i]-r[n-1]): (j+r[i]));
					}
					else
						break;
				}

			}
			
			/*for(j=0;j<r[n-1];j++)
				printf("%I64d ",dp[j]);
			printf("\n");*/
		}
		printf("Case #%d: %I64d\n", cs, dp[L%r[n-1]] + L/r[n-1]);
		fprintf(stderr,"Case #%d: %I64d\n", cs, dp[L%r[n-1]] + L/r[n-1]);
	}
	return 0;
}
