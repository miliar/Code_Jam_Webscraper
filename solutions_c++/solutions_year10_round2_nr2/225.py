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
#include<math.h>
#include<stack>
using namespace std;

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b)
#define ABS(X) ((X) < 0 ? (-(X)) : (X))
#define S(X) ((X)*(X))

typedef pair<int,int> PII;
typedef __int64 LL;

//int dr[]={0,-1,-1,-1,0,1,1,1};
//int dc[]={-1,-1,0,1,1,1,0,-1};

LL x[100],v[100],feasible[100];
LL t,b;

int main()
{
	//freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt10.out","w",stdout);
//	freopen("B-small-attempt1.in","r",stdin);freopen("B-small-attempt1.out","w",stdout);
//	freopen("B-small-attempt2.in","r",stdin);freopen("B-small-attempt2.out","w",stdout);
	freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
	
	int T,ks;
	LL now,ans,i,n,k,cnt;

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		scanf("%I64d%I64d%I64d%I64d",&n,&k,&b,&t);
		for(i=0;i<n;i++)
			scanf("%I64d",&x[i]);
		for(i=0;i<n;i++)
			scanf("%I64d",&v[i]);

		cnt=0;
		for(i=0;i<n;i++)
		{
			feasible[i] = (x[i]+v[i]*t >= b);
			cnt+=feasible[i];
		}

		if(cnt<k)
		{
			printf("Case #%d: IMPOSSIBLE\n",ks);
			continue;
		}

		if(!k)
		{
			printf("Case #%d: %d\n",ks,0);
			continue;
		}

		int j=0;
		now=ans=0;
		for(i=n-1;i>=0;i--)
		{
			if(feasible[i]==0) now++;
			else
			{
				j++;

				ans+=now;
				if(j==k) break;
			}
		}

		printf("Case #%d: %I64d\n",ks,ans);
	}

	return 0;
}