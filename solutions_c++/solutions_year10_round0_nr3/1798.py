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
typedef unsigned long long ull;

#define MAXG 1010

// cash after i-th ride
// sizes of groups in the order as in line
// after which ride was the group first in the line
ull cash[MAXG], groups[MAXG];
int first[MAXG];

void Solve(int testcase)
{
	printf("Case #%d: ", testcase+1);

	memset(cash, 0, sizeof(cash));
	memset(groups, 0, sizeof(groups));
	memset(first, -1, sizeof(first));

	ull R, K, G;
	scanf(" %llu %llu %llu", &R, &K, &G);

	FOR (i, 0, G)
		scanf(" %llu", &groups[i]);

	ull rides = 0, gr = 0;
	
	while (first[gr] == -1 && rides < R) {

		first[gr] = rides;

		ull k = 0;
		while (k + groups[gr] <= K && (k == 0 || first[gr] != rides)) {
			k += groups[gr];
			gr = (gr+1)%G;
		}

		cash[rides+1] = cash[rides]+k;
		rides++;
	}

	if (rides == R) {
		printf("%llu\n", cash[rides]);
		return;
	}

	ull period = rides-first[gr];
	ull precash = cash[first[gr]];
	ull percash = cash[rides]-precash;
	ull ca = 0;

	R -= first[gr];
	ca += precash;
	ca += (R/period)*percash;
	ca += cash[first[gr]+(R%period)]-precash;

	printf("%llu\n", ca);
}

int main()
{
	int T;
	scanf(" %d", &T);

	FOR (t, 0, T)
		Solve(t);

	return 0;
}
