#include <cstdio>
#define CASEID printf("Case #%d: ",iD++)
#define CASES  for(scanf("%d",&cases);cases--;)
using namespace std;

int ans[]={0,1,1,2,3,5,8,14,24,43,77,140,256,472,874,1628,3045,5719,10780,20388,38674,73562,140268,268066,513350,984911};

int main()
{
	int cases,iD=1,n;
	
	CASES
	{
		scanf("%d",&n);
		CASEID;
		printf("%d\n",ans[n]%100003);
	}
	return 0;
}
