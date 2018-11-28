#include <cstdio>
#include <string>
#include <cstring>
using namespace std;
const int MAXN=100+10;
const int MAXM=1000+10;
const int MAXK=100+10;
bool eq[MAXN][MAXM];
char s[MAXN][MAXK];
char s1[MAXM][MAXK];

int dp[MAXN];
int dp1[MAXN];
const int INF=1<<29;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,z,n,m,i,j;
	scanf("%d",&t);
	int mm;
	for(z=0;z<t;z++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf(" %[^\n] ",s[i]);
			//fprintf(stderr,"%s\n",s[i]);
		}
		scanf("%d",&m);
		for(i=0;i<m;i++)
			scanf(" %[^\n] ",s1[i]);
		
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				eq[i][j]=(strcmp(s[i],s1[j])==0);
			
		for(i=0;i<n;i++)
			dp[i]=0;
		mm=0;
		for(i=0;i<m;i++)
		{
			for(j=0;j<n;j++)
			{
				dp1[j]=INF;
				if(eq[j][i]) continue;
				dp1[j]=min(mm+1,dp[j]);
			}
			mm=INF;
			for(j=0;j<n;j++)
			{
				dp[j]=dp1[j];
				if(mm>dp[j]) mm=dp[j];
			}				
		}		
			
		
		printf("Case #%d: %d\n",z+1,mm);
	}
	return 0;
}
