#include <iostream>
#include <cstdio>
#include <algorithm>
#include <numeric>
#include <climits>
#include <sstream>
#include <cstring>
#include <cassert>
#include <vector>
#include <stack>
#include <queue>
#include <cmath>
#include <map>
#include <set>

#define INF (INT_MAX/3)

typedef long long lint;

using namespace std;

int main(int argc, char ** argv)
{
	int ntest;

	scanf("%d", &ntest);
	
	for (int t = 0; t < ntest; t++) {
		lint mtime, npeople, ngroup;
		lint result = 0;

		scanf("%lld %lld %lld", &mtime, &npeople, &ngroup);
		vector <lint> gsizes(ngroup, 0);
		vector <pair <lint, lint> > states(ngroup, make_pair(-1, -1LL));
		
		for (int i = 0; i < ngroup; i++)
			scanf("%lld", &gsizes[i]);
			
		lint when = 0, where = 0;
		lint done = 0;

		while (when < mtime) {
			if (done == 0) {
				if (states[where].first != -1) {
					lint dtime = when-states[where].first;
					lint dres = result-states[where].second;

					lint rtime = mtime-when, much = rtime/dtime;

					when += dtime * much;
					result += dres * much;

					done = 1;

					if (when >= mtime)
						break;
				} else
					states[where] = make_pair(when, result);
			}

			lint remain = npeople-gsizes[where];

			result += gsizes[where];

			int j;
			for (j = (where+1)%ngroup; j != where && remain >= gsizes[j]; j = (j+1)%ngroup) {
				remain -= gsizes[j];
				result += gsizes[j];
			}

			where = j;
			when ++;
		}

		printf("Case #%d: %lld\n", t+1, result);
	}

	return 0;
}
