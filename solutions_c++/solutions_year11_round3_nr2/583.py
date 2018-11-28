#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <ctime>

using namespace std;

typedef long long lint;

int l, n, c, a[1001];
lint ctm, d[1001], parsec[1001];

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("7s.out", "w", stdout);
	int t; cin>>t;
	for (int k=1; k<=t; k++) {
		cout<<"Case #"<<k<<": ";
		cin>>l>>ctm>>n>>c;
		d[0]=0;
		for (int i=0; i<c; i++) {
			cin>>a[i];
			d[i+1] = d[i]+a[i];
		}
		for (int i=c; i<n; i++) d[i+1]=d[i]+a[i%c];

		if (l==0) {
			cout<<d[n]+d[n]<<endl;
		}
		else if (l==1) {
			lint min = d[n]+d[n], tmp;
			for (int i=1; i<=n; i++) {
				tmp = d[n]+d[n];
				if (ctm/2<=d[i-1]) tmp-=(d[i]-d[i-1]);
				else if (ctm/2<d[i]) {
					tmp-=(d[i]-ctm/2);
				}
				if (tmp<min) min=tmp;
			}
			cout<<min<<endl;
		}
		else if (l==2) {
			lint min = d[n]+d[n], tmp, minus;
			for (int i=1; i<n; i++) {
				for (int j=i+1; j<=n; j++) {
					tmp = d[n]+d[n];
					minus=0;
					if (ctm/2<=d[i-1]) {
						tmp-=(d[i]-d[i-1]);
						minus=d[i]-d[i-1];
					}
					else if (ctm/2<d[i]) {
						tmp-=(d[i]-ctm/2);
						minus=d[i]-ctm/2;
					}

					if (ctm/2+minus<=d[j-1]) {
						tmp-=(d[j]-d[j-1]);
					}
					else if (ctm+minus<d[j]) {
						tmp-=(d[j]-minus-ctm/2);
					}
					if (tmp<min) min=tmp;
				}
			}
			cout<<min<<endl;
		}
	}

	return 0;
}
