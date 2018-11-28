//Fruit of Light
//FoL CC
//pineapple strawberry
#include <cstdio>
#include <stack>
#include <vector>
using namespace std;

int main()
{
	int t1;
	scanf("%d",&t1);
	for(int i1=0; i1<t1; i1++)
	{
		int n;
		scanf("%d",&n);
		int x1=0;
		int poc=0;
		int mini=11000000;
		for(int i=0; i<n; i++)
		{
			int x;
			scanf("%d",&x);
			x1^=x;
			poc+=x;
			mini=min(mini,x);
		}
		printf("Case #%d: ",i1+1);
		if(x1!=0) printf("NO\n");
		else printf("%d\n",poc-mini);
	}
return 0;
}