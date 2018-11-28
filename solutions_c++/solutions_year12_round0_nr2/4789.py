#include <cstdio>

using namespace std;
int T,S,p,N,x;
int main()
{
	scanf("%d",&N);
	for(int i=1;i<=N;i++)
	{
		scanf("%d%d%d",&T,&S,&p);
		int result = 0;
		for(int j=0;j<T;j++)
		{
			scanf("%d",&x);
			if(p*3-2 <= x)
			{result++; continue;}
			if(p*3-4 <= x && (p*3-4)>=0)
			{
				if(S>0) {result++; S--;}
			}
		}
		printf("Case #%d: %d\n",i,result);
	}


	return 0;
}
