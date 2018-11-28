#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <queue>
#include <map>

using namespace std;

int tem[2000];

int main()
{
	int i,j;
	int cas=1;
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;scanf("%d",&t);
	while(t--)
	{
		int n;scanf("%d",&n);
		int sun=0,maxx=1000000000;
		int su=0;
		for(i=0;i<n;++i)
		{
			scanf("%d",tem+i);
			maxx=min(maxx,tem[i]);
			su^=tem[i];
			sun+=tem[i];
		}
		printf("Case #%d: ",cas++);
		if(su!=0)
			printf("NO\n");
		else 
			printf("%d\n",sun-maxx);
	}
}