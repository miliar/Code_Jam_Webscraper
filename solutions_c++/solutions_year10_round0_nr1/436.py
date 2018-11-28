#include<cstdio>
#include<algorithm>
#include<cstring>
#include<vector>
using namespace std;
typedef __int64 ll;
const int maxn=5010;

ll dp[100];
int n,m;
int main()
{
	freopen("A-large.in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k,ca,cc=1;
	scanf("%d",&ca);
	while(ca--) 
	{
		scanf("%d%d",&n,&m);
		dp[1]=1;
		for(i=2;i<=n;i++) 
		{
			dp[i]=dp[i-1]*2+1;
		}
		printf("Case #%d: ",cc++);
		if(m>=dp[n]&&(m-dp[n])%(dp[n]+1)==0) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}