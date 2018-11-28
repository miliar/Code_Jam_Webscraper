#include<iostream> 
#include<cstdio> 
#include<algorithm> 
#include<cstring> 
#include<cmath> 
#include<vector> 
#include<queue> 
#include<map>
typedef long long lld; 
using namespace std; 
#define clr(NAME,VALUE) memset(NAME,VALUE,sizeof(NAME)) 
#define MAX 0x7f7f7f7f 
#define N 110
int mp[N][N];
int mp1[N][N];
int mp2[N][N];
int maxn;
bool check()
{
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<N;j++)
		{
			if(mp[i][j]!=0)
			return 0;
		}
	}
	return 1;
}
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("a.txt","r",stdin);
	#endif
	freopen("b.txt","w",stdout);
	int T,csn=1;
	scanf("%d",&T);
	int R;
	int x1,y1,x2,y2;
	while(T--)
	{
		clr(mp,0);
		scanf("%d",&R);
		while(R--)
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			if(x1>x2)
			swap(x1,x2);
			if(y1>y2)
			swap(y1,y2);
			for(int i=x1;i<=x2;i++)
			{
				for(int j=y1;j<=y2;j++)
				{
					mp[i][j]=1;
				}
			}
		}
//		for(int i=1;i<6;i++)
//			{
//				for(int j=1;j<6;j++)
//				{
//					cout<<mp[i][j]<<" ";
//				}
//				cout<<endl;
//			}
//			cout<<endl;
		int ans=0;
		int fn,fw;
		int bj=0;
		while(1)
		{
			clr(mp2,0);
			for(int i=1;i<N;i++)
			{
				for(int j=1;j<N;j++)
				{
					mp2[i][j]=mp[i][j];
				}
			} 
			clr(mp1,0);
			for(int i=1;i<N;i++)
			{
				for(int j=1;j<N;j++)
				{
					if(mp[i][j]==1)
					continue;
					fn=0,fw=0;
					if(i==1)
					fn=0;
					else
					{
						if(mp[i-1][j]==1)
						fn=1;
					}
					if(j==1)
					fw=0;
					else
					{
						if(mp[i][j-1]==1)
						fw=1;
					}
					if(fn==1&&fw==1)
					{
						mp1[i][j]=1;
					}
				}
			}
	//		for(int i=1;i<6;i++)
//			{
//				for(int j=1;j<6;j++)
//				{
//					cout<<mp[i][j]<<" ";
//				}
//				cout<<endl;
//			}
			for(int i=1;i<N;i++)
			{
				for(int j=1;j<N;j++)
				{
					if(mp[i][j]==0)
					continue;
					fn=0,fw=0;
					if(i==1)
					fn=1;
					else
					{
						if(mp[i-1][j]==0)
						fn=1;
					}
					if(j==1)
					fw=1;
					else
					{
						if(mp[i][j-1]==0)
						fw=1;
					}
					if(fn==1&&fw==1)
					{
						mp2[i][j]=0;
					}
				}
			}
			clr(mp,0);
	//		for(int i=1;i<6;i++)
//			{
//				for(int j=1;j<6;j++)
//				{
//					cout<<mp[i][j]<<" ";
//				}
//				cout<<endl;
//			}
//			cout<<endl;
			for(int i=1;i<N;i++)
			{
				for(int j=1;j<N;j++)
				{
					if(mp2[i][j]==1||mp1[i][j]==1)
					{
						mp[i][j]=1;
					}
				}
			}
	//		for(int i=1;i<6;i++)
//			{
//				for(int j=1;j<6;j++)
//				{
//					cout<<mp1[i][j]<<" ";
//				}
//				cout<<endl;
//			}
//			cout<<endl;
			ans++;
			if(check())
			break;
		}
		printf("Case #%d: %d\n",csn++,ans); 
	}
	#ifndef ONLINE_JUDGE
//    while(1);
	#endif
	return 0;
}
