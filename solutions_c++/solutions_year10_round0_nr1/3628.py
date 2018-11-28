#include <iostream>
using namespace std;
int main()
{
	int T,Ti;
	scanf("%d",&T);
	for(Ti = 1;Ti<=T;Ti++)
	{
		int n,k;
		scanf("%d%d",&n,&k);

		bool flag = false;
		
		printf("Case #%d: ",Ti);

		unsigned int t = 1;
		t = (t << n) ;
		t--;

		if((k & t) == t)
			printf("ON");
		else
			printf("OFF");
		puts("");
		
	}
}