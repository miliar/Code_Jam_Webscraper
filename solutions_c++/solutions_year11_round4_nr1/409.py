#include <iostream>
#include <cstdio>
#include <math.h>
#include <string>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;
const long maxx = 1000005;
const long maxn = 1000005;
struct node 
{
	long s, t, w;
};
struct bnode
{
	long s, w;
};

node a[maxn];
bnode b[maxn];
long x, s, r, t, n;

double min(double a,double b)
{
	if (a<0) return b;
	if (b<0) return a;
	return (a<b)?a:b;
}

bool cmp(bnode a,bnode b)
{
	return a.w<b.w;
}

void work()
{
	double tmp;
	long h = 0;
	double f = 0, rt = 0;
	for (long h = 0; h != n; ++h) {
			if (double(t-rt)*(r+b[h].w)<b[h].s) {
				tmp = f + (t-rt) + double(b[h].s-(t-rt)*(r+b[h].w))/(s+b[h].w);
				f = tmp;
				rt = t;
			} else {
				tmp = f + double(b[h].s)/(r+b[h].w);
				f = tmp;
				rt = rt + double(b[h].s)/(r+b[h].w);
			}
	}
	printf("%.7lf\n",f);
}

void init()
{
	cin >> x >> s >> r >> t >> n;
	long sum = 0;
	for (int i = 0; i != n; ++i) {
		cin >> a[i].s >> a[i].t >> a[i].w;
		b[i].s = a[i].t - a[i].s;
		b[i].w = a[i].w;
		sum += b[i].s;
	}
	b[n].s = x - sum;
	b[n].w = 0;
	++n;
	sort(b,b+n,cmp);
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);

	int TextNum, Num = 0;
	long x,s,r,t,n;
	cin >> TextNum;
	while (TextNum--) {
		cout << "Case #" << ++Num << ": ";
		init();
		work();
	}

	return 0;
}
