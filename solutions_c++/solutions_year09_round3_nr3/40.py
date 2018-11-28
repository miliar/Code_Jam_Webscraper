#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <algorithm>
#include <cassert>
#include <string>
#include <cmath>
#include <map>
#include <set>

using namespace std;

const int qmax = 111;
const int inf = (int)1e+9;

int a[qmax][qmax];
int x[qmax];

int go(int i, int j)
{
	if (a[i][j] != -1) return a[i][j];
	int & r = a[i][j];
	if (i + 1 >= j) return (r = 0);
	r = inf;
    for (int k = i + 1; k < j; ++k)
    	r = min(r, go(i, k) + go(k, j) + x[j] - x[i] - 2);
    return r;
}

int main()
{
	int test_cnt;
	scanf("%d", &test_cnt);
	for (int test_id = 1; test_id <= test_cnt; ++test_id)
	{
		int p, q;
        cin >> p >> q;
        for (int i = 1; i <= q; ++i)
        	cin >> x[i];
        x[0] = 0, x[q + 1] = p + 1;

        memset(a, -1, sizeof(a));
        printf("Case #%d: %d\n", test_id, go(0, q + 1));
    }

	return 0;
}
