#include <cstdio>

using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	
	for(int i=1;i<=t;i++){
		int n,k;
		scanf("%d%d",&n,&k);
		int all_one=(1<<n)-1;
		bool light_on=(k&all_one)==all_one;
		printf("Case #%d: %s\n",i,light_on?"ON":"OFF");
	}
	
	return 0;
}
