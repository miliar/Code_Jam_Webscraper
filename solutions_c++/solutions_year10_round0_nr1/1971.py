#include <iostream>


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d", &t);
	for(int a = 0; a < t; a++)
	{
		int n, k;
		scanf("%d%d", &n, &k);
		int timeToOn = 1 << n;
		printf("Case #%d: ", a + 1);
		if(k % timeToOn != timeToOn - 1)
			printf("OFF\n");
		else
			printf("ON\n");
	}
}