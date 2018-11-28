#include <iostream>
using namespace std;

int main(void)
{
	freopen("snap.in","r",stdin);
	freopen("snap.out","w",stdout);
	int t;
	cin>>t;
	for(int m=1;m<=t;m++)
	{
		int n,k;
		bool tag=0;
		scanf("%d%d",&n,&k);
		for(int i=0;i<n;i++)
		{
			if(!(k & (1<<i)))
			{
				printf("Case #%d: OFF\n",m);
				tag=1;
				break;
			}
		}
		if(tag==0)
			printf("Case #%d: ON\n",m);
	}
	return 0;
}