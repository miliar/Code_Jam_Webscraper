#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int mapp[25][25];
int vp[25],vq[25];
int quan[25][25];
int qt;

int check(int a[],int t)
{
	int i,j;
	for(i=0;i<t;++i)
	{
		int aa=a[i],bb=a[(i+1)%t];
		if(mapp[aa][bb]==0) return 0;
	}
	for(i=0;i<t;++i)
	{
		for(j=i+1;j<t;++j)
		{
			int aa=a[i],bb=a[j];
			if(i==0&&j==t-1) continue;
			if(abs(i-j)==1) continue;
			if(mapp[aa][bb]==1) return 0;
		}
	}
	return 1;
}

int main()
{
	int cas=1;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("outC.txt","w",stdout);
	int T;scanf("%d",&T);
	while(T--)
	{
		int i,j,k;

		int N,M;scanf("%d%d",&N,&M);
		memset(mapp,0,sizeof(mapp));
		memset(quan,0,sizeof(quan));
		qt=0;
		for(i=0;i<M;++i)
			scanf("%d",vp+i);
		for(i=0;i<M;++i)
			scanf("%d",vq+i);
		for(i=1;i<N;++i)
		{
			mapp[i][i-1]=1;
			mapp[i-1][i]=1;
		}
		mapp[0][N-1]=mapp[N-1][0]=1;
		for(i=0;i<M;++i)
		{
			mapp[vp[i]-1][vq[i]-1]=mapp[vq[i]-1][vp[i]-1]=1;
		}
		int minn=20;
		for(i=0;i<(1<<N);++i)
		{
			int cnt[20],t=0;
			for(j=0;j<N;++j)
			{
				if((1<<j)&i) cnt[t++]=j;
			}
			if(t>=3)
			{
				if(check(cnt,t))
				{
					minn=min(minn,t);
					for(j=0;j<t;++j)
					{
						quan[cnt[j]][++quan[cnt[j]][0]]=qt;
					}
					qt++;
				}
			}
		}
		int po=1;
		int ans[20];
		
		for(i=0;i<N;++i)
		{
			po*=minn;
		}
		for(i=0;i<po;++i)
		{
			int kl=i;
			int sun[20]={0};
			int aa[10]={0},tt=0;
			while(kl) aa[tt++]=kl%minn,kl/=minn;
			int pp=0,su=0;
			for(j=0;j<minn;++j)
			{
				if(pp&(1<<j)) continue;
				su++;pp|=(1<<j);
			}
			if(su!=minn) continue;
			for(j=0;j<N;++j)
			{
				for(k=1;k<=quan[j][0];++k)
				{
					int kl=quan[j][k];
					sun[kl]|=(1<<aa[j]);
				}
			}
			for(j=0;j<qt;++j)
			{
				if(sun[j]!=(1<<minn)-1) break;
			}
			if(j==qt)
			{
				for(j=0;j<N;++j)
					ans[j]=aa[j];
				break;
			}
		}
		printf("Case #%d: %d\n",cas++,minn);
		for(i=0;i<N-1;++i)
			printf("%d ",ans[i]+1);
		printf("%d\n",ans[N-1]+1);
	}
}