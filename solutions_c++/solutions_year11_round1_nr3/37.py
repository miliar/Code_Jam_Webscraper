#include <iostream>
#include <cstdio>
#include <math.h>
#include <string>
#include <string.h>
#include <algorithm>
#include <vector>
#include <time.h>
using namespace std;
const int maxn = 100+10;
struct node
{
	int c, s, t;
} a[maxn];
int n, m;
bool mark[maxn];

int getans()
{
	int ans = 0;
	memset(mark,0,sizeof(mark));
	int r = n+1, t = 1;
	int c0max, c1max, c0k, c1k;
	bool bj;
	while (t--) {
		bj = false;
		for (int i = 1; i != r; ++i) 
			if (!mark[i]  &&  a[i].t>0) {
				mark[i] = true;
				ans += a[i].s;
				if (r<=n+m)	r += a[i].c;
				t += a[i].t;
				bj = true;
				break;
			}
		if (!bj) {
			c0max = -1; c1max = -1;
			for (int i = 1; i != r; ++i)
				if (!mark[i] && a[i].c==0 && a[i].s>c0max) {
					c0max = a[i].s;
					c0k = i;
				}
			for (int i = 1; i != r; ++i)
				if (!mark[i] && a[i].c==1 && a[i].s>c1max) {
					c1max = a[i].s;
					c1k = i;
				}
			if (c1max<0 && c0max<0) break;
			if (c1max>=c0max) {
				mark[c1k] = true;
				if (r<=n+m) r += a[c1k].c;
				ans += a[c1k].s;
			} else 
			if (c1max<0) {
				mark[c0k] = true;
				if (r<=n+m) r += a[c0k].c;
				ans += a[c0k].s;
			} else {
				int x = rand()%10;
				if (x<5) {	
					mark[c1k] = true;
					if (r<=n+m) r += a[c1k].c;
					ans += a[c1k].s;
				} else {	
					mark[c0k] = true;
					if (r<=n+m) r += a[c0k].c;
					ans += a[c0k].s;
				}
			}
		}
	}
	return ans;
}

void init()
{
	cin >> n;
	for (int i = 1; i <= n; ++i) cin >> a[i].c >> a[i].s >> a[i].t;
	cin >> m;
	for (int i = 1; i <= m; ++i) cin >> a[i+n].c >> a[i+n].s >> a[i+n].t;
}

int main()
{
	srand( (unsigned)time(NULL) );
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C3.out","w",stdout);
	int TextNum, Tnum = 0;
	int ans, tmp;
	cin >> TextNum;
	while (TextNum--) {
		cout << "Case #" << ++Tnum << ": ";
		init();
		ans = -1;
		for (int tt = 0; tt <= 5000; ++tt) {
			tmp = getans();
			if (tmp>ans) ans = tmp;
		}
		cout << ans << endl;
	}
	
	return 0;
}