#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

#define tr(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define x first
#define y second

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef long long ll;

pair<pair<int,int>, int> b[1010];

void test()
{
	vector<pair<int,int> > all;
	int x,s,r,n;
	double res=0,t;
	scanf("%d%d%d%lf%d", &x, &s, &r, &t, &n);
	for(int i = 0; i < n; i++) scanf("%d%d%d", &b[i].x.x, &b[i].x.y, &b[i].y);
	sort(b,b+n);
	int last = 0;
	for(int i = 0; i < n; i++)
	{
		if(b[i].x.x > last) all.push_back(make_pair(0, b[i].x.x-last));
		all.push_back(make_pair(b[i].y, b[i].x.y-b[i].x.x));
		last = b[i].x.y;
	}
	if(last < x) all.push_back(make_pair(0, x-last));
	sort(all.begin(), all.end());
	for(int i = 0; i < all.size(); i++)
	{
		int w = all[i].x, len = all[i].y;
		double dist = 1.0 * t * (w+r);
		if(dist > len) dist = len;
		double trun = 1.0 * dist / (w+r), twalk = 1.0 * (len-dist) / (w+s);
		res += trun + twalk;
		t -= trun;
	}
	printf("%.7lf\n", res);
}

int main()
{
	int tt;
	scanf("%d", &tt);
	for(int i = 1; i <= tt; i++)
	{
		printf("Case #%d: ", i);
		test();
	}
}
