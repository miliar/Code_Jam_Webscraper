// by shik
#include <iostream>
using namespace std;
int main()
{
	int t,T,n,k;
	scanf("%d",&T);
	for ( t=1; t<=T; t++ ) {
		scanf("%d%d",&n,&k);
		printf("Case #%d: %s\n",t,(k+1)%(1<<n)==0?"ON":"OFF");
	}
	return 0;
}
