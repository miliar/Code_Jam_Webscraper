
#include<cstdio>
#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<string>
#include<cstdlib>
#include<climits>
#include<cstring>
using namespace std;
#define PB push_back
#define INF 1000000010
#define MOD 1000000007
void precompute(void)
{
}
long long int d[1024*16],l[1024*16],reach[1024*16];
int main()
{
	int test=0,t;
	int n,i,j;
	precompute();
	while(scanf("%d",&t)!=EOF)
	{
		test=0;
		while(t--)
		{
			test++;
			printf("Case #%d: ",test);
			fprintf(stderr,"Case #%d: started\n",test);
			scanf("%d",&n);
			for(i=0;i<n;i++)
			{
				scanf("%lld%lld",&d[i],&l[i]);
				reach[i]=-1;
			}
			scanf("%lld",&d[i]);
			l[i]=INF;
			reach[i]=-1;
			
			reach[0]=d[0];	
			for(i=0;i<n;i++)
			{
				if(reach[i]==-1)
					continue;
				for(j=i+1;j<=n;j++)
				{
					if(d[j]>d[i]+reach[i])
						break;
					reach[j]=max(min(min(l[j],reach[i]),d[j]-d[i]),reach[j]);
				}
			}
			if(reach[n]!=-1)
			{
				printf("YES\n");
			}
			else
				printf("NO\n");
		}
	}
	return 0;
}
