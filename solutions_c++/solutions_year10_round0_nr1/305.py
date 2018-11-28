#include <iostream>

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	int n, k;
	bool flag = false;
	for (int ca = 1; ca <= T; ca++) {
		scanf("%d %d", &n, &k);
		flag = false;
		
		int init_on = (1 << n) - 1;
		if ((k - init_on) % (1 << n) == 0) flag = true;
		
		printf("Case #%d: ", ca);
		if (flag) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}

