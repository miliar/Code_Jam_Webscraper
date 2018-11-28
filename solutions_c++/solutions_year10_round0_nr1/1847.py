#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>

#include <iostream>
#include <sstream>
#include <string>

#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <algorithm>
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
//#define FOR2(i,a,b) for (int i = (a); i > (b); --i)
/*
#define FOR(i,n)      for (int i=0; i<(n); i++)
#define FORTO(i,a,b)  for (int i=(a); i<=(b); i++)
#define FORD(i,n)     for (int i=(n)-1; i>=0; i--)
*/

#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define SIZE(x) int(x.size())

typedef pair<int,int> PII;
typedef long long ll;

void Solve(int testcase)
{
	printf("Case #%d: ", testcase+1);

	ll N, K, c = 1;
	scanf(" %lld %lld", &N, &K);

	while (K & 1) {
		c++; K >>= 1;
	}

	if (N < c) printf("ON\n");
	else printf("OFF\n");
}

int main()
{
	int T;
	scanf(" %d", &T);

	FOR (t, 0, T)
		Solve(t);

	return 0;
}
