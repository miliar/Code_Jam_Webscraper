#include <cstdio>

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);

	int qn = 0;
	while (T--)
	{
		qn++;
		int x, y;
		scanf("%d%d", &x, &y);
		printf("Case #%d: ", qn);
		int t = (1 << x) - 1;
		if ((y & t) == t) printf("ON\n"); else printf("OFF\n");
	}
}

