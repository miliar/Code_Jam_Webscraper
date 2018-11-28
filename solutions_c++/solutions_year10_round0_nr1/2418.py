
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

//

int main(void)
{
	int n, k;
	int nc;

	scanf("%d", &nc);
	for(int ca=1; ca<=nc; ca++)
	{
		printf("Case #%d: ", ca);

		scanf("%d %d", &n, &k);

		k %= (1<<n);

		if(k == (1<<n)-1)
			printf("ON\n");
		else
			printf("OFF\n");
	}

	return 0;
}
