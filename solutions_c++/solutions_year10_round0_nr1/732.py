#include <cstdio>

using namespace std;

int main(int argc, char *argv[])
{
	int t;
	scanf("%d", &t);
	for (int c = 0; c < t; c++)
	{
		int n, k;
		scanf("%d %d", &n, &k);
		bool b = true;
		for (int i = 0; (i < n) && b; i++)
		{
			b = b && (k % 2);
			k /= 2;
		}
		printf("Case #%d: %s\n", c + 1, b ? "ON" : "OFF");
	}
	return 0;
}