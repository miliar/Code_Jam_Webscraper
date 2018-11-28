#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

#define MAXN 10005

int n, test;
int d[MAXN], l[MAXN], res[MAXN];

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	scanf("%d", &test);
	for (int t=1; t<= test; ++t){
		scanf("%d", &n);
		for (int i=0; i<n; ++i)
			scanf("%d%d", &d[i], &l[i]);
		memset(res, -1, sizeof(res));
		res[0] = d[0];
		scanf("%d", &d[n]);
		l[n] = 0;
		for (int i=1; i<=n; ++i)
			for (int j=0; j<i; ++j)
				if (res[j] != -1 && res[j] + d[j] >= d[i])
					res[i] = max(res[i], min(l[i], d[i] - d[j]));
		if (res[n]!=-1)
			printf("Case #%d: YES\n", t);
		else
			printf("Case #%d: NO\n", t);
	}
	return 0;
}