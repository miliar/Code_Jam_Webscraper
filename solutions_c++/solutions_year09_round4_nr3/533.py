#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int ok[17][17];
int a[50][50];
int n,k;

int f(int x,int y)
{
int d=0;
if(a[x][0]==a[y][0])return 0;
if(a[x][0]>a[y][0])d=1;
for(int i=1;i<k;++i)
{
if(a[y][i]==a[x][i] || (d==1 && a[x][i]<a[y][i]) || (d==0 && a[x][i]>a[y][i]) )return 0;
}
return 1;
}


int dp[1<<17];
int mg[1<<17];
int X[20];

int g(int mask)
{
 if(mg[mask]!=-1)return mg[mask];
 int xx=0;
 for(int i=0;i<n;++i)if(mask&(1<<i))X[xx++]=i;
 for(int i=0;i<xx;++i)
         for(int j=i+1;j<xx;++j)
         if(ok[X[i]][X[j]]==0)
         return mg[mask]=0;
  return mg[mask]=1;     
}
int cnt[1<<16];
int go(int mask)
{
 if(mask==0)return 0;
 int &ret=dp[mask];
 if(ret==-1)
 {
  ret=cnt[mask];
  for(int temp=mask;temp;temp=mask&(temp-1))if(g(temp))
  {
   int tem=go(mask&(~temp))+1;
   if(ret>tem)ret=tem;        
  }
 }
 return ret;    
}

int main()
{
//	freopen("C.in","r",stdin);
	freopen("C:\\data\\C-small-attempt0.in","r",stdin);freopen("C:\\data\\C-small-attempt0.out","w",stdout);
//	freopen("C-small-attempt1.in","r",stdin);freopen("C-small-attempt1.out","w",stdout);
//	freopen("C:\\data\\C-large.in","r",stdin);freopen("C:\\data\\A-large.out","w",stdout);
   cnt[0]=0;
   for(int i=0;i<1<<16;++i)cnt[i]=cnt[i>>1]+(i&1);
	int t;
	scanf("%d",&t);
	for (int cas=1;cas<=t;cas++)
	{
		printf("Case #%d: ",cas);
		scanf("%d %d",&n,&k);
		memset(ok,0,sizeof(ok));
		for(int i=0;i<n;++i)
		        for(int j=0;j<k;++j)
		        scanf("%d",&a[i][j]);
            for(int i=0;i<n;++i)
            for(int j=0;j<n;++j)
            ok[i][j]=f(i,j);
         memset(dp,255,sizeof(dp));
         memset(mg,255,sizeof(mg));
         printf("%d\n",go((1<<n)-1));
	}
	return 0;
}
