#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<list>
#include<functional>
#include<algorithm>

using namespace std;

//#define _INFILE		"A.in"
//#define _OUTFILE	"A.out"

//#define _INFILE		"A-small-attempt0.in"
//#define _OUTFILE	"A-small.out"

#define _INFILE		"A-large.in"
#define _OUTFILE	"A-large.out"
typedef long long lint;

void solve()
{
	int n;
	scanf("%d",&n);
	vector<pair<lint, lint> > v;
	vector<lint> v1;
	for(int i=0; i<n; i++)
	{
		lint dd, ll;
		scanf("%lld%lld",&dd,&ll);
		v.push_back(make_pair(dd, ll));
		v1.push_back(0);
	}
	lint D;
	scanf("%lld",&D);
	v1[0] = v[0].first + v[0].first;
	for(int i=0; i<n; i++)
	{
		lint d1, l1;
		d1 = v[i].first;
		l1 = v[i].second;

		for(int j=i+1; j<n; j++)
		{
			lint d2, l2;
			d2 = v[j].first;
			l2 = v[j].second;
			if (v1[i] < d2) break;
			v1[j] = max(v1[j], d2 + min(d2 - d1, l2));
		}
		if (v1[i] >= D)
		{
			printf("YES\n");
			return;
		}
	}

	printf("NO\n");
}

int main(void)
{
	int T;
	freopen(_INFILE, "r", stdin);
	freopen(_OUTFILE, "w", stdout);

	scanf("%d",&T);

	for(int i=0; i<T; i++)
	{
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}

