#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>

using namespace std;

#define nul(a) memset(a, 0, sizeof(a))
int res[5001];
int tt[5001];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d", &t);
	for (int ti = 1; ti <= t; ti++){
		int k, n;
		scanf("%d%d", &k, &n);
		int last=-1;
		for (int i = k, z = 1; i >= 1; i--, z++){
			int pos = (i - 1)  % z + 1;
			for (int j = 1; j <= z; j++)
				tt[(j + pos -1) % z +1] = res[j];
			memcpy(res, tt, sizeof(tt));
			res[pos] = i;
		}
		printf("Case #%d:",ti);
		for (int i = 0; i < n; i++){
			int b;
			scanf("%d", &b);
			printf(" %d", res[b]);
		}
		printf("\n");

	}
	return 0;
}