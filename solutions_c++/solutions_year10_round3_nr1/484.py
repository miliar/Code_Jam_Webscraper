#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<map>
#include<vector>
#include<queue>
using namespace std;

typedef struct
{
	int a,b;
}Edge; 

int T,N,A,B;
Edge e[1001];

int main()
{
	int i;
	int Case=1;
	freopen("A-large(2).in","r",stdin);
	freopen("Output.txt","w",stdout);
	scanf("%d",&T);
	for(;T>0;T--)
	{
		scanf("%d",&N);
		for(i=1;i<=N;i++)
		{
			scanf("%d%d",&A,&B);
			e[i].a = A , e[i].b = B;
		}
		int ans = 0;
		for(i=1;i<N;i++)
		{
			for(int j=i+1;j<=N;j++)
			{
				if((e[i].a > e[j].a && e[i].b < e[j].b ) || (e[i].a < e[j].a && e[i].b > e[j].b ))
					ans++;
			}
		}
		printf("Case #%d: %d\n",Case++,ans);
	}
	return 0;
}
