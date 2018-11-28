#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <memory.h>
#include <cmath>
#include <cassert>

using namespace std;

#define fr(i,a,b) for(int i = (a); i <= (b); ++i)
#define fi(a) for(int i = (0); i < (a); ++i)
#define fj(a) for(int j = (0); j < (a); ++j)
#define fk(a) for(int k = (0); k < (a); ++k)

int n, k;

void solve()
{
	scanf("%d%d", &n, &k);
	fi(n)
		if (!(k & (1 << i)))
		{
			printf("OFF\n");
			return;
		}
	printf("ON\n");
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	fi(t)
	{
		printf("Case #%d: ", i + 1);
		solve();
	}
	return (0);
} 
