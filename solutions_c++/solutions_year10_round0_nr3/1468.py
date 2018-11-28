#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<iterator>
using namespace std;



#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define pi acos(-1.0)
#define inf ((i64)1<<30)
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define pb push_back
#define all(a) a.begin(),a.end()
#define eps 1e-11
#define i64 __int64


int main()
{
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	i64 cs,t=1,r,n,k,a[2009],next[1009],sum[1009],i,j,cnt;
	scanf("%I64d",&cs);
	while(cs--)
	{
		scanf("%I64d %I64d %I64d",&r,&k,&n);
		for(i=0;i<n;i++)
		{
			scanf("%I64d",&a[i]);
		}
		for(i=n;i<2*n;i++)
		{
			a[i]=a[i-n];
		}
		CLR(sum);
		for(i=0;i<n;i++)
		{
			for(j=i;j<i+n;j++)
			{
				if(sum[i]+a[j]>k)
				{
					break;
				}
				sum[i]+=a[j];
				next[i]=(j+1)%n;
			}
		}
		cnt=0;
		j=0;
		for(i=0;i<r;i++)
		{
			cnt+=sum[j];
			j=next[j];
		}
		printf("Case #%I64d: %I64d\n",t++,cnt);
	}
	return 0;
}


