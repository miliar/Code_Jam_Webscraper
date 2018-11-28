#include <cstdio>
#include <cmath>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <utility>
#include <stack>
#include <queue>
#include <map>

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define pi 2*acos(0.0)
#define eps 1e-9
#define PII pair<int,int> 
#define PDD pair<double,double>
#define LL long long
#define INF 1000000000

using namespace std;

int bts,T,N,x,y,z,ans,temp1,temp2,dpt;
int can[20];

int main()
{
	scanf("%d",&T);
	for(z=1;z<=T;z++)
	{
		scanf("%d",&N);
		for(x=0;x<N;x++) scanf("%d",&can[x]);
		ans=0;
		bts=(1<<N)-1;
		for(x=0;x<bts;x++)
		{
			temp1=temp2=dpt=0;
			for(y=0;y<N;y++) if(x&(1<<y))
			{
				temp1^=can[y];
				dpt+=can[y];
			} else temp2^=can[y];
			//printf("%d %d %d %d\n",x,temp1,temp2,dpt);
			if(temp1==temp2) ans=max(ans,dpt);
		}
		printf("Case #%d: ",z);
		if(!ans) printf("NO\n"); else printf("%d\n",ans);
	}
	return 0;
}

