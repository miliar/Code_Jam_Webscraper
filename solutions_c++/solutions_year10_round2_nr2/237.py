#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<queue>
#include<set>
#include<algorithm>
#include<sstream>
#include<cmath>
#include<cstdlib>
#include<deque>
#include<list>
#include<stack>
using namespace std;

#define INF 0x7fffffff
#define PI acos(-1.0)
#define EPS (1e-10)
#define SZ(a) int((a).size())

typedef long long LL;

int gcd(int a,int b){return b>0?gcd(b,a%b):a;}

int main()
{
	freopen("C:\\Users\\LL\\Desktop\\GCJ\\1.in","r",stdin);
	freopen("C:\\Users\\LL\\Desktop\\GCJ\\1.out","w",stdout);

	int csNum,cs;
	scanf("%d",&csNum);
	for(cs=1;cs<=csNum;cs++)
	{
		int n,k,b,t,i,j,x[100],v[100];
		scanf("%d%d%d%d",&n,&k,&b,&t);
		for(i=0;i<n;i++)
			scanf("%d",&x[i]);
		for(i=0;i<n;i++)
			scanf("%d",&v[i]);
		int ans=0;
		for(i=n-1;i>=0;i--)
		{
			if(x[i]+t*v[i]>=b)
			{
				k--;
			}
			else
			{
				ans+=k;
			}
			if(k==0)
				break;
		}
		printf("Case #%d: ",cs);
		if(k>0)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",ans);
	}
}