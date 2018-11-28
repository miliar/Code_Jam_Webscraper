#include <queue>
#include <iostream>
#include <vector>
using namespace std;

int T,cas;

int main()
{
	int N,K,i;

	scanf("%d",&T);
	for (cas=1;cas<=T;cas++)
	{
		scanf("%d%d",&N,&K);
		for (i=0;i<N;i++)
		{
			if (K%2==0) break;
			K/=2;
		}
		printf("Case #%d: ",cas);
		if (i==N) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}