#include<iostream>
using namespace std;

int main()
{
	freopen("intput.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		int n, k;
		scanf("%d %d", &n, &k);
		if (k % (1 << n) == (1 << n) - 1) 
			printf("ON\n");
		else printf("OFF\n");
	}
}