#include<iostream>

using namespace std;

int main()
{
	int t;
	freopen("A-small-attempt2.in","r",stdin);
	freopen("out","w",stdout);

	scanf("%d",&t);
	int n,m;
	int cas=0;
	while (t--)
	{
		cas++;
		scanf("%d%d",&n,&m);
		int sz=(1<<n);
		m%=sz;
		printf("Case #%d: ",cas);
		if (m==sz-1)
			puts("ON");
		else
			puts("OFF");
	}
	return 0;
}