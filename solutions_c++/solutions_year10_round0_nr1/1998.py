#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		int n, k;
		scanf("%d %d", &n, &k);
		
		printf("Case #%d: ", t + 1);
		if ((k & ((1 << n) - 1)) == (1 << n) - 1)
			printf("ON\n");
		else
			printf("OFF\n");
	}



	return 0;
}
