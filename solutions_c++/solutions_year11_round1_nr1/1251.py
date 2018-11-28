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

int T, testid;

void output(bool ans)
{
	if (ans) 
		printf("Case #%d: Possible\n", testid);
	else
		printf("Case #%d: Broken\n", testid);
}

void init()
{
	int N, Pd, Pg;
	cin >> N >> Pd >> Pg;

	if (Pg == 0 && Pd > 0) return output(false);
	if (Pg == 100 && Pd < 100) return output(false);

	for (int d = 1; d <= N; ++d)
		if (d * Pd % 100 == 0)
			return output(true);
	output(false);
}

void york()
{
}

int main()
{
	cin >> T;
	for (testid = 1; testid <= T; ++testid)
	{
		init();
		york();
	}
	return 0;
}



