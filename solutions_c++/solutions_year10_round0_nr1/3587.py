/* One Year, One Dream!!! */
/* Mu +U */
#include <stdio.h>
#include <iostream>
#include <string>
#include <cstring>
#include <math.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
using namespace std;

int main()
{
    int test, n, k;
	freopen("a.out", "w", stdout);
	freopen("ain.txt", "r", stdin);
	scanf("%d", &test);
	for (int u=1; u<=test; u++)
	{
		scanf("%d %d", &n, &k);
        int m=(1<<n) -1 ;
		if ((k & m) == m) printf("Case #%d: ON\n", u);
		else printf("Case #%d: OFF\n", u);
	}
	return 0;
}
