/*
ID: mrdotmoon
LANG: C++
TASK: 1
*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;


int T, pd, pg, D, G;
long long N;

bool can()
{
	if (pd == 0 && pg == 0) return true;
	if (pd > 0 && pg == 0) return false;
	if (pd == 100 && pg == 100) return true;
	if (pd < 100 && pg == 100) return false;

	if (pd == 0 || pd == 100) return true;
	for (int i = 1; i <= 100; i++)
	{
		int fd = i * 100 / pd;
		if (fd * pd == i * 100) return fd <= N; 
	}
	return false;
}
int main ()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	scanf("%d", &T);
	for (int cases = 1; cases <= T; cases++)
	{
		scanf("%I64d%d%d", &N, &pd,&pg);
		printf("Case #%d: ", cases);
		if (can()) printf("Possible\n");
		else printf("Broken\n");
	}
	
}