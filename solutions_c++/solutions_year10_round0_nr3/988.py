#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <list>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair
#define pi acos(-1.0)
#define MAXN 1010
#define inf 1000000000
#define eps 1e-5
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

int main()
{
	long long cs,c,r,k,n,i,j,ans,beg,cnt,g[1010],sum,tot[2010],end[2010];
	freopen("C-large.in","r",stdin);	
	freopen("C-large.out","w",stdout);	
	scanf("%I64d",&cs);
	for (c=1;c<=cs;c++)
	{
		scanf("%I64d%I64d%I64d",&r,&k,&n);
		sum=0;
		for (i=0;i<n;i++)
		{
			scanf("%I64d",&g[i]);
			sum+=g[i];
		}
		memset(tot,0,sizeof(tot));
		for (i=0;i<n;i++)
		{
			beg=i;
			while (1)
			{
				if (tot[i]+g[beg]<=k) tot[i]+=g[beg];
				else break;
				beg=(beg+1)%n;
				if (beg==i) break;
			}
			end[i]=beg;
		}
		
		beg=0;
		ans=0;
		for (i=0;i<r;i++)
		{
			ans+=tot[beg];
			beg=end[beg];
		}
		printf("Case #%I64d: %I64d\n",c,ans);
	}
	return 0;
}
