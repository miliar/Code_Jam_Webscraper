#include <cstdio>
using namespace std;

int n,k;

bool on(int n,int k)
{
	return !(~k&((1<<n)-1));
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int t1=1;t1<=t;++t1)
	{
		scanf("%d %d",&n,&k);
		printf("Case #%d: %s\n",t1,on(n,k)?"ON":"OFF");
	}
	return 0;
}
