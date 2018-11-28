#include <iostream>

using namespace std;

int main(void)
{
	string str;
	int cnt;

	freopen("A-large.in.txt","r",stdin);
	freopen("A-large.out.txt","w",stdout);
	scanf("%d", &cnt);
	unsigned long n, k, shr;
	for (int i = 1; i <= cnt; ++i)
	{
		scanf("%ld %ld", &n, &k);
	
		printf("Case #%d: ", i);
		shr = (1 << n) - 1;
		if ((k & shr) == shr)
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}