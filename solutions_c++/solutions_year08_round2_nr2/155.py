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

int xx[100010];
int yy[100010];

using namespace std;

typedef __int64 ll;

char sm[1010][1010];

ll cnk(ll n, ll k) {
	if (n < k)
		return 0;
	ll ret = 1;
	for (ll i = 1; i <= k; i++) {
		ret = ret * (n-i+1) / i;
	}
	return ret;
}

int col[1010];

int A, B;

void fill(int x) {
	if (col[x])
		return;
	col[x] = 1;
	for (int i = A; i <= B; i++) {
		if (sm[x][i]) {
			fill(i);
		}
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int a[1010];
	int pr[1010];
	int npr = 0;
	memset(a,1,sizeof(a));
	for (int i = 2; i <= 1000; i++) {
		if (a[i]) {
			pr[npr++] = i;
			for (int j = 2*i; j <= 1000; j += i) {
				a[j] = 0;
			}
		}
	}

	int nt;
	scanf("%d", &nt);

	for (int test = 1; test <= nt; test++) {
		memset(sm,0,sizeof(sm));
		int  P;
		scanf("%d %d %d", &A, &B, &P);

		for (int x = A; x <= B; x++) {
			sm[x][x] = 1;
			for (int y = x+1; y <= B; y++) {
				for (int k = npr-1; k >= 0; k--) {
					if (pr[k] < P)
						break;
					if (x%pr[k]==0 && y%pr[k]==0) {
						sm[x][y] = sm[y][x] = 1;
						break;
					}
				}
			}
		}

		memset(col,0,sizeof(col));

		int ret = 0;
		for (int x = A; x <= B; x++) {
			if (col[x] == 0) {
				fill(x);
				ret++;
			}
		}

		cout << "Case #" << test << ": " << ret << endl;
	}


	return 0;
}

