#include <cstdio>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	int nCase,n,k,case_Id=0,now;
	scanf("%d",&nCase);
	while(nCase--)
	{
		scanf("%d%d",&n,&k);
		now=1<<n;
		now--;
		if(now==(k & now))
			printf("Case #%d: ON\n",++case_Id);
		else
			printf("Case #%d: OFF\n",++case_Id);
	}
	return 0;
}