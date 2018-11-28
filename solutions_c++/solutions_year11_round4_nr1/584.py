#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>

using namespace std;


const int nmax = 1005;

struct el{
	int l,r,w;
};

el a[nmax];

bool cmp(el & a, el & b)
{
	return a.w < b.w;
}
 

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int nn;
	cin >> nn;
	for (int test = 1;test <= nn; ++test){

		int s,r,n;
		double t,x;
		cin >> x >> s >> r >> t >> n;

		for (int i = 0;i < n; ++i) cin >> a[i].l >> a[i].r >> a[i].w;

		int sumLen = 0;

		for (int i = 0;i < n; ++i) sumLen += a[i].r - a[i].l;

		double ans = 0;		

		a[n].l = 0;
		a[n].r = x - sumLen;
		a[n].w = 0;
		++n;

		sort(a,a+n,cmp);

		for (int i = 0;i < n; ++i)
		{
			double len = a[i].r - a[i].l;
			double v = a[i].w + r;
			double time = len / v;

			if (time <= t)
			{
				t -= time;
				ans += time;				
			}
			else
			{
				len -= v * (double) t;
				ans += t;
				double vv = a[i].w + s;
				ans += len / vv;							
				t = 0;
			}
		}
		
		printf("Case #%i: %.9lf\n",test,ans);		
	}
	
	return 0;
}