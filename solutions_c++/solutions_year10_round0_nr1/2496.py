#include <iostream>
#include <string>
#include <string.h>
#include <vector>
#include <math.h>
#include <set>
#include <time.h>
#include <algorithm>
using namespace std;

int main()
{
	freopen("d:\\A-large.in", "r", stdin);
	freopen("d:\\A-large.out", "w", stdout);

	int n, k;
	int T;
	int c = 0;
	scanf("%d", &T);
	while(T--)
	{
		scanf("%d%d", &n, &k);
		int L = n;
		printf("Case #%d: ", ++c);
		if(k % (1 << L) == (1 << L) - 1)  printf("ON\n");
		else  printf("OFF\n");
	}
}