#include<iostream>

using namespace std;

int main()
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small.out","w",stdout);
	int i, T, ncase;
	bool visit;
	scanf("%d",&T);
	for(ncase= 1; ncase<=T; ncase++)
	{
		int n,k;
		scanf("%d %d",&n,&k);
		visit = true;
		for(i = 0; i < n; i++)
		{
			if(((k>>i)&1)==0)
			{
				visit = false;
				break;
			}
		}
		if(visit)
			printf("Case #%d: ON\n",ncase);
		else
			printf("Case #%d: OFF\n",ncase);
	}
	return 0;
}

