#include <cstdio>
#include <cstring>
#include <algorithm>
#define MAX 1005
using namespace std;

#define two(_X) 				(1<<_X)
#define getBit(_mask,_bit) ((_mask&two(_bit))>0)

int N;
int candy[MAX];

int main()
{
	int cases,iD=1;

	for(scanf("%d",&cases);cases--;)
	{
		scanf("%d",&N);
		for(int i=0;i<N;i++)
			scanf("%d",&candy[i]);

		int sean=0;
		for(int i=two(N)-2;i;i--)
		{
			int S=0,P=0;
			int SC=0,PC=0;
			for(int j=0;j<N;j++)
			{
				if(getBit(i,N-1-j)) { S^=candy[j];SC+=candy[j]; }
				else { P^=candy[j];PC+=candy[j]; }
			}
			if(S==P && SC>0 && PC>0) sean=max(sean,SC);
		}
		printf("Case #%d: ",iD++);
		if(sean==0) puts("NO");
		else printf("%d\n",sean);
	}

	return 0;
}

