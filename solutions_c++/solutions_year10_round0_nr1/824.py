#include <iostream>

using namespace std;


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; i++)
	{
		int n, k;
		scanf("%d%d", &n, &k);
		int p = 1 << n;
		k++;
		printf("Case #%d: ", i + 1);
		if(k % p == 0)
		{
			printf("ON\n");
		}
		else
		{
			printf("OFF\n");
		}
	}
	return 0;
}