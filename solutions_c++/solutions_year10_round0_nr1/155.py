#include <iostream>

using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	int cse=0;
	while(t--)
	{
		cse++;
		int n,k;
		scanf("%d%d",&n,&k);
		bool ok=false;
		if((k&((1<<n)-1))==(1<<n)-1) ok=true;
		printf("Case #%d: %s\n",cse,ok?"ON":"OFF");
	}
	return 0;
}
