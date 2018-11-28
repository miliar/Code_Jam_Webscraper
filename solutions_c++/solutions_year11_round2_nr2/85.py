// GCJ 2011 R1B
// wookayin

// B

#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>

#define infile "B-large.in"
#define outfile "B-large.out"

#define REP(i, n) for(int i=0; i<(int)(n); ++i)

using namespace std;

int n, D;
int point[1000000], amt[1000000];

vector<int> locs;

bool able(long long time_by_2)
{
	long long leftmost = locs[0] * 2 - time_by_2;
	long long deadline = leftmost + D * 2;

	for(int i = 1; i < (int)locs.size(); ++ i)
	{
		long long mypos = max(deadline, locs[i] * 2 - time_by_2);
		if( abs(mypos - locs[i] * 2) > time_by_2)
			return false;
		deadline = mypos + D * 2;
	}
	return true;
}

double go()
{
	long long l = 0, r = 1LL<<60;
	long long ans = 0;
	while(l <= r)
	{
		long long x = (l+r) / 2;
		if( able(x) )
		{
			r = x - 1;
			ans = x;
		}
		else
		{
			l = x + 1;
		}
	}
	return ans / 2.0;
}
int main()
{
	freopen(infile, "r", stdin);
	freopen(outfile, "w", stdout);

	int T;
	scanf("%d", &T);
	for(int tt=1; tt<=T; ++tt)
	{
		printf("Case #%d: ", tt);
		fprintf(stderr, "%d\n", tt);

		scanf("%d %d", &n, &D);
		locs.clear();
		locs.reserve(n);
		for(int i=0; i<n; ++i)
		{
			scanf("%d %d", &point[i], &amt[i]);
			REP(q, amt[i]) locs.push_back(point[i]);
		}

		std::sort(locs.begin(), locs.end());
		printf("%.6lf\n", go());

	}
	return 0;
}