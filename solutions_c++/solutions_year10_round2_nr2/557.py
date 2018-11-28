#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>
#include <string>

using namespace std;

int loc[100],vv[100];
int sum[100],flag[100];

int main()
{
	freopen("test.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int case_t;
	int i,j;
	int oop=1;
	scanf("%d",&case_t);
	while(case_t--)
	{
		int n,k,b,t;
		scanf("%d%d%d%d",&n,&k,&b,&t);
		for(i=0;i<n;++i)
			scanf("%d",&loc[i]);
		for(i=0;i<n;++i)
			scanf("%d",&vv[i]);
		int tt=0;
		memset(sum,0,sizeof(sum));
		memset(flag,0,sizeof(flag));
		for(i=n-1;i>=0;--i)
		{
			if(t*vv[i]+loc[i]>=b)
				tt++;
			else break;
		}
		int hj=i;
		int ans=0;
		if(tt>=k)
		{
			printf("Case #%d: 0\n",oop++);
			continue;
		}
		k-=tt;
		for(i=i-1;i>=0;--i)
		{
			if(k==0) break;
			if(t*vv[i]+loc[i]>=b)
			{
				flag[i]=1;
				k--;
				for(j=i+1;j<=hj;++j)
				{
					if(!flag[j])
					{
						sum[i]++;
					}
					else
					{
						sum[i]+=sum[j];
						break;
					}
				}
			}
		}
		if(k)
		{
			printf("Case #%d: IMPOSSIBLE\n",oop++);
			continue;
		}
		for(i=0;i<n;++i)
			ans+=sum[i];
		printf("Case #%d: %d\n",oop++,ans);
	}
}