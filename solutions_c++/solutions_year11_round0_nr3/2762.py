#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<sstream>
#include<vector>
#include<set>
#include<map>
#include<algorithm>

using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define EACH(i,x) REP(i,(x).size())
#define sz	size()
#define all(x) ((x).begin, (x).end)
#define eps	1e-15

typedef long long int lint;

lint solve()
{
	int n;
	scanf("%d",&n);
	int total = 0;
	vector<int> v;
	v.reserve(n);
	lint sum = 0;
	REP(i,n) {
		int t;
		scanf("%d",&t);
		total ^= t;
		sum += t;
		v.push_back(t);		
	}
	lint maxsean = -1;
	set<pair<int, lint> > s[1001];

	int bound = (n-1)/2;
	s[0].insert( make_pair(0, 0LL) );

	for(int i=0; i<n; i++) {
		int j = min(i, bound);
		for(int j=bound; j>=0; j--) {
			set<pair<int, lint> >::iterator it;
			for(it=s[j].begin(); it != s[j].end(); ++it) {
				int t = (it->first) ^ v[i];
				lint ss = (it->second) + v[i];
				if ( t == (total ^ t) ) {
					lint sean = max(ss, sum - ss);
					maxsean = max(maxsean, sean);
				}
				s[j+1].insert(make_pair(t, ss) );
			}
		}
	} 

	return maxsean;
}

int main(void)
{
	int T;
	scanf("%d",&T);

	REP(i,T) {
		printf("Case #%d: ", i+1);
		lint result = solve();
		if ( result == -1 )
			printf("NO\n");
		else printf("%I64d\n",result);
	}

	return 0;
}

