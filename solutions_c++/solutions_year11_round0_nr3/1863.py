#include<cstdio>
#include<algorithm>
using namespace std;
#define MAX 1000001
int main()
{
	int t,n;
	FILE* pFile=fopen("33.out","w");
	scanf("%d",&t);
	for(int c=1;c<=t;c++)
	{
		scanf("%d",&n);
		int exor=0,mini=MAX,x,sum=0;
		for(int i=0;i<n;i++)
		{
			scanf("%d",&x);
			mini=min(mini,x);
			exor^=x;
			sum+=x;
		}
		if(exor!=0) fprintf(pFile,"Case #%d: NO\n",c);
		else fprintf(pFile,"Case #%d: %d\n",c,sum-mini);
	}
	return 0;
}