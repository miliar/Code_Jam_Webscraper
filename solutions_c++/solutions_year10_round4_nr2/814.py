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
#define N 1100
int a[N];
int b[N][N];
int fang[12];
void init()
{
	fang[0]=1;
	fang[1]=2;
	for(int i=2;i<=10;i++)
	fang[i]=fang[i-1]*2;
}
int ans,p;
int dfs(int nn,int st,int ed)
{
//	cout<<"st "<<st <<" "<<ed<<endl;
	if(nn==p)
	{
		if(min(a[st],a[ed])<p-nn+1)
		{
			ans++;
		}
		return min(a[st],a[ed]);
	}
	int bj=min(dfs(nn+1,st,(st+ed)/2),dfs(nn+1,((st+ed)/2)+1,ed));
	if(bj<p-nn+1)
	{
		ans++;
	}
	return bj;
}
	
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("a.txt","r",stdin);
	#endif
	freopen("b.txt","w",stdout);
	int T,csn=1;
	scanf("%d",&T);
	int n;
	int tmp;
	init();
	while(T--)
	{
		scanf("%d",&p);
		n=fang[p];
		for(int i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
		}
		for(int i=p-1;i>=0;i--)
		{
			for(int j=0;j<fang[i];j++)
			{
				scanf("%d",&tmp);
			}
		}
//		for(int i=0;i<n;i++)
//		{
//			cout<<a[i]<<" ";
//		}
//		cout<<endl;
		ans=0;
		dfs(1,0,n-1);
		
		printf("Case #%d: %d\n",csn++,ans);
	}
	#ifndef ONLINE_JUDGE
//    while(1);
	#endif
	return 0;
}
