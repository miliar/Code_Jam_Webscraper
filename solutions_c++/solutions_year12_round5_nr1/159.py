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
//#define _OUTFILE	"A-small1.out"

#define _INFILE		"A-large.in"
#define _OUTFILE	"A-large.out"
typedef long long lint;

struct S
{
	int a;
	int b;
	int c;

	bool operator < (const S& rhs) const
	{
		int l = a * rhs.b;
		int r = b * rhs.a;
		if (l == r) return c < rhs.c;
		return l < r;
	}
};

void solve()
{
	int n;
	scanf("%d",&n);

	vector<S> a;
	for(int i=0; i<n; i++){
		S s;
		int t;
		scanf("%d",&t);
		s.a = t;
		s.b = 0;
		s.c = i;
		a.push_back(s);
	}

	for(int i=0; i<n; i++){
		int t;
		scanf("%d",&t);
		a[i].b = t;
	}

	sort(a.begin(), a.end());
	for(int i=0; i<n; i++)
		printf(" %d", a[i].c);
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

