#include <iostream>
#include <algorithm>
using namespace std;

int main ()
{
	freopen("A-small-practice.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	int N,K;
	for(int t=1;t<=T;t++)
	{
		scanf("%d%d",&N,&K);
		printf("Case #%d: ",t);
		int i;
		for(i=0;i<N;i++)
			if((K&(1<<i))==0)
				break;
		if(i<N)
		{
			printf("OFF\n");
		}
		else
		{
			printf("ON\n");
		}
	}
	return 0;
}
