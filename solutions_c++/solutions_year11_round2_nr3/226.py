#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
#define MAXN 10
int n,m;
int u[MAXN],v[MAXN];
int max_color;
int parts[MAXN];
int power[MAXN];
int color[MAXN];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int caseN;
	cin>>caseN;
	for (int caseI=1;caseI<=caseN;caseI++)
	{
		cin>>n>>m;
		parts[0]=(1<<n)-1;
		for (int i=1;i<=m;i++)
			cin>>u[i];
		for (int i=1;i<=m;i++)
			cin>>v[i];
		for (int i=1;i<=m;i++)
		{
			u[i]--;
			v[i]--;
			for (int j=0;j<i;j++)
				if ((parts[j]&(1<<u[i]))&&(parts[j]&(1<<v[i])))
				{
					parts[i]=(1<<u[i])|(1<<v[i]);
					for (int k=u[i]+1;k<v[i];k++)
						if (parts[j]&(1<<k))
						{
							parts[j]^=1<<k;
							parts[i]^=1<<k;
						}
					break;
				}
		}
		m++;
		for (int i=0;i<m;i++)
		{
			for (int j=0;j<n;j++)
				if (parts[i]&(1<<j))
					cerr<<j<<' ';
			cerr<<endl;
		}
		max_color=n;
		for (int i=0;i<m;i++)
		{
			int now=0;
			for (int j=0;j<n;j++)
				if (parts[i]&(1<<j))
					now++;
			max_color=min(max_color,now);
		}
		cerr<<max_color<<endl;
		for (int ans=max_color;ans;ans--)
		{
			cerr<<"checking "<<ans<<endl;
			power[0]=1;
			for (int i=1;i<=n;i++)
				power[i]=power[i-1]*ans;
			bool valid_ans=false;
			for (int s=0;s<power[n];s++)
			{
				int temp=s;
				for (int i=0;i<n;i++)
				{
					color[i]=temp%ans;
					temp/=ans;
				}
				bool valid_color=true;
				for (int i=0;i<m;i++)
				{
					bool flag[MAXN];
					memset(flag,false,sizeof(flag));
					for (int j=0;j<n;j++)
						if (parts[i]&(1<<j))
							flag[color[j]]=true;
					if (count(flag,flag+ans,false))
					{
						valid_color=false;
						break;
					}
				}
				if (valid_color)
				{
					valid_ans=true;
					break;
				}
			}
			if (valid_ans)
			{
				printf("Case #%d: %d\n",caseI,ans);
				for (int i=0;i<n;i++)
					printf("%d%c",color[i]+1,i<n-1?' ':'\n');
				break;
			}
		}
	}
	return 0;
}
