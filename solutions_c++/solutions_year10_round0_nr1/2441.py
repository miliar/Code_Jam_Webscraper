#include <iostream>
#include <string>
#include <cmath>
using namespace std;
const int maxn = 101;
bool state[maxn];
int main()
{
	int i, j, t, n, k, c = 0;
	//freopen("A-small-attempt1.in", "r", stdin);
	//freopen("A-small-attempt1.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &t);
	for (c = 0; c < t; c++)
	{
		bool on = false;
		scanf("%d %d", &n, &k);
		int p = (int)pow(2.0, n);
		if ((k + 1) % p == 0)
		{
			on = true;
		}
		printf("Case #%d: %s\n", c + 1, on ? "ON" : "OFF");
	}
	return 0;
}
