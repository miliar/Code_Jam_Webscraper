#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int T, N, K;
	cin >> T;
	for (int t = 1; t <= T; t ++)
	{
		cin >> N >> K;
		printf("Case #%d: ", t);
		if (K % (1 << N) == (1 << N) - 1) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}
