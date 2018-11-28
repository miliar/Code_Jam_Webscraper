#if 1
#include <iostream>
#include <stdio.h>
using namespace std;
int L, H, N;
int freq[10000];
int main()
{
	int t;
	cin >> t;
	for (int cases = 1; cases <= t; cases++)
	{
		cin >> N >> L >> H;
		for (int i = 0; i < N; i++)
			cin >> freq[i];
		bool ans = false;
		printf("Case #%d: ", cases);
		for (int i = L; i <= H; i++)
		{
			bool check = true;
			for (int j = 0; j < N && check; j++)
				if (i % freq[j] != 0 && freq[j] % i != 0) 
				{
					//printf("%d %d\n", i, freq[j]);
						check = false;
				}
			if (check) {
				printf("%d\n", i);
				ans = true;
				break;
			}
		}
		if (!ans) puts("NO");
	}
	return 0;
}
#endif