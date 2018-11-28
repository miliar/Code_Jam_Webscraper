#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		int n, k;
		scanf("%d %d", &n, &k);
		printf("Case #%d: ", t);
		
		int N = (1 << n) - 1;
		printf("%s\n", ((k & N) == N) ? "ON" : "OFF");
	}
}