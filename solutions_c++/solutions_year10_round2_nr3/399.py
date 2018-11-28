
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

#define MAX 128

int v[MAX];
int n;
int ord;
int res;

void bt(int x)
{
	if(x == n)
	{
		v[x] = ord;
		while(v[x] != -1) x = v[x];
		if(x == 1) res++;
	}
	else
	{
		v[x] = ord;
		ord++;
		bt(x+1);
		ord--;

		v[x] = -1;
		bt(x+1);
	}
}

int main(void)
{
	int nc, ca;

	scanf("%d", &nc);
	for(ca=1; ca<=nc; ca++)
	{
		printf("Case #%d: ", ca);

		scanf("%d", &n);
		
		res = 0;
		ord = 1;
		v[1] = -1;
		bt(2);

		printf("%d\n", res % 100003);
	}

	return 0;
}
