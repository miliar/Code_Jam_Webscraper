#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;

#define sz(v) int((v).size())
#define len(s) int(strlen(s))
#define inf 0x3f3f3f3f;
#define fori(i,c,f) for(int i = c; i < f; i++)
#define for0(i,f) fori(i,0,f)

int main(void)
{
	int tc;
	scanf("%d", &tc);

	for (int tcc = 1; tcc <= tc; tcc++)
	{
		int n, k;
		scanf("%d %d", &n, &k);
		printf("Case #%d: ", tcc);
		if (k == 0)
		{
			printf("OFF\n");
			continue;
		}
		printf((k + 1) % (int) pow(2, n) == 0? "ON" : "OFF");
		printf("\n");
	}

	return 0;
}
