#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <map>
using namespace std;


void solve()
{


}

void trys(int n)
{
	int rank[40] = {0};
	int in[40] = {0};
	int count = 0;
	for(int t=0;t<(1<<(n-2));t++)
	{
		memset(rank,0,sizeof(rank));
		memset(in,0,sizeof(in));
		in[n]=1;
		for(int i=2;i<n;i++)
		{
			if((1<<(i-2)) & t) in[i]=1;
		}
		for(int i=2;i<=n;i++)
		{
			if(in[i]) for(int j=2;j<=i;j++) rank[i] += in[j];
		}


		int p=rank[n];
		while(1)
		{
			if(p==1) break;
			if(p==0) break;
			p=rank[p];
		}

/*
		for(int i=0;i<=n;i++)
			if(in[i]) printf("%d(%d) ",i,rank[i]);

		if(p==1)  printf(" YES");
		puts("");*/

		if(p==1) count++;
		count = count % 100003;

	}
	printf("%d,",count);
}

int ans[30] = {0,0,1,2,3,5,8,14,24,43,77,140,256,472,874,1628,3045,5719,10780,20388,38674,73562,40265,68060,13335,84884};
int main()
{
	/*
	for(int i=2;i<=25;i++)
	{
		trys(i);
	}
	puts("");
*/


	int Ti,T;
	scanf("%d",&T);
	for(Ti = 1; Ti <= T; Ti++)
	{
		printf("Case #%d: ",Ti);
		int n;
		scanf("%d",&n);
		printf("%d\n",ans[n]);
	}
}
