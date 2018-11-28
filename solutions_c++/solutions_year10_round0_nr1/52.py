#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define pb push_back
#define mp make_pair

typedef long long li;
typedef pair<int, int> pt;
typedef long double ld;

const ld PI = 2 * acos(0.0);
const int N = 6000;

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("outp.txt", "wt", stdout);

	int t;
	scanf("%d", &t);
	for1(it, t)
	{
		int n, k;
		scanf("%d%d", &n, &k);
		++k;
		printf("Case #%d: ", it);
		if(k % (1 << n) == 0)
			puts("ON");
		else
			puts("OFF");			
	}

	return 0;
}
