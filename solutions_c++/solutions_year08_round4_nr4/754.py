#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>

using namespace std;

#define FOR(i, lo, hi) for(int i = (lo); i < (hi); ++i)
#define MP make_pair
#define PB push_back

typedef long long ll;

char s[65536];
char t[65536];
int len, k;

int getLength(vector<int> &v)
{
	int rep = len / k;
	FOR(i, 0, rep)
	{
		FOR(j, 0, k)
		{
			t[i * k + j] = s[i * k + v[j] - 1];
		}
	}

	char cur = '#';
	int ct = 0;
	FOR(i, 0, len)
	{
		if(t[i] != cur)
		{
			++ct;
			cur = t[i];
		}
	}

	return ct;
}

int main()
{
	int numCases;
	scanf("%d", &numCases);

	FOR(tc, 1, numCases + 1)
	{
		scanf("%d", &k);
		scanf("%s", s);
		len = strlen(s);
		
		vector<int> v;
		FOR(i, 1, k + 1) v.PB(i);

		int best = len;
		do
		{
			best = min(best, getLength(v));
		}
		while(next_permutation(v.begin(), v.end()));

		printf("Case #%d: %d\n", tc, best);
	}

	return 0;
}
