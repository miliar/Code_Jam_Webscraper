#include <iostream>
using namespace std;
#define MAXN 10

int T,N,K,power;
bool status[MAXN];

int main()
{
	freopen("A-small-attempt0.in","rb",stdin);
	freopen("A-small-attempt0.out","wb",stdout);
	scanf("%d",&T);
	for (int k=1;k<=T;k++)
	{
		scanf("%d%d",&N,&K);
		memset(status,0,sizeof(status));
		power=0;
		for (int i=0;i<K;i++)
		{
			for (int j=0;j<=power && j<N;j++)
				status[j]=!status[j];
			power=0;
			while (status[power] && power<N)
				power++;
		}
		printf("Case #%d: ",k);
		if (status[N-1] && power==N)
			puts("ON");
		else
			puts("OFF");
	}
	return 0;
}