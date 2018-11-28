#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int num[101];
int main()
{
	freopen("C-small-attempt2.in","r",stdin);
	freopen("C.out","w",stdout);
	int T,N,L,H;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%d%d%d",&N,&L,&H);
		for(int i=0;i<N;i++)
			scanf("%d",num+i);
		
		printf("Case #%d: ",t);
		int i;
		for(i=L;i<=H;i++)
		{
			int j;
			for(j=0;j<N;j++)
				if(i%num[j]!=0&&num[j]%i!=0)
					break;
			if(j==N)
			{
				printf("%d\n",i);
				break;
			}
		}
		if(i==H+1)
		printf("NO\n");
	
	}
	return 0;
}
