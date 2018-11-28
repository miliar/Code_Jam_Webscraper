#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <cassert>
#include <cstdlib>
#include <cstring>

using namespace std;

typedef long long LL;

#define sz(c) ((int) (c).size ())
#define pb push_back
#define mp make_pair
#define fi first
#define se second

LL N, K;

int main ()
{
	int T;
	scanf ("%d", &T);
	for (int test = 1; test <= T; test++)
	{
		scanf ("%lld%lld", &N, &K);
		LL t = (K + 1) % (1LL << N);
		printf ("Case #%d: ", test);
		puts ((t == 0 ? "ON" : "OFF"));
	}
	return 0;
}

