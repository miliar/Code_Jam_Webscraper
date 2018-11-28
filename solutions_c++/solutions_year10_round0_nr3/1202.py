#include <iostream>
#include <string.h>
using namespace std;
int r,k,n;
int num[1001];
int sum[1001][1001];
int rem[1001][1001];
bool flag[1001];
int next[1000];
int find_next(int s,int &he)//O(1000)
{
	he=0;
	int temp=k;
	int i;
	if(sum[s][n-1]>=temp)
	{
		for(i=s;i<=n-1;i++)
		{
			if(sum[s][i]>temp)
			{
				he=sum[s][i-1];
				return i;
			}
			if(sum[s][i]==temp)
			{
				he=sum[s][i];
				return (i+1)%n;
			}
		}
	}
	else
	{
		temp-=sum[s][n-1];
		he+=sum[s][n-1];
		if(sum[0][s-1]<=temp)
		{
			he+=sum[0][s-1];
			return s;
		}
		for(i=0;i<=s-1;i++)
		{
			if(sum[0][i]>temp)
			{
				he+=sum[0][i-1];
				return i;
			}
		}
	}
}


int main()
{
	freopen("C-small-attempt2.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,i,j,d;
	scanf("%d",&t);
	int s,cyc,cnt,he,cyc_num;
	__int64 ans,cyc_sum;
	int Case=0;
	bool find,f;
	while(t--)
	{
		find=0;
		scanf("%d%d%d",&r,&k,&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&num[i]);
			sum[i][i]=num[i];
		}
		memset(flag,0,sizeof(flag));
		for(d=1;d<n;d++)
			for(i=0;i<n-d;i++)
				sum[i][i+d]=sum[i][i+d-1]+num[i+d];
		s=0;
		while(!flag[s])
		{
			flag[s]=1;
			next[s]=find_next(s,he);
			rem[s][next[s]]=he;
			s=next[s];
		}
		cyc=s;s=0;//cyc为循环的起点
		ans=0;cnt=0;
		f=0;
		cyc_sum=0;cyc_num=0;
		while(1)
		{

			if(s==cyc && f==1)break;
			if(s==cyc)f=1;
			ans+=rem[s][next[s]];
			cnt++;
			if(f==1)
			{
				cyc_num++;
				cyc_sum+=rem[s][next[s]];
			}
			if(cnt==r)
			{
				find=1;
				printf("Case #%d: %I64d\n",++Case,ans);
				break;
			}
			s=next[s];
		}
		if(find==0)
		{
			cnt=r-cnt;
			ans+=(cnt/cyc_num)*cyc_sum;
			cnt%=cyc_num;
			for(i=1;i<=cnt;i++)
			{
				ans+=rem[s][next[s]];
				s=next[s];
			}
			printf("Case #%d: %I64d\n",++Case,ans);
		}
	}
	return 0;
}

			










