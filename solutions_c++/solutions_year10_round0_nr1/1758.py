#include <iostream>
using namespace std;

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int t,cas=1;
	int n,m;

	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&n,&m);
		int tmp=(1<<n);
		m%=(tmp);

		printf("Case #%d: ",cas++);
		if(m==tmp-1) puts("ON");
		else puts("OFF");
	}
}