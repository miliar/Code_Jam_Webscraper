#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <set>
#include <algorithm>
#include <queue>
#include <cassert>
#include <fstream>
#include <sstream>
#include <bitset>
#include <stack>
#include <list>
#define debug1(x) cout << #x" = " << x << endl;
#define debug2(x, y) cout << #x" = " << x << " " << #y" = " << y << endl;
#define debug3(x, y, z) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << endl;
#define debug4(x, y, z, w) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << " " << #w" = " << w << endl;
using namespace std;

int T;
int testid;

void init()
{
	int N;
	int sum = 0;
	int smallest = 99999999;
	cin >> N;

	int xor = 0;
	for (int i = 0; i < N; ++i)
	{
		int d;
		cin >> d;
		xor ^= d;
		sum += d;
		smallest = min(smallest, d);
	}

	if (xor == 0)
		printf("Case #%d: %d\n", testid, sum - smallest);
	else
		printf("Case #%d: NO\n", testid);
}

void york()
{
}

int main()
{
	scanf("%d", &T);
	for (testid = 1; testid <= T; ++testid)
	{
		init();
		york();
	}

	return 0;
}



