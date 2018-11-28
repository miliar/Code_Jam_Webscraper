#include <iostream>
#include <math.h>
using namespace std;

int main(void)
{
	freopen("B-small.in","r",stdin);
	freopen("B-small.out","w",stdout);
	const double l2=log((double)2);
	int T;
	cin>>T;
	for(int W=1;W<=T;W++)
	{
		int L,P,C,sum=0;
		scanf("%d%d%d",&L,&P,&C);
		int now=P;
		while(now>L)
		{
			if(now%C==0) now=now/C;
			else now=now/C+1;
			//now--;
			sum++;
		}
		int ans=ceil(log((double)sum)/l2);
		printf("Case #%d: %d\n",W,ans);
	}
}