// projA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <set>
#include <map>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

typedef __int64 ll;

int d[5050];
int n;

int a[5050];

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int nt;
	scanf("%d", &nt);

	for (int test = 1; test <= nt; test++) {
		int K;
		scanf("%d", &K);

		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", d+i);
		}

		memset(a,0xff,sizeof(a));

		int p = 0;
		for (int i = 1; i <= K; i++) {
			int z = i-1;
			while (a[p] != -1 || z) {
				if (a[p]==-1) {
					z--;
				}
				p = (p+1)%K;
			}
			a[p] = i;
		}

		printf("Case #%d:", test);
		for (int i = 0; i < n; i++) {
			printf(" %d", a[d[i]-1]);
		}
		printf("\n");
	}


	return 0;
}

