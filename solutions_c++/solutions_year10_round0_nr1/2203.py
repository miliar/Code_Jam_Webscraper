#include <cstdio>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int n,k;
		scanf("%d%d",&n,&k);
		int m=(1<<n)-1;
		printf("Case #%d: %s\n",i,(k&m)==m?"ON":"OFF");
	}
	return 0;
}
