#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

// Google CodeJam 2012 Round 2
// Author: Fdg

pair<int,int> r[1001];

set < pair <int,int> > f1,f2;

int x[1001],y[1001];

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;++test) {
		printf("Case #%d:",test);
		int n,w,h;
		scanf("%d%d%d",&n,&w,&h);
		for(int i=0;i<n;++i) {
			scanf("%d",&r[i].first);
			r[i].second=i;
		}
		sort(r,r+n);
		reverse(r,r+n);
		bool sw=false;
		if (w<h) {
			swap(w,h);
			sw=true;
		}
/*		f1.clear(); f2.clear();
		int what=1;
		f1.insert(make_pair(r[0].first,r[0].first));
		int last=r[0].first;

		while(what<n) {
			f1.insert(make_pair());
		}*/
		for(int i=0;i<n;++i)
			x[i]=y[i]=-1;
		x[r[0].second]=y[r[0].second]=0;
		int last=r[0].first,what=1,left=n-1;
		bool ok[1001]={0}; ok[0]=true;
		while(what<n) {
			if (r[what].first+last<=w) {
				x[r[what].second]=last+r[what].first;
				y[r[what].second]=0;
				last+=2*r[what].first;
				ok[what]=true;
				--left;
			}
			what++;
		}
		while(left) {
			last=0;
			for(int i=0;i<n;++i) {
				if (ok[i]) continue;
				int low=0,L=last,R=last+2*r[i].first;
				for(int j=0;j<n;++j) {
					if (ok[j]) {
						int l=x[r[j].second]-r[j].first,ri=x[r[j].second]+r[j].first,up=y[r[j].second]+r[j].first;
						if (L<l&&l<R||L<ri&&ri<R||l<=L&&R<=ri)
							low=max(low,up);
					}
				}
				if (low+r[i].first<=h) {
					x[r[i].second]=last+r[i].first;
					y[r[i].second]=low+r[i].first;
					last+=2*r[i].first; left--;
					ok[i]=true;
				}
			}
		}
		if (sw) {
			for(int i=0;i<n;++i)
				swap(x[i],y[i]);
			swap(w,h);
		}
		bool good=true;
		for(int i=0;i<n;++i) {
			if (x[i]<0||x[i]>w||y[i]<0||y[i]>h) good=false;
			for(int j=0;j<n;++j)
				if (i!=j&&1LL*(x[r[i].second]-x[r[j].second])*(x[r[i].second]-x[r[j].second])+
					1LL*(y[r[i].second]-y[r[j].second])*(y[r[i].second]-y[r[j].second])<
					1LL*(r[i].first+r[i].second)*(r[i].first+r[i].second)) good=false;
		}
		if (!good)
			cout << "fail\n";
		for(int i=0;i<n;++i)
			printf(" %d %d",x[i],y[i]);
		printf("\n");
	}
	return 0;
}
