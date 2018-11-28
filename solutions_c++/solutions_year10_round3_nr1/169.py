#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

int N;

struct MM
{
	int a,b;
}mm[1000];

bool cmp(MM a,MM b)
{
	return a.a < b.a;
}

int main()
{
	int T,i,j;
	//freopen("A-large.in","r",stdin);
	//freopen("A.out","w",stdout);
	scanf("%d",&T);
	for(int Case = 1;Case <= T;Case++)
	{
		scanf("%d",&N);
		for(i = 0;i < N;i++)
			scanf("%d%d",&mm[i].a,&mm[i].b);
		sort(mm,mm + N,cmp);
		int ans = 0;
		for(i = 0;i < N;i++)
			for(j = i + 1;j < N;j++)
			{
				if(mm[i].b > mm[j].b)
					ans++;
			}
		printf("Case #%d: %d\n",Case,ans);
	}
	return 0;
}
