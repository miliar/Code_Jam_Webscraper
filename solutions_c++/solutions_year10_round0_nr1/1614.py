
#include <iostream>
using namespace std;

int main()
{
	freopen("F://Google Code Jam//A-large.in","r",stdin);
	freopen("F://Google Code Jam//write.txt","w",stdout);
	int T,t =1,n,k;
	scanf("%d",&T);
	while(t<=T)
	{
		printf("Case #%d: ",t);
		t++;

		scanf("%d %d",&n,&k);
		if((1<<n)-1 == k%(1<<n))
			printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}