#include<stdio.h>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<memory>
#include<math.h>
#include<time.h>
#include<string.h>
#include<algorithm>

using namespace std;

typedef vector<int> vi; 
typedef vector<string> vs; 

#define minx(i,j) ((i)<(j)?(i):(j))
#define maxx(i,j) ((i)>(j)?(i):(j))
#define abx(i) ((i)>0?(i):(-(i)))
#define eps 1e-9

map<string,int>wqb;
int n,m;
char str[128];
int a[1024],dp[1024][1024];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,j,k;
	int ans;
	int ncase,icase=1;
	for(scanf("%d",&ncase);ncase--;)
	{
		scanf("%d\n",&n);
		wqb.clear();
		for(i=0;i<n;i++)
		{
			gets(str);
			wqb[str]=i+1;
		}
		scanf("%d\n",&m);
		for(i=0;i<m;i++)
		{
			gets(str);
			a[i]=wqb[str];
		}
		memset(dp,-1,sizeof(dp));
		for(i=1;i<=n;i++)
			dp[0][i]=0;
		dp[0][a[0]]=-1;n++;
		for(i=1;i<m;i++)		
			for(j=1;j<n;j++)
				if(a[i]!=j)
				{
					if(dp[i-1][a[i]]>=0)
						dp[i][j]=dp[i-1][a[i]]+1;
					k=dp[i-1][j];
					if(k>=0&&(dp[i][j]<0||k<dp[i][j])) 
						dp[i][j]=k;
			 }
		ans=0x7fffffff;
		for(i=1;i<n;i++)
			if(dp[m-1][i]>=0&&dp[m-1][i]<ans)
				ans=dp[m-1][i];
		printf("Case #%d: %d\n",icase++,ans);
	}
	return 0;
}