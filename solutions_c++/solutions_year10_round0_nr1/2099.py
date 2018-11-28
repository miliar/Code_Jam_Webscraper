//Arek Wróbel - skater
#include <cstdio>
using namespace std;

int n, k;

bool wy;

int main()
{
	int t;
	scanf("%d", &t);
	for (int lpt=1; lpt<=t; ++lpt)
	{
		//wej
		scanf("%d%d", &n, &k);
		//prog
		wy=true;
		for (; n && wy; --n)
			if (k & 1)
				k = k >> 1; else
				wy=false;
		//wyj
		printf((wy ? "Case #%d: ON\n" : "Case #%d: OFF\n"), lpt);
	}
	return 0;
}
