#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<cstdio>
#include <iomanip>


using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define istr(S) istringstream sin(S)
#define MP make_pair
#define pb push_back
#define inf 1000000000

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<pi> vpi;

#define inf 1000000000

//typedef long long LL;
typedef __int64 LL;

int dp[20002];

int main()
{
	int i,j,k,l,tests,cs=0,n;
	LL L;

	//freopen("D:\\gcj\\A-large.in","r",stdin);
	freopen("D:\\gcj\\B-small0.out","w",stdout);

	scanf("%d",&tests);
	while(tests--)
	{
		scanf("%I64d%d",&L,&n);

		for(i=1;i<=20000;i++)
			dp[i]=inf;

		for(i=0;i<n;i++)
		{
			scanf("%d",&k);
			for(j=k;j<=20000;j++)
				dp[j]=MIN(dp[j],dp[j-k]+1);
		}

		LL ans=-1;

		for(i=1;i<=20000;i++)
		{
			if(dp[i]==inf || dp[L%i]==inf) continue;
			LL need=(LL)(L/i)*dp[i];
			need+=dp[L%i];

			if(ans<0 || need<ans)
				ans=need;

		}

		if(ans<0)
			printf("Case #%d: IMPOSSIBLE\n",++cs);
		else
			printf("Case #%d: %I64d\n",++cs,ans);
	}

	return 0;
} 


