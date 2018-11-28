#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <cstddef>
#include <algorithm>
#include <utility>
#include <iterator>
#include <numeric>
#include <list>
#include <complex>
#include <cstdio>
#include <climits>

using namespace std;
typedef long long ll;
const int MAXN = 2000;
struct Circle{
	int id, r;
	int x, y;
	bool operator < (const Circle &c)const{
		return r < c.r;
	}
};
Circle cir[2000];
bool cmp(const Circle &c1, const Circle &c2){
	return c1.id < c2.id;
}
int main()
{
	int T, n, w, l;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	cin>>T;
	for(int tt = 1; tt <= T; ++tt){
		cin>>n>>w>>l;
		for(int i = 0; i < n; ++i){
			cin>>cir[i].r;
			cir[i].id = i;
		}
		sort(cir, cir + n);
		bool wl = false;
		if(w < l){
			swap(w, l);
			wl = true;
		}
		int x = 0, y = -INT_MAX;
		int nc = 0;
		while(nc < n && y + cir[nc].r <= l){
			cir[nc].x = 0;
			//cir[nc].y = max(y + cir[nc].r, 0);
			int old_nc = nc;
			int len = cir[nc++].r;
			while(nc < n && len + cir[nc].r <= w){
				len += cir[nc].r * 2;
				cir[nc].x = len - cir[nc].r;
				++nc;
			}
			y = max(y + 2*cir[nc-1].r, cir[nc-1].r);
			while(old_nc < nc){
				cir[old_nc++].y = y - cir[nc - 1].r;
			}
		}
		cout<<"Case #"<<tt<<":";
		if(nc < n){cout<<"wrong"<<endl;}
		sort(cir, cir + n, cmp);
		for(int i = 0; i < n; ++i){
			if(wl)swap(cir[i].x, cir[i].y);
			cout<<' '<<cir[i].x<<' '<<cir[i].y;
		}
		cout<<endl;
	}

	return 0;
}
