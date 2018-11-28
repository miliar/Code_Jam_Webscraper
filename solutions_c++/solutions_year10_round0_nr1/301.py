#include <iostream>
using namespace std;
int num[32];
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int i;
	num[0] = 1;
	for (i=1;i<32;++i)
	{
		num[i] = num[i-1] * 2;
	}

	int T;
	scanf("%d",&T);
	int b = 1;
	while (T--)
	{
		int k,n;
		scanf("%d%d",&n,&k);
		if (k%num[n] == num[n]-1)
		{
			printf("Case #%d: ON", b++);
		}
		else
		{
			printf("Case #%d: OFF", b++);
		}
		puts("");
	}
	return 0;
}