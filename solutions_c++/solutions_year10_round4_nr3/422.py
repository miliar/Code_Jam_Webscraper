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
#include<cstdio>
#include<cstring>
#include<memory.h>
using namespace std;

typedef long long LL;

#define INF 0x7fffffff
#define PI acos(-1.0)
#define EPS (1e-10)

#define SZ(a) int((a).size())
#define PB push_back
#define MP make_pair

#define M 105

int gcd(int a,int b){return b>0?gcd(b,a%b):a;}

bool mp[M][M],tmp[M][M];

int main()
{
	freopen("C:\\Users\\LL\\Desktop\\GCJ\\1.in","r",stdin);
	freopen("C:\\Users\\LL\\Desktop\\GCJ\\1.out","w",stdout);

	int csNum,cs;
	scanf("%d",&csNum);
	for(cs=1;cs<=csNum;cs++)
	{
		int n,r,i,j,x1,y1,x2,y2,t;
		scanf("%d",&r);
		memset(mp,0,sizeof(mp));
		while(r--)
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for(i=x1;i<=x2;i++)
				for(j=y1;j<=y2;j++)
					mp[j][i]=1;
		}
		for(t=1;;t++)
		{
			memcpy(tmp,mp,sizeof(mp));
			bool flag=0;
			for(i=1;i<=M;i++)
				for(j=1;j<=M;j++)
				{
					mp[i][j]=tmp[i][j];
					if(!tmp[i][j]&&tmp[i-1][j]&&tmp[i][j-1])
						mp[i][j]=1;
					if(tmp[i][j]&&!tmp[i-1][j]&&!tmp[i][j-1])
						mp[i][j]=0;
					if(mp[i][j])
						flag=1;
				}
			if(!flag)
				break;
		}
		printf("Case #%d: %d\n",cs,t);
	}
}