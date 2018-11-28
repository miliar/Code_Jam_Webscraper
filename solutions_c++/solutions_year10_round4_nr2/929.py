#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <queue>
#include <string.h>
using namespace std;

#define N 505
#define PI acos(-1.0)
#define inf 2100000000
#define eps 1e-10
#define ll __int64
#define max(a,b) a>b?a:b
#define min(a,b) a<b?a:b
#define mod 100003
bool pri[N];
ll cost[N][N],dp[N][N];
int md[2][13]={{0,31,28,31,30,31,30,31,31,30,31,30,31}, {0,31,29,31,30,31,30,31,31,30,31,30,31}};
int isleap(int year){return (!(year%4)&&year%100)||!(year%400);}
void prim(){pri[0]=1;pri[1]=1;int i;long long j;for(i=2;i<N;i++){if(pri[i]==0){for(j=i,j=j*i;j<N;j+=i){pri[j]=1;}}}}
int arr[1030];
int main()
{
	int t,n,i,j,g=0,p,ans,a;
		freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		g++;
		scanf("%d",&p);
		ans=(1<<p)-1;
		for(i=0;i<(1<<p);i++)
		{
			scanf("%d",&arr[i]);
		}
		for(i=1;i<=( (1<<p) -1);i++)
		{
			scanf("%d",&a);
		}
		for(i=0;i<p;i++)
		{
			for(j=0;j<( 1<<(p-i) );j+=2)
			{
				if(arr[j]!=0&&arr[j+1]!=0)
				{
					ans--;
					arr[j]--;arr[j+1]--;
				}
				arr[j/2]=min(arr[j],arr[j+1]);
			}
		}
		printf("Case #%d: %d\n",g,ans);
	}
	return 0;
}
//printf("%d")
//	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);