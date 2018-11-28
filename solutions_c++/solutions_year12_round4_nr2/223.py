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
#include<cassert>

using namespace std;

//#define _INFILE		"B.in"
//#define _OUTFILE	"B.out"

//#define _INFILE		"B-small-attempt0.in"
//#define _OUTFILE	"B-small.out"

#define _INFILE		"B-large.in"
#define _OUTFILE	"B-large.out"
int n, w, l;

bool solve1(vector<pair<int, int> > &v, vector<pair<int, int> >& result)
{
	int x = 0, y = 0;
	int yy = v[0].first;
	for(int i=0; i<n; i++)
	{
		int p = v[i].second;
		int r = v[i].first;
		if (x > 0) x = x + r;
		if (x > w)
		{
			x = 0;
			y = yy + r;
			yy = y + r;
			if ( y > l ) return false;
		}
		result[p].first = x;
		result[p].second = y;
		x = x + r;
	}
}

void solve()
{
	scanf("%d%d%d",&n,&w,&l);
	vector<pair<int, int> > v;
	vector<pair<int, int> > result;
	for(int i=0; i<n; i++)
	{
		int t;
		scanf("%d",&t);
		v.push_back(make_pair(t, i));
		result.push_back(make_pair(0,0));
	}
	sort(v.begin(), v.end());
	reverse(v.begin(), v.end());
	if (solve1(v, result))
	{
		for(int i=0; i<n; i++)
			printf(" %d %d", result[i].first, result[i].second);
	}
	else {
		swap(w, l);
		bool flag = solve1(v, result);
		assert(flag);
		for(int i=0; i<n; i++)
			printf(" %d %d", result[i].second, result[i].first);
	}

	printf("\n");
}

int main(void)
{
	int T;
	freopen(_INFILE, "r", stdin);
	freopen(_OUTFILE, "w", stdout);

	scanf("%d",&T);

	for(int i=0; i<T; i++)
	{
		printf("Case #%d:", i+1);
		solve();
	}
	return 0;
}

