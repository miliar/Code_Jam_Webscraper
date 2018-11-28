#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<string>
#include<iostream>
#define swap(a, b)  ((a) == (b) || (a) ^= (b), (b) ^= (a), (a) ^= (b))
using namespace std;
typedef int TT;
typedef __int64 ll;
TT abs(TT x)
{
	return x>0?x:-x;
}
TT min(TT x,TT y)
{
	return x<y?x:y;
}
TT max(TT x,TT y)
{
	return x>y?x:y;
}
const int INF = 1000000000;
#define mp(x,y) make_pair(x,y)
typedef pair<int,int>per;
const int N = 10005;
struct P
{
	int d,l;
}data[N];
int dp[N];
int main()
{
	freopen("A-large (1).in","r",stdin);
	freopen("out.txt","w",stdout);
	int n,ca=1,T,D,i,j;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",ca++);
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d%d",&data[i].d,&data[i].l);
		}
		scanf("%d",&D);
		int flag=0,len=min(data[0].d,data[0].l);
		memset(dp,0,sizeof(dp));
		dp[0]=len;
		for(i=0;i<n;i++)
		{
			if(data[i].d+dp[i]>=D){flag=1;break;}
			for(j=i+1;j<n;j++)
			{
				if(data[i].d+dp[i]>=data[j].d)
				{
					dp[j]=max(dp[j],min(abs(data[j].d-data[i].d),data[j].l));
				}
			}
		}
		if(!flag)puts("NO");
		else puts("YES");
	}
	return 0;
}