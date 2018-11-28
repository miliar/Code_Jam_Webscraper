#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

int C[1005],N;

int main()
{
	freopen("d://C-large.in","r",stdin);
	freopen("d://project.txt","w",stdout);
	int _,cases=1;
	scanf("%d",&_);
	while(_--)
	{
		scanf("%d",&N);
		int v=0,sum=0,minV=100000000;
		for(int i=1;i<=N;i++)
		{
			scanf("%d",&C[i]);
			v^=C[i];
			sum+=C[i];
			minV=min(minV,C[i]);
		}
		printf("Case #%d: ",cases++);
		if(v!=0) printf("NO\n");
		else printf("%d\n",sum-minV);
	}
	return 0;
}